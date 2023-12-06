# Async Lava API library

### Example to use

```python
import asyncio

from aiolava import BusinessClient


async def main():
    client = BusinessClient(
        private_key="INSERT_PRIVATE_KEY",
        mics_key="INSERT_MICS_KEY",
        shop_id="INSERT_SHOP_ID"  # optional
    )
    
    invoice = await client.create_invoice(
        sum_=10,
        order_id="order#10"
    )
    print(invoice.data.url)
    
    status = await client.check_invoice_status(
        order_id="order#10"
    )
    print(status.data.status)


if __name__ == '__main__':
    asyncio.run(main())

```