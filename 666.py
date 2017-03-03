#!/usr/bin/env python3
# -- coding: utf-8 --
LOG = '-->hello Log: '
import statistics
import utils_file
import utils

list = utils_file.getListfromFile()
sum_avg_list = []
listLenth = len(list)

sum_count_list = []
print(LOG,listLenth)

# process list
for i in range(3):
	sum_count_list.append(utils.getSumCountGroubyItem(i,list)[1])
	print('MIAOMIAOMIAO',sum_count_list)
print(LOG,'sum_count_list:',sum_count_list)

for item in sum_count_list:
	tmp_sum_avg = []
	print(LOG,'item:',item)
	for element in item:
		tmp_sum_avg.append(element*100 / listLenth)
	print(LOG,'tmp_sum_avg:',tmp_sum_avg)
	sum_avg_list.append(tmp_sum_avg)

print(LOG,'sum_avg_list:',sum_avg_list)

print('--1--','--2--','--3--','--4--','--5--','--6--')
for r in sum_avg_list:
	for i in r:
		print('{0:.2f}'.format(i).rjust(5),end=' ')
	print()
	#print('%.2f' % r[0],'%.2f' % r[1],'%.2f' % r[2],'%.2f' % r[3],'%.2f' % r[4],'%.2f' % r[5])
	#print('{0:.2f} {1:.2f} {2:.2f} {3:.2f} {4:.2f} {5:.2f}'.format(r[0],r[1],r[2],r[3],r[4],r[5]))
	
	
sum_comlumn = [0, 0, 0, 0, 0, 0]
for r in sum_avg_list:
	for i in range(6):
		sum_comlumn[i] +=r[i]
print('-----------------------------------')
for i in sum_comlumn:
	print('{0:.2f}'.format(i).rjust(5),end=' ')