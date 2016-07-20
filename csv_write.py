# _*_ coding:utf-8 _*_ 

import csv

data = [
  ( '0011' , 'http://www.59store.com/' , '59store.com' ),
  ( '0022' , 'http://59data.top/' , '59data.top' ),
  ( '0033' , 'http://my.space.zmx/' , 'ùh◊”Åy¥a£ø' )
]

with open('csvtest.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, dialect='excel')
	writer.writerow(['id', 'url', 'keywords'])
	writer.writerows(data)