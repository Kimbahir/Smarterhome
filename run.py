import os

from TadoToolkit.tado import Tado

""" Setting the environ in powershell:
$env:TADO_PASS = "<pass>"
$env:TADO_EMAIL = "<email>"
"""

tado_pass = os.environ['TADO_PASS']
tado_email = os.environ['TADO_EMAIL']

t = Tado(tado_email, tado_pass)

print(t.get_bearer_token())
