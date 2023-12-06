from typing import List
from datetime import datetime

from aiolava.types.base import LavaType


class CreatedInvoice(LavaType):
    id: str
    amount: float
    expired: datetime
    status: int
    shop_id: str
    url: str
    comment: str = None
    fail_url: str = None
    success_url: str = None
    hook_url: str = None
    custom_fields: str = None
    merchantName: str = None
    exclude_service: List[str] = None
    include_service: List[str] = None


class CreateInvoiceResponse(LavaType):
    data: CreatedInvoice
    status: int
    status_check: bool
