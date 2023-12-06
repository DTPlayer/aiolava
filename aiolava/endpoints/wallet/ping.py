from aiolava.endpoints.base import LavaEndpoint
from aiolava.misc import HTTPMethod

from aiolava.types.wallet.ping import PingResponse


class Ping(LavaEndpoint):
    __http_method__ = HTTPMethod.GET
    __endpoint__ = "/test/ping"
    __returns__ = PingResponse
