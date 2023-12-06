from datetime import datetime

from aiolava.types.base import LavaType


class CreateInvoiceResponse(LavaType):
    status: str
    id: str
    url: str
    expire: datetime
    sum: float
    success_url: str
    fail_url: str
    hook_url: str
    custom_fields: str
    merchant_name: str
    merchant_id: str
