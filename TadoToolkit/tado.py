import requests
from json import dumps, loads
import logging
import time
from email.utils import parseaddr

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Tado(object):

    def __init__(self, email, password):
        """Initialization of the Tado class

        The tokens and home id is set, so I can allow other functions to check
        whether they have been initialized, and do their own tests beforehand

        Arguments:
            email {str} -- Email address of account
            password {str} -- Password of email address of account
        """

        if parseaddr(email) == ('', ''):
            raise Exception(f'Invalid Email address ({email})')
        if len(password) <= 4:
            raise Exception(f'The password was too short ({password}')
        self.clientSecret = 'wZaRN7rpjn3FoNyF5IFuxg9uMzYJcvOoQ8QWiIqS3hfk6gLhVlG57j5YNoZL2Rtc'
        self.email = email
        self.password = password
        self.access_token = ""
        self.refresh_token = ""
        self.home_id = ""
        self.token_duration = 600

    def get_bearer_token(self):
        """Responsible for getting the initial bearer token

        Returns:
            int -- returns the status code, 200 for OK
        """
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

        self.token_valid_to = time.time() + self.token_duration

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        r = loads(response.content)

        self.access_token = r['access_token']
        self.refresh_token = r['refresh_token']

        return response.status_code

    def refresh_bearer_token(self):
        """Responsible for refreshing the bearer token

        Returns:
            int -- returns https status code, 200 for OK
        """
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

        self.token_valid_to = time.time() + self.token_duration

        r = loads(response.content)

        self.refresh_token = r['refresh_token']
        return response.status_code

    def get_home_id(self):
        """Responsible for getting the homeId for later use. 

        If bearer token is not set, it will call get_bearer_token

        Returns:
            int -- Returns the HTTP status code
        """
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
        return response.status_code

    def get_home_details(self):
        """Gets home details from API

        Returns:
            int -- Returns the HTTP status code
        """
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

        self.home_details = r
        return response.status_code

    def get_presence(self):
        """Gets presence from the geo fencing functionality

        Returns:
            int -- Returns the HTTP status code
        """
        if self.home_id == "":
            self.get_home_id()

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        response = requests.get(
            f'https://my.tado.com/api/v2/homes/{self.home_id}/state', headers=headers)

        logging.debug(
            f'The response was {response.status_code} and the content was {response.content}')

        r = loads(response.content)

        self.presence = r["presence"]
        return response.status_code
