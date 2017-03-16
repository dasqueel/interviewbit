'''x = []
a = 4
n = 2*a-1
mid = a-1
for i in range(0,n):
	for j in range(0,n):
		x.append([i,j])

final = []

for c in x:
	num = max(abs(c[0]-mid),abs(c[1]-mid)) + 1
	final.append(num)

answer = [final[i:i+n] for i in range(0, len(final), n)]'''


'''for line in answer:
	string = ''
	for num in line:
		string = string +' '+str(num)
	print string.strip()'''

def foo():
	for i in range(1,10):
		x = i
		if i == 4:
			print 4
			break
		print x

foo()