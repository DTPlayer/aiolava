from pydantic.v1 import root_validator

from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint

from aiolava.types.business.check_invoice_status import CheckInvoiceStatusResponse


class CheckInvoiceStatus(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/business/invoice/status"
    __returns__ = CheckInvoiceStatusResponse

    shopId: str
    orderId: str = None
    invoiceId: str = None

    @root_validator()
    def check_invoice_identify_possibility(cls, values):
        if values.get("orderId") is None and values.get("invoiceId") is None:
            raise ValueError("invoice can't be identified, nether of `orderId` nor `invoiceId` are specified")

        return values
