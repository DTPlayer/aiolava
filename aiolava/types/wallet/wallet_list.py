from typing import List
from datetime import datetime

from aiolava.types.base import LavaType, RootMixin


class Wallet(LavaType):
    account: str
    currency: str
    balance: float


class WalletListResponse(LavaType, RootMixin[Wallet]):
    __root__: List[Wallet]
