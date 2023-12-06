from typing import List, Type, Union

from aiolava.endpoints.base import LavaEndpoint
from aiolava.misc import HTTPMethod

from aiolava.types.wallet.wallet_list import WalletListResponse, Wallet


class WalletList(LavaEndpoint):
    __http_method__ = HTTPMethod.GET
    __endpoint__ = "/wallet/list"
    __returns__: Type[Union[List[Wallet], WalletListResponse]] = WalletListResponse
