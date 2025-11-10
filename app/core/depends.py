from typing import Annotated

from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.store import Store

required_bearer = HTTPBearer()
optional_bearer = HTTPBearer(auto_error=False)

TokenDep = Annotated[HTTPAuthorizationCredentials, Depends(required_bearer)]
OptionalTokenDep = Annotated[
    HTTPAuthorizationCredentials | None,
    Depends(optional_bearer),
]


def get_store(request: Request) -> Store:
    return request.app.state.store


StoreDep = Annotated[Store, Depends(get_store)]
