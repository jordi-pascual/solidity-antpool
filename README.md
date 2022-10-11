# Solidity ANTPOOL

This API is based on the documentation provided by ANTPOOL (https://www.antpool.com/userApiGuide).

ANTPOOL's application programming interface (API) allows users to access and control their accounts using custom written software.

## Request limits
Do not make more than 600 request per 10 minutes or we will ban your IP address.

## API authentication

You need to provide 3 parameters to authenticate a request:

- key - API key
- secret - API secret
- user_id - Id Antpool

![antpool_info_credentials](https://user-images.githubusercontent.com/7261873/194952942-eef3c399-80f1-4d12-97b1-d0bc26743b17.jpg)

## Install

    pip3 install solidity-antpool

## Use Case
```python
from AntPool import antpool

user_id = '#####'
key = '#########'
secret = '######'

def example():
    if __name__ == '__main__':
        data = antpool.AntPool(user_id, key, secret)
        print(data.get_overview())


if __name__ == '__main__':
    example()
```
### Response 
```json
{
    "code": 0,
    "message": "ok",
    "data":
    {
        "hsLast10m": "127603936523714",
        "hsLast1d": "102498704834436",
        "invalidWorkerNum": 0,
        "totalAmount": "0.00480411",
        "totalWorkerNum": 1,
        "unpaidAmount": "0.00480411",
        "yesterdayAmount": "0.00037884",
        "inactiveWorkerNum": 0,
        "hsLast1h": "114466490529000",
        "userId": "#####",
        "activeWorkerNum": 1
    }
}
```


## Methods
- get_hash_user_rate (Hash Rate)
- get_sub_account_list (Sub-account List)
- get_workers (Workers' Hash Rate)
- get_worker_list (Worker List)
- get_account (Account balance)
- get_overview (Overview for sub-account)
- get_overview_list_by_email (Overview for sub-account according to the mailbox)
- get_pool_stats (Pool Stats)
- get_overview_list_by_email (Overview for subaccount according to the mailbox)
- get_user_hash_rate_chart (When the userWorkerId query parameter is not void)
- get_payment_history (Payment History Summary)

- get_coin_calculator (Mining Calculator)
- change_coin (Change coin)
- 
## Holla at ya' boy

BTC: 18ViDtX2XXqciFJg8f4B6tf6nWLBTQTS2

ETH: 0xc5D4A8DA3151cd09B25631760da495E7FcaC8b93

