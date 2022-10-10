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

- ![antpool_info_credentials](https://user-images.githubusercontent.com/7261873/194952942-eef3c399-80f1-4d12-97b1-d0bc26743b17.jpg)


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

