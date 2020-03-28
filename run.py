import os

from Tado.tado import Tado

""" Setting the environ in powershell:
$env:TADO_PASS = "<pass>"
$env:TADO_EMAIL = "<email>"
"""

tado_pass = os.environ['TADO_PASS']
tado_email = os.environ['TADO_EMAIL']

t = Tado(tado_email, tado_pass)

# t.get_bearer_token()

t.get_home_details()

#print(f"{tado_email}'s password is '{tado_pass}'")
