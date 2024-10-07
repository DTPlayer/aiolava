# Async Lava API library

## ATTENTION

**Warning:** This development branch is experimental and not recommended for integration into projects.

### Example to use

```python
import asyncio

from aiolava import LavaBusinessClient


async def main():
    client = LavaBusinessClient(
        private_key="INSERT_PRIVATE_KEY",
        shop_id="INSERT_SHOP_ID"
    )
    
    invoice = await client.create_invoice(
        amount=10,
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


## Roadmap
1. [ ] Update Pydantic
2. [ ] Add testing
3. [x] Code optimization
4. [ ] Documentation

### All documentation you can find [here](https://dev.lava.ru/)