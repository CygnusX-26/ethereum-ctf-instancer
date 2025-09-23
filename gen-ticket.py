import hashlib,random
print("Generating your ticket. This may take a few minutes.")
x = 100000000+random.randint(0,200000000000)
for i in range(x,x+20000000000):
	m = hashlib.sha256()
	ticket = str(i)
	m.update(ticket.encode('ascii'))
	digest1 = m.digest()
	m = hashlib.sha256()
	m.update(digest1 + ticket.encode('ascii'))
	if m.hexdigest().startswith('0000000'):
		print(i)
		break
print("You can reuse this ticket the next time you need an instance.")
