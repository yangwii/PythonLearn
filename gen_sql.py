import os

def gene_sql(filename):
	sqlfilename = 'f' + filename
	reader = open(filename, 'r')
	data = reader.readlines()
	with open(sqlfilename, 'w') as sqlfile:
		item = ''
		for item_id in data:
			item = item_id + item
		sqlfile.write(item.rstrip(','))

	reader.close()


if __name__ == '__main__':
	import sys
	filename = sys.argv[1]
	gene_sql(filename)