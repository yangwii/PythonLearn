#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'yangpengjs'

import xlrd
import time

bl_type = ['rule_cust_id', 'rule_mobile_phone', 'rule_email']
def drawdata(filename, col, type):
	data = xlrd.open_workbook(filename)
	table = data.sheets()[0]
	nrows = table.nrows
	ncols = table.ncols

	data = set([])
	for i in xrange(nrows):
		colstr = str(table.row(i)[col].value)
		if colstr.endswith('.0'):
			data.add(colstr.replace('.0', ''))
		else:
			data.add(colstr)			

	today = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
	csvfilename = today + '.csv'
	print csvfilename
	with open(csvfilename, 'w') as csvfile:
		for item_id in data:
			csvfile.write('{} {} {}\n'.format(item_id, bl_type[type], 2))
	print u'生成csv文件完毕'

	sqlfilename = today + '_sql' + '.csv'
	sql = 'select count(*)  from antifraud_bl_pullblack_tag where item_id in ( '
	with open(sqlfilename, 'w') as sqlfile:
		item = ''
		for item_id in data:
			item = item + '\'' + item_id + '\','
		sql = sql + item[:-1] + ' )'
		sqlfile.write(sql)

if __name__ == '__main__':
	import sys
	print 'input filename col_number bltype'
	filename = sys.argv[1] 
	col = int(sys.argv[2])
	bltp = int(sys.argv[3])
	drawdata(filename, col, bltp)

