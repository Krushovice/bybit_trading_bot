import logging
from pybit import exceptions
from pybit.unified_trading import HTTP


logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)


def main():
    client = HTTP(
        testnet=True,
        recv_window=60000,
        max_retries=3,
    )
    try:
        response = client.get_orderbook(category="linear", symbol="BTCUSDT")
        print(response)
    except exceptions.InvalidRequestError as e:
        print(f"Ошибка запроса: {e.status_code}| {e.message}")


if __name__ == "__main__":
    main()
