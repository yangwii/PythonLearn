import os

def write2file(filename, ln, start, end):
	pre = 'f'
	ind = '.csv'
	tofile = pre + str(ln) + ind
	print tofile
	with open(tofile, 'w') as writer:
		with open(filename, 'r') as csvfile:
			for line in csvfile:
				for idx, line in enumerate(csvfile):
					if idx >= start and idx < end:
						writer.write('{}'.format(line))
						
						
	print '{}--{} ok'.format(start, end)
				
def getline(filename):
	line = 0
	reader = open(filename, 'r')
	lines = reader.readlines()
	return len(lines)
		
if __name__ == '__main__':
	print 'start'
	line = getline('bg.csv')
	kn = line % 10000
	kkn = line / 10000
	for i in xrange(kkn):
		write2file('bg.csv', i + 1, i * 10000, i * 10000 + 10000)
	if kn != 0:
		write2file('bg.csv', kkn + 1, 10000 * kkn, 10000 * kkn + kn)