import os

class Fab_Iter(object):
	def __init__(self, max):
		self.max = max
		self.n, self.a, self.b = 0, 0, 1
		
	def __iter__(self):
		return self
		
	def next(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.b, self.a + self.b
			self.n = self.n + 1
			return r
		raise StopIteration()
	
def fab_yield(max):
		n, a, b = 0, 0, 1
		while n < max:
			yield b
			a, b = b, a + b
			n = n + 1
			
if __name__ == '__main__':
	for n in fab_yield(5):
		print n