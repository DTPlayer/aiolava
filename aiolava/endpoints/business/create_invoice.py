from typing import Union, List, Optional

from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint

from aiolava.types.business.create_invoice import CreateInvoiceResponse


class CreateInvoice(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/business/invoice/create"
    __returns__ = CreateInvoiceResponse

    sum: Union[float, int]
    orderId: Union[str, int]
    shopId: str
    hookUrl: Optional[str] = None
    failUrl: Optional[str] = None
    successUrl: Optional[str] = None
    expire: Optional[int] = None
    customFields: Optional[str] = None
    comment: Optional[str] = None
    includeService: Optional[List[str]] = None
    excludeService: Optional[List[str]] = None
