"""
  Antpool
  @ 2022/10              By Jordi Pascual
"""

__version__ = '0.0.1'
__author__ = 'Jordi Pascual'

import hashlib
import hmac
import requests
import time


class AntPool:
    """Allows users to access and control their accounts using custom written software.
    Do not make more than 600 request per 10 minutes, or we will ban your IP address.
    To get an API key, go to "API". Set permissions and click "Generate key". https://www.antpool.com/userApi

       Attributes:
           user_id (str): [Name account or Sub-account]
           key (str): [API key]
           secret (str): [API secret]
       """

    def __init__(self, ant_pool_user_id: str, ant_pool_key: str, ant_pool_secret: str,
                 url_base: str = 'https://antpool.com/api/') -> None:
        self.user_id = ant_pool_user_id
        self.key = ant_pool_key
        self.secret = ant_pool_secret
        self.url_base = url_base

    def get_signature(self):
        """
        Signature is a HMAC-SHA256 encoded message containing: nonce, client ID and API key.
        The HMAC-SHA256 code must be generated using a secret key that was generated with your API key.
        This code must be converted to its hexadecimal representation (64 uppercase characters).
        """
        nonce = int(time.time() * 1000)
        msgs = self.user_id + self.key + str(nonce)
        ret = [
            hmac.new(self.secret.encode(encoding="utf-8"),
                     msg=msgs.encode(encoding="utf-8"),
                     digestmod=hashlib.sha256).hexdigest().upper(),
            nonce
        ]
        return ret

    def get_hash_user_rate(self, coin: str = 'BTC') -> str:
        """
        Hash Rate

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC).

        Returns:
           Returns overall hash rate in MH/s, total accepted and rejected diff one shares
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin
        }
        request = requests.post(self.url_base + 'hashrate.htm', data=post_data)
        return request.text

    def get_sub_account_list(self, email: str, coin: str = 'BTC') -> str:
        """
        Subaccount List

        Args:
            email: Account email.
            coin: BTC, LTC, ETH, ZEC (default BTC).

        Returns:
           Returns sub-account List
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin_type': coin,
            'email': email,
        }
        request = requests.post(self.url_base + 'subAccount.htm', data=post_data)
        return request.text

    def get_worker_list(self, coin: str = 'BTC', worker_status: int = 0, page: int = 1, page_size: int = 10) -> str:
        """
        Worker List

        Args:
           coin: BTC, LTC, ETH, ZEC (default BTC).
           worker_status: Worker Status(0 All, 1 online, 2 offline, 3 invalid).
           page: goto page number and default is 1.
           page_size: the number of records per page and default is 10.

        Returns:
           Returns overview
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coinType': coin,
            'userId': self.user_id,
            'workerStatus': worker_status,
            'page': page,
            'pageSize': page_size,
        }
        request = requests.post(self.url_base + 'userWorkerList.htm', data=post_data)
        return request.text

    def get_overview(self, coin: str = 'BTC') -> str:
        """
        Overview for subaccount

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC).

        Returns:
           Returns overview
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin,
            'userId': self.user_id
        }
        request = requests.post(self.url_base + 'accountOverview.htm', data=post_data)
        return request.text

    def get_account(self, coin: str = 'BTC') -> str:
        """
        Account balance

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC)

        Returns:
           Returns user account balance in BTC
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin,
            'userId': self.user_id
        }
        request = requests.post(self.url_base + 'account.htm', data=post_data)
        return request.text

    def get_pool_stats(self, coin: str = 'BTC') -> str:
        """
        Pool Stats

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC)

        Returns:
          Return pool statistics information
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin
        }
        request = requests.post(self.url_base + 'poolStats.htm', data=post_data)
        return request.text

    def get_overview_list_by_email(self, email: str, coin: str = 'BTC', page_enable: int = 1, page: int = 1,
                                   page_size: int = 10) -> str:
        """
        Overview for subaccount according to the mailbox

        Args:
            email: Account email.
            coin: BTC, LTC, ETH, ZEC (default BTC)
            page_enable: page enable and default is enable, 0:disable; 1:enable.
            page: goto page number and default is 1.
            page_size: the number of records per page and default is 10.

        Returns:
           Returns overview list by email
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin_type': coin,
            'email': email,
            'pageEnable': page_enable,
            'page': page,
            'pageSize': page_size
        }
        request = requests.post(self.url_base + 'accountOverviewListByEmail.htm', data=post_data)
        return request.text

    def get_workers(self, coin: str = 'BTC', page_enable: int = 1, page: int = 1, page_size: int = 10) -> str:
        """
        Workers' Hash Rate

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC)
            page_enable: page enable and default is enable, 0:disable; 1:enable.
            page: goto page number and default is 1.
            page_size: the number of records per page and default is 10.

        Returns:
            Returns workers' hash rate in MH/s, total accepted and rejected diff one shares.
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin,
            'clientUserId': self.user_id,
            'pageEnable': page_enable,
            'page': page,
            'pageSize': page_size
        }
        request = requests.post(self.url_base + 'workers.htm', data=post_data)
        return request.text

    def get_user_hash_rate_chart(self, worker_id: str, date: str, coin: str = 'BTC', type_r: int = 3) -> str:
        """
        When the userWorkerId query parameter is not void, it means to query the hashrate curve of a certain miner;
        when it is empty, it means to query the hashrate of the current subaccount.
        Date indicates the start time, you can specify to start the query from a certain date, and it can be void;
        when it is empty, it means that the default start date is used for the query

        Args:
            coin: BTC, LTC, ETH, ZEC (default BTC)
            worker_id: Worker Id
            date: (yyyy-MM-dd HH:mm:ss).
            type_r: 1 stands for minutes hashrate chart, 2 stands for hourly hashrate, 3 stands for daily hashrate.

        Returns:
           Returns Timestamp and Hashrate Value
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coinType': coin,
            'userId': self.user_id,
            'userWorkerId': worker_id,
            'date': date,
            'type': type_r
        }
        request = requests.post(self.url_base + 'userHashrateChart.htm', data=post_data)
        return request.text

    def get_payment_history(self, coin: str = 'BTC', page_enable: int = 1, type_p: str = 'payout', page: int = 1,
                            page_size: int = 10) -> str:
        """
        Payment History Summary
        If the number of data query results is less than pageSize, the parameter page of the returned result will be 1,
        and the page of the returned result has nothing to do with the page of the passed parameter.
        For example: there are a total of 10 pieces of data, when the incoming parameter pageSize is 20 and page is 2;
        the return parameter pageSize is 20 and page is 1.

        Args:
           coin:  BTC, LTC, ETH, ZEC (default BTC).
           page_enable: page enable and default is enable, 0:disable; 1:enable.
           type_p:  payment history type and default is payout, payout: payout history; recv: Earnings history.
           page: goto page number and default is 1.
           page_size: the number of records per page and default is 10.

        Returns:
           If type is payout, return to the user's payout history.
           If type is recv, return to the user's earnings history.
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin,
            'pageEnable': page_enable,
            'type': type_p,
            'page': page,
            'pageSize': page_size
        }
        request = requests.post(self.url_base + 'paymentHistoryV2.htm', data=post_data)
        return request.text

    def get_coin_calculator(self, hash_input: str, coin: str = 'BTC') -> str:
        """
        Mining Calculator.

        Args:
            coin:  BTC, LTC, ETH, ZEC (default BTC).
            hash_input: Input Hashrate, 1000000000000 indicates 1TH/s.

        Returns:
            Daily Earnings
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coinType': coin,
            'hashInput': hash_input,
        }
        request = requests.post(self.url_base + 'coinCalculator.htm', data=post_data)
        return request.text

    def change_coin(self, coin: str) -> str:
        """
        Change coin.

        Args:
            coin:  BTC, LTC, ETH, ZEC (default BTC).

        Returns:
            Returns result ok or error
        """
        api_sign = self.get_signature()
        post_data = {
            'key': self.key,
            'nonce': api_sign[1],
            'signature': api_sign[0],
            'coin': coin,
        }
        request = requests.post(self.url_base + 'changeMiningCoin.htm', data=post_data)
        return request.text
