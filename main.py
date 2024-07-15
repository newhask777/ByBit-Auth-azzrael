import os

from pybit import exceptions
from pybit.unified_trading import HTTP
from config import demo_api_key, demo_secret_key, api_key, secret_key


def main():

    cl = HTTP(
        demo = False,
        api_key = api_key,
        api_secret = secret_key,
        recv_window = 60000,
        return_response_headers = True
    )

    try:
        r = cl.get_executions(category="linear", limit=10)
        print(r)
    
    except exceptions.InvalidRequestError as e:
        print("Bybit Request Error", e.status_code, e.message, sep=' | ')
    except exceptions.FailedRequestError as e:
        print("Bybit Request Failed", e.status_code, e.message, sep=' | ')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print('Hola, AzzraelCode YT Subs!')
    main()