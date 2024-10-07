from typing import TypeVar
from abc import abstractmethod

from aiohttp import ClientSession

from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint
from aiolava.types.base import LavaType

from aiolava.exceptions.lava_exceptions import LavaRequestError

import logging


_LTT = TypeVar("_LTT", bound=LavaType)



class BaseClient:
    _BASE_URL = 'https://api.lava.ru'

    @abstractmethod
    def _prepare_request(self, payload: dict, headers: dict) -> tuple[dict, dict]:
        raise NotImplemented

    async def _execute_request(self, request: LavaEndpoint[_LTT]) -> _LTT:
        payload = request.model_dump(mode='json')
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
            text = await response.text()
            logging.error(f"Error while parsing response: {text}")
            data = await response.json()

            logging.info(f"Request: {data}")

        try:
            parsed_data = request.__returns__.model_validate(data)
            return parsed_data
        except Exception:
            raise LavaRequestError(
                data=data.get('data'),
                status=data.get('status'),
                error=data.get('error'),
                status_check=data.get('status_check')
            )


__all__ = [
    "BaseClient",
]
