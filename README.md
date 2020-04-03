# Stark

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![PyPi Version](https://img.shields.io/pypi/v/stark.svg)](https://pypi.org/project/stark/)

stark generates random and strong passwords.

the password can include the following characters

```
lowercase      abcdefghijklmnopqrstuvwxyz
uppercase      ABCDEFGHIJKLMNOPQRSTUVWXYZ
digits         0123456789
letters        abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
alphanumeric   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
hexdigits      0123456789abcdefABCDEF
symbols        !"#$%&\'()*+,-./:;<=>?@[]^_`{|}~
```

## Requirements

```
python 3.6 or higher
```

## Installation

```
pip install stark
```

## Usage

### API

```python
from stark import generate

length = 30
types = {'lowercase':15,'digits':10,'symbols':True}

password = generate(length=length,types=types)
```

#### Notes

A value of True in types dictionary indicates that the character
will have a number of one or more (randomly) in the password.

If length is None, the password length
will be the sum of the values of types.

Thus, it's not allowed to have one value equals True
while length is None.

#### Examples

```python
length = 30
types = {'lowercase':15,'digits':True,'symbols':True}

password = generate(length=length,types=types)
```

in this example, the number of digits and symbols is not provided so it will be given a random partition such that the sum of the values will be equal to the password length.

the password in this case will contain 15 lowercase and might contain (7 digits and 8 symbols) or (5 digits and 10 symbols) etc...

<br>

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

<br>

### License

```
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
```
