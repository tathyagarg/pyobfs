"""
print.py
~~~~~~~~

This module contains the print function.
`print` can be accessed through `__builtins__.__getattribute__("print")`.
So, our task is really to obfuscate `"print"` in the code.

We'll do this by obfuscating `''.join("print")`
Which is `str().join("print")`
=> `str().join(["p", "r", "i", "n", "t"])`
=> `str().join([chr(112), chr(114), chr(105), chr(110), chr(116)])`
=> `str().join(map(chr, [112, 114, 105, 110, 116]))`
=> `str().join(map(chr, [0x70, 0x72, 0x69, 0x6e, 0x74]))`

Let a = 0x6e (110)
=> `str().join(map(chr, [a + 2, a + 4, a - 5, a, a + 6]))`

Thus, we require `str`, `join`, `map`, `chr`, `a`, `+`, `-`, `2`, `4`, `5`, `6` in the code.
`+` and `-` can be substitude to the `__add__` and `__sub__` methods respectively.

=> `str().join(map(chr, [a.__add__(2), a.__add__(4), a.__sub__(5), a, a.__add__(6)]))`
"""


PRINT = "print"
