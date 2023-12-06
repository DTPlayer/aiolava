from typing import TypeVar

from .base_client import BaseClient
from .endpoints import wallet as endpoints
from .types.base import LavaType

_LTT = TypeVar("_LTT", bound=LavaType)


class LavaWalletClient(BaseClient):
    def __init__(self,
                 jwt_token: str,
                 ):

        self.jwt_token = jwt_token

    def _prepare_request(self, payload: dict, headers: dict) -> tuple[dict, dict]:
        headers.update({"Authorization": self.jwt_token})

        return payload, headers

    async def ping(
            self
    ) -> endpoints.Ping.__returns__:

        request = endpoints.Ping()

        return await self._execute_request(request)

    async def wallet_list(
            self
    ) -> endpoints.WalletList.__returns__:

        request = endpoints.WalletList()

        return await self._execute_request(request)

    async def invoice_info(
            self,
            id_: str = None,
            order_id: str = None,
    ):

        request = endpoints.InvoiceInfo(
            id=id_,
            order_id=order_id,
        )

        return await self._execute_request(request)

    async def create_invoice(
            self,
            wallet_to: str,
            sum_: float,
            order_id: str = None,
            hook_url: str = None,
            success_url: str = None,
            fail_url: str = None,
            expire: int = None,
            subtract: str = None,
            custom_fields: str = None,
            comment: str = None,
            merchant_id: str = None,
            merchant_name: str = None,
    ):

        request = endpoints.CreateInvoice(
            wallet_to=wallet_to,
            sum=sum_,
            order_id=order_id,
            hook_url=hook_url,
            success_url=success_url,
            fail_url=fail_url,
            expire=expire,
            subtract=subtract,
            custom_fields=custom_fields,
            comment=comment,
            merchant_id=merchant_id,
            merchant_name=merchant_name,
        )

        return await self._execute_request(request)


__all__ = [
    "LavaWalletClient"
]
