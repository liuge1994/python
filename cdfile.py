import os

print os.name

print os.uname()
print os.environ
print os.getenv('PATH')
print os.path.abspath('.')
os.path.join('/home/liuge/python', 'testdir')
os.mkdir('/home/liuge/python/testdir')
os.rmdir('/home/liuge/python/testdir')

