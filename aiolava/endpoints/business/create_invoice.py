from typing import Union, List

from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint

from aiolava.types.business.create_invoice import CreateInvoiceResponse


class CreateInvoice(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/business/invoice/create"
    __returns__ = CreateInvoiceResponse

    sum: float
    orderId: Union[str, int]
    shopId: str
    hookUrl: str = None
    failUrl: str = None
    successUrl: str = None
    expire: int = None
    customFields: str = None
    comment: str = None
    includeService: List[str] = None
    excludeService: List[str] = None
