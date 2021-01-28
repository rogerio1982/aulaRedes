import hashlib
from typing import Text
text = input("entre com o senha: ")
h = hashlib.sha256(text.encode("ascii"))
print (h.hexdigest())
