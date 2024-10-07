from typing import List
from datetime import datetime
from pydantic import RootModel

from aiolava.types.base import LavaType


class Wallet(LavaType):
    account: str
    currency: str
    balance: float


class WalletListResponse(RootModel[List[Wallet]]):
    pass