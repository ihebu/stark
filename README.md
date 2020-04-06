# Stark

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/07c251e92b634c2895ea9dc2ad77001d)](https://app.codacy.com/manual/Iheb-Haboubi/stark?utm_source=github.com&utm_medium=referral&utm_content=Iheb-Haboubi/stark&utm_campaign=Badge_Grade_Dashboard)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui?color=blue)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![PyPi Version](https://img.shields.io/pypi/v/stark.svg)](https://pypi.org/project/stark/)
[![PyPi Python Versions](https://img.shields.io/badge/python-3.6%7C%203.7%20%7C%203.8-blue)](https://pypi.org/project/stark)

stark generates random and strong passwords.

## Installation

```bash
pip install stark
```

## Usage

### API

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

#### Notes

A value of True in types dictionary indicates that the character
will have a number of one or more (randomly) in the password.

If length is None, the password length
will be the sum of the values of types.

Thus, it's not allowed to have one value equals True
while length is None.

### CLI

```
$ stark [options]
```

Get help about options

```
$ stark --help

usage: stark [options]

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

default password : 25 character alphanumeric

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

### License

MIT License

Copyright (c) 2020 Iheb Haboubi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
