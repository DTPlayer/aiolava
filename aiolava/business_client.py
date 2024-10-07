import json
from typing import List, Union, TypeVar, Optional
import hmac
import hashlib

import logging

from aiolava.base_client import BaseClient
from aiolava.endpoints import business as endpoints
from aiolava.types.base import LavaType

import warnings


_LTT = TypeVar("_LTT", bound=LavaType)


class LavaBusinessClient(BaseClient):
    def __init__(self,
                 private_key: str,
                 shop_id: str,
                 ):

        self.private_key = private_key
        self.shop_id = shop_id

    def _prepare_request(self, payload: dict, headers: dict) -> tuple[dict, dict]:
        payload_bytes = json.dumps(payload).encode()
        signature = (
            hmac
            .new(self.private_key.encode('UTF-8'), payload_bytes, hashlib.sha256)
            .hexdigest()
        )
        headers.update({
            'Signature': signature,
        })
        return payload, headers

    async def create_invoice(
            self,
            order_id: Union[str, int],
            amount: Optional[float],
            sum_: Optional[float] = None,
            shop_id: Optional[str] = None,
            hook_url: Optional[str] = None,
            fail_url: Optional[str] = None,
            success_url: Optional[str] = None,
            expire: Optional[int] = None,
            custom_fields: Optional[str] = None,
            comment: Optional[str] = None,
            include_service: Optional[List[str]] = None,
            exclude_service: Optional[List[str]] = None,
    ) -> endpoints.CreateInvoice.__returns__:
        
        if sum_:
            warnings.warn("sum_ is deprecated, use amount instead", DeprecationWarning)
            amount = sum_

        if shop_id:
            warnings.warn("shop_id is not provided, using default", DeprecationWarning)
            self.shop_id = shop_id

        request = endpoints.CreateInvoice(
            sum=amount,
            shopId=self.shop_id,
            orderId=order_id,
            hookUrl=hook_url,
            failUrl=fail_url,
            successUrl=success_url,
            expire=expire,
            customFields=custom_fields,
            comment=comment,
            includeService=include_service,
            excludeService=exclude_service,
        )
        return await self._execute_request(request)

    async def check_invoice_status(
            self,
            order_id: str = None,
            invoice_id: str = None,
            shop_id: str = None,
    ) -> endpoints.CheckInvoiceStatus.__returns__:

        if shop_id is None:
            shop_id = self.shop_id

        request = endpoints.CheckInvoiceStatus(
            shopId=shop_id,
            orderId=order_id,
            invoiceId=invoice_id
        )
        return await self._execute_request(request)


__all__ = [
    "LavaBusinessClient",
]
