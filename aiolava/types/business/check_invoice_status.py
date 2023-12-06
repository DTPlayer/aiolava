from typing import List
from datetime import datetime

from aiolava.types.base import LavaType


class InvoiceStatus(LavaType):
    status: str
    error_message: str = None
    id: str
    shop_id: str
    amount: float
    expire: datetime
    order_id: str
    fail_url: str = None
    success_url: str = None
    hook_url: str = None
    custom_fields: List[str] = None
    include_service: List[str] = None


class CheckInvoiceStatusResponse(LavaType):
    data: InvoiceStatus
    status: int
    status_check: bool
