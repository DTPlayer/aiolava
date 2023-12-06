from pydantic.v1 import root_validator

from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint

from aiolava.types.wallet.invoice_info import InvoiceInfoResponse


class InvoiceInfo(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/invoice/info"
    __returns__ = InvoiceInfoResponse

    id: str
    order_id: str

    @root_validator()
    def check_invoice_identify_possibility(cls, values):
        if values.get("id") is None and values.get("order_id") is None:
            raise ValueError("invoice can't be identified, nether of `id` nor `order_id` are specified")

        return values
