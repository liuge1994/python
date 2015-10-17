f = open('/home/liuge/python/test.txt','r')

f.read()

f.close()

try: 
    f = open('/home/liuge/python/test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('/home/liuge/python/test.txt', 'r') as f:
    print f.read()

f = open('/home/liuge/python/test.txt', 'rb') 
f.read()

f = open('/home/liuge/python/test.txt', 'rb')
u = f.read().decode('gbk')

import codecs

with codecs.open('/home/liuge/python/test.txt', 'r', 'gbk') as f:
    f.read()

f = open('/home/liuge/python/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/home/liuge/python/test.txt', 'w') as f:
    f.write('Hello, world!')

with codecs.open('/home/liuge/python/test.txt', 'w', 'gbk') as f:
    f.write('Hello, world!')
