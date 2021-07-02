import os

from TadoToolkit.tado import Tado

""" Setting the environ in powershell:
$env:TADO_PASS = "<pass>"
$env:TADO_EMAIL = "<email>"

Used for quick testing of the class
"""

tado_pass = os.environ['TADO_PASS']
tado_email = os.environ['TADO_EMAIL']

# tado_email = "blah@blah.com"
# tado_pass = "blahblah"

t = Tado(tado_email, tado_pass)

print(t.get_bearer_token())
