#!/usr/bin/env python3
to_str = __import__('3-to_str').to_str

print(to_str(3.14) == "{}".format(str(3.14)))
print(to_str.__annotations__)