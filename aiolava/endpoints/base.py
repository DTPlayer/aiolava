from typing import Generic, TypeVar, Type, Final
from pydantic import BaseModel, ConfigDict

from aiolava.misc import HTTPMethod
from aiolava.types.base import LavaType


_LTT = TypeVar("_LTT", bound=LavaType)


class LavaEndpoint(BaseModel, Generic[_LTT]):
    __http_method__: HTTPMethod
    __endpoint__: str
    __returns__: Type[_LTT]
    model_config = ConfigDict(frozen=False)