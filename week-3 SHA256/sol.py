import os
from Crypto.Hash import SHA256
import hashlib

'''
h = SHA256.new()
f = open('6 - 2 - Generic birthday attack (16 min).mp4','r')
filesize = os.path.getsize('6 - 2 - Generic birthday attack (16 min).mp4') 
location = filesize - (filesize % 1024)
f.seek(location,0)
#print f.tell()

#print h.hexdigest()
h.update(f.read())

while location > 0:
	location = location - 1024
#	print lengthcovered
	f.seek(location, 0)
#	print f.tell()
	h.update(f.read(1024) + h.digest())
#h.update(h.hexdigest())
#print len(f.read(1024)+h.digest())
print h.hexdigest()
'''

data = list()
i = 0
fp = open('6 - 1 - Introduction (11 min).mp4','rb')
while True:
	chunk = fp.read(1024)
	if chunk == '':
		break
	data.insert(i,chunk)
	i = i + 1

digest = hashlib.sha256(data[len(data)-1]).digest()
#h.update(data[len(data)-1])
i = len(data) - 2
while i >= 0:
	#h.update(data[i] + h.digest())
	digest = hashlib.sha256(data[i]+digest).digest()
	i = i-1
print digest.encode('hex')
