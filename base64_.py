import base64

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluzw==')

print base64.b64encode('i\xb7\x1d\xef\xff')

print base64.urlsafe_b64encode('i\xb7\x1d\xef\xff')

print base64.urlsafe_b64decode('abcd--__')

def safe_b64decode(s):
    if len(s) % 4:
        s = s + (4 - len(s) % 4) * '='
    return base64.b64decode(s)

print safe_b64decode('YWJjZA')


