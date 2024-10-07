from typing import TypeVar, Generic
from pydantic import BaseModel, Field, ConfigDict


_T = TypeVar("_T")


class LavaType(BaseModel):
    model_config = ConfigDict(frozen=True)


class RootMixin(BaseModel, Generic[_T]):
    def __iter__(self) -> _T:
        return iter(getattr(self, '__root__'))

    def __getitem__(self, item) -> _T:
        return getattr(self, '__root__')[item]