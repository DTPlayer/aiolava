from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint

from aiolava.types.wallet.create_invoice import CreateInvoiceResponse


class CreateInvoice(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/invoice/create"
    __returns__ = CreateInvoiceResponse

    wallet_to: str
    sum: float
    order_id: str = None
    hook_url: str = None
    success_url: str = None
    fail_url: str = None
    expire: int = None
    subtract: str = None
    custom_fields: str = None
    comment: str = None
    merchant_id: str = None
    merchant_name: str = None
