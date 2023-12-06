from datetime import datetime

from aiolava.types.base import LavaType


class InvoiceInInfo(LavaType):
    id: str
    order_id: str
    expire: datetime
    sum: float
    comment: str
    status: str
    success_url: str
    fail_url: str
    hook_url: str
    custom_fields: str


class InvoiceInfoResponse(LavaType):
    status: str
    invoice: InvoiceInInfo
