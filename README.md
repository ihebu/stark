# Stark

[![MIT License](https://img.shields.io/github/license/iheb-haboubi/stark?color=blue)](https://github.com/Iheb-Haboubi/stark/blob/master/LICENSE)
[![PyPi Version](https://img.shields.io/pypi/v/stark.svg)](https://pypi.org/project/stark/)
[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/stark)](https://pypi.org/project/stark)

Stark is a python tool that generates random and strong passwords.

The password can include the following characters

```
lowercase       abcdefghijklmnopqrstuvwxyz
uppercase       ABCDEFGHIJKLMNOPQRSTUVWXYZ
digits          0123456789
letters         abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
alphanumeric    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
hexdigits       0123456789abcdefABCDEF
symbols         !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## Installation

```
pip install stark
```

## Usage

### From python

```python
from stark import generate

length = 30
types = {'lowercase':15,'digits':10,'symbols':True}
password = generate(length=length,types=types)
# The remaining number of characters is 30 - 15 - 10 = 5
# Thus, the number of symbols in the password will be remainder = 5

length = 30
types = {'lowercase':15,'digits':True,'symbols':True}
password = generate(length=length,types=types)
# The remaining number of characters is 30 - 15 = 15
# Thus, the number of digits and symbols in the password will be a random partition of remainder = 15
# e.g (7,8) or (10,5) or (9,6) etc ...
# the partition will not contain a value of 0
# i.e the occurance of each type in the password will be greater than or equal 1

length = None
types = {'lowercase':15,'uppercase':5,'digits':7}
password = generate(length=length,types=types)
# If length is None, the password length will be the sum of the values of types.
# Thus, it's not allowed to have one value equals True while password length is None.
```

### From CLI

```
$ stark [options]
```

Get help about options

```
$ stark --help

stark generates random and strong passwords

optional arguments:
  -h, --help           show this help message and exit
  -ln, --length        password length
  -a, --any            include any character
  -l, --lowercase      include lowercase
  -u, --uppercase      include uppercase
  -d, --digits         include digits
  -s, --symbols        include symbols
  -x, --hexdigits      include hexadecimal
  -an, --alphanumeric  include alphanumeric
  -lt, --letters       include letters
```

### Examples

Default password : 25 character alphanumeric

```
$ stark

Ezvx2gwGVvylnNkueHtoLwg77
```

<br>

custom length

```
$ stark -ln 50

0alR2vsoy2FsdqALF7oQhzG0GPicS1qitm69u7Yu6Fhq9mcu2Z
```

<br>

30 character password, include 15 lowercase, 7 digits and the rest will be symbols

```
$ stark -ln 30 -l 15 -d 7 -s

7\1z]9%g#4r}kk'zn0da]w~1uy9myb
```

<br>

30 character password, include 10 hexdigits an the rest will be uppercase and symbols

```
$ stark -ln 30 -x 10 -u -s

N{92D=NB{8FV"D1B\?OI!)BK6$KB3I
```

## Testing

```
$ pip install pytest

$ pytest
```

## Contributing

Anyone is welcome and encouraged to contribute, especially the beginners as this is a beginner friendly project.

Contributing can include, but is not limited to :

- Adding / Improving documentation
- Adding / Improving tests
- Reporting bugs and errors
- Adding new feautures and code
- Sharing this project with anyone who might be interested
