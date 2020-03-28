import requests
from json import dumps, loads
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Tado(object):

    def __init__(self, email, password):
        """Initialization of the Tado class

        Arguments:
            email {str} -- Email address of account
            password {str} -- Password of email address of account
        """
        self.clientSecret = 'wZaRN7rpjn3FoNyF5IFuxg9uMzYJcvOoQ8QWiIqS3hfk6gLhVlG57j5YNoZL2Rtc'
        self.email = email
        self.password = password
        self.access_token = ""
        self.home_id = ""

    def get_bearer_token(self):
        data = {
            'client_id': 'tado-web-app',
            'grant_type': 'password',
            'scope': 'home.user',
            'username': self.email,
            'password': self.password,
            'client_secret': self.clientSecret
        }

        logging.debug(f'Data is {data}')

        response = requests.post(
            'https://auth.tado.com/oauth/token', data=data)

        self.token_valid_to = time.time() + 600

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        r = loads(response.content)

        self.access_token = r['access_token']
        self.refresh_token = r['refresh_token']

    def refresh_bearer_token(self):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token,
            'client_id': 'tado-web-app',
            'scope': 'home.user',
            'client_secret': self.clientSecret
        }

        response = requests.post(
            'https://auth.tado.com/oauth/token', data=data)

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        self.token_valid_to = time.time() + 600

        r = loads(response.content)

        self.refresh_token = r['refresh_token']

    def get_home_id(self):
        if self.access_token == "":
            self.get_bearer_token()

        headers = {
            'Authorization': f'Bearer  {self.access_token}'
        }

        response = requests.get(
            'https://my.tado.com/api/v1/me', headers=headers)

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        r = loads(response.content)

        self.home_id = r['homeId']

    def get_home_details(self):
        if self.home_id == "":
            self.get_home_id()

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        response = requests.get(
            f'https://my.tado.com/api/v2/homes/{self.home_id}', headers=headers)

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        r = loads(response.content)
