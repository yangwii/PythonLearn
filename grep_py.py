import os
import glob

def search(root, key, ftype='', logname=None):
	ftype = '*.' + ftype if ftype else '*'
	logname = logname or os.devnull
	symbol = os.path.join(root, ftype)
	fnames = glob.glob(symbol)
	vc = len(fnames)
	fc = 0
	
	with open(logname, 'wb') as writer:
		for fname in fnames:
			found = False
			with open(fname) as reader:
				for idx, line in enumerate(reader):
					line = line.strip()
					if key in line.split():
						line = line.replace(key, '**' + key + '**')
						found = True
						writer.write('{}---{}:{}\n'.format(fname, idx + 1, line))
			if found:
				fc = fc + 1
				print '{} has {}'.format(fname, key)
	
	return vc, fc

if __name__ == '__main__':
	search('.', 'import', 'py', 'res')
				