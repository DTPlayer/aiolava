import pytest
import os
import uuid

from aiolava.business_client import LavaBusinessClient

env = os.environ


@pytest.mark.asyncio
async def test_create_invoice():
    client = LavaBusinessClient(
        private_key=env.get("LAVA_PRIVATE_KEY"),
        shop_id=env.get("LAVA_SHOP_ID"),
    )

    invoice = await client.create_invoice(
        amount=100,
        order_id=f'{uuid.uuid4()}|aiolava test',
    )
    assert isinstance(invoice, dict)