import string

BASE62 = string.digits + string.ascii_letters
BASE = len(BASE62)

def encode(num: int) -> str:
    if num == 0:
        return BASE62[0]
    
    result = []
    while num > 0:
        num, rem = divmod(num, BASE)
        result.append(BASE62[rem])
    
    return "".join(reversed(result))

def decode(short_code: str) -> int:
    num = 0
    for char in short_code:
        num = num * BASE + BASE62.index(char)
    return num
