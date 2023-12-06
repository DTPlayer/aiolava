from typing import TypeVar
from abc import abstractmethod

from aiohttp import ClientSession

from .misc import HTTPMethod
from .endpoints.base import LavaEndpoint
from .types.base import LavaType


_LTT = TypeVar("_LTT", bound=LavaType)


class BaseClient:
    _BASE_URL = 'https://api.lava.ru'

    @abstractmethod
    def _prepare_request(self, payload: dict, headers: dict) -> tuple[dict, dict]:
        raise NotImplemented

    async def _execute_request(self, request: LavaEndpoint[_LTT]) -> _LTT:
        payload = request.dict(exclude_none=True)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        http_method = request.__http_method__
        url = request.__endpoint__

        payload, headers = self._prepare_request(payload, headers)

        request_call_arguments = {
            "method": http_method.value,
            "url": url,
            "headers": headers,
        }

        if http_method is HTTPMethod.GET:
            request_call_arguments.update({"params": payload})
        elif http_method is HTTPMethod.POST:
            request_call_arguments.update({"json": payload})
        else:
            raise KeyError(f"http method `{http_method}` not supports by lava client.")

        async with ClientSession(
                base_url=self._BASE_URL,
        ) as cs:

            response = await cs.request(**request_call_arguments)
            data = await response.json()

        parsed_data = request.__returns__.parse_obj(data)
        return parsed_data


__all__ = [
    "BaseClient",
]
