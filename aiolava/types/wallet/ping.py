from typing import List
from datetime import datetime

from aiolava.types.base import LavaType


class PingResponse(LavaType):
    status: bool
