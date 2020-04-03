"""
Stark
-----


stark generates random and strong passwords

the password can include the following characters

lowercase
uppercase
digits
letters
alphanumeric
hexdigits
symbols

stark provides two feautures:

CLI
---
    you can generate passwords on the fly from the command line

API
---
    you can import stark in another module and generate passwords

"""

from .app import generate
