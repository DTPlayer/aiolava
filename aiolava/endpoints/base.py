from typing import Generic, TypeVar, Type, Final
from pydantic.v1 import BaseModel

from ..misc import HTTPMethod
from ..types.base import LavaType


_LTT = TypeVar("_LTT", bound=LavaType)


class LavaEndpoint(BaseModel, Generic[_LTT]):
    __http_method__: HTTPMethod
    __endpoint__: str
    __returns__: Type[_LTT]

    class Config:
        allow_mutation = False
