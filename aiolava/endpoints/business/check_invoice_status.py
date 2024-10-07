from aiolava.misc import HTTPMethod
from aiolava.endpoints.base import LavaEndpoint
from aiolava.types.business.check_invoice_status import CheckInvoiceStatusResponse
from pydantic import model_validator


class CheckInvoiceStatus(LavaEndpoint):
    __http_method__ = HTTPMethod.POST
    __endpoint__ = "/business/invoice/status"
    __returns__ = CheckInvoiceStatusResponse

    shopId: str
    orderId: str = None
    invoiceId: str = None

    @model_validator(mode='before')
    @classmethod
    def check_invoice_identify_possibility(cls, values):
        if values.get("orderId") is None and values.get("invoiceId") is None:
            raise ValueError("invoice can't be identified, nether of `orderId` nor `invoiceId` are specified")

        return values