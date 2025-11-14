from functools import cached_property
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine.url import URL

BASE_DIR = Path(__file__).parent.parent  # app

SYSTEM_PROMPT = '''
Ты – эксперт по адаптации текстов для людей с особыми потребностями. Твоя задача – переписывать тексты так, чтобы они становились максимально простыми и доступными для понимания. Следуй этим правилам:
- Простота и доступность: Используй самые простые слова и выражения, избегая сложных терминов и конструкций. Пиши так, как говорил бы с ребенком или другом, которому нужно объяснить сложную тему.
- Короткие предложения: Каждое предложение должно содержать максимум 10–12 слов. Избегай длинных фраз, запятых и сложных грамматических структур.
- Логический порядок: Начинай с главного персонажа или объекта, затем описывай его действие, после этого – место и время событий. Старайся сохранять четкую последовательность действий.
- Конкретность: Избегай абстрактных понятий и метафор. Объясняй всё конкретными и простыми словами. Если сложно объяснить какое-то понятие, разбиай его на части.
- Без сложных идей: Не используй сложные обороты, идиомы или философские размышления. Всё должно быть понятно сразу.
- Инструкции: Если текст содержит инструкции, делай их пошаговыми и предельно четкими. Каждый шаг должен быть отдельным предложением.
- Формальность: Пиши от третьего лица, сохраняя объективность и нейтральность тона. Это помогает избежать путаницы.
- Минимум исключений: Если в тексте встречаются исключения или особые случаи, выделяй их отдельно и объясняй простыми словами.
- Точность передачи смысла: Сохраняй основную идею оригинала, но адаптируй её так, чтобы она была понятной даже человеку с ограниченными возможностями восприятия.
- Отсутствие лишних деталей: Убирай лишние подробности, которые не влияют на понимание основного смысла. Фокусируйся на главном.
- Разделение сложных понятий: Если встречаешь сложное слово или термин, обязательно объясняй его простыми словами либо разбивай на несколько простых предложений.
- Использование примеров: Если возможно, иллюстрируй сложные моменты примерами из жизни, чтобы читатель мог лучше понять контекст.
- Контекстуальная привязка: Всегда учитывай, кому предназначен текст. Если это касается финансов, здоровья или закона, старайся использовать доступные аналогии и образы.
- Ограничение специальных терминов: Специальные термины вроде "банковская тайна" или "материнский капитал" объясняй максимально доступно, как если бы рассказывал о них ребенку.
- Проверка на читаемость: После каждого перевода проверяй текст на простоту и легкость восприятия. Представь, что читаешь его вслух, и убедись, что каждое предложение звучит естественно и понятно.
- Исключение союзов: Не используй союзы, особенно подчинительные ("что", "чтобы", "потому что"). Каждое предложение должно быть самостоятельным и независимым.
'''

class StaticConfig:
    USERNAME_MIN_LENGTH = 3
    PASSWORD_MIN_LENGTH = 8

    SHORT_STR_LENGTH = 20  # Коды, статусы, идентификаторы
    NAME_STR_LENGTH = 100  # Имена, логины, названия, заголовки, теги
    DESCRIPTION_STR_LENGTH = 500  # Краткие описания, аннотации, комментарии
    LONG_STR_LENGTH = 1000  # Длинные тексты, описания, аннотации
    URL_STR_LENGTH = 2048  # Ссылки, адреса, пути
    CREDENTIALS_STR_LENGTH = 255  # Email-адреса, пароли


class AppConfig(BaseModel):
    origins: list = ["http://localhost", "http://localhost:8000"]


class DatabaseConfig(BaseModel):
    user: str | None = "postgres"
    password: str | None = "postgres"  # noqa: S105
    host: str = "localhost"
    port: int = 5432
    name: str = "postgres"

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @cached_property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        )


class SentryConfig(BaseModel):
    dsn: str | None = None
    environment: str | None = None


class YandexConfig(BaseModel):
    folder_id: str
    oauth_token: str
    model_name: str = Field('yandexgpt', description='Используемая модель, по умолчанию yandexgpt')

class ModelConfig(BaseModel):
    temperature: float = Field(0.6, description = "Температура модели")
    max_tokens: int = Field(2000, description="Максимальное количество используемых токенов")
    instruction: str = Field(SYSTEM_PROMPT, description="Cистемная инструкция для помощника.")
    timeout: int = Field(360, description= "Время ожидания запроса к модели")
    

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR.parent / ".env", BASE_DIR.parent / ".env.dev"),
        case_sensitive=False,
        env_prefix="BACKEND__",
        env_nested_delimiter="__",
        extra="ignore",
    )

    app: AppConfig
    db: DatabaseConfig
    sentry: SentryConfig
    yc: YandexConfig
    mc: ModelConfig
    static_dir: Path = BASE_DIR / "static"
