import logging
from pybit.unified_trading import HTTP

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)


def main():
    client = HTTP()
    response = client.get_orderbook(category="linear", symbol="BTCUSDT")

    print(response)


if __name__ == "__main__":
    main()
