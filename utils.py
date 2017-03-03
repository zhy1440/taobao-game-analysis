#!/usr/bin/env python3
# -- coding: utf-8 --

LOG = '-->utils Log: '
def getSumCountGroubyItem(i,list):
	sum_count = [0, 0, 0, 0, 0, 0]
	tmp = []
	for item in list:
		# process th first element
		sum_count[int(item[i]) - 1] += 1;
		tmp.append(item[i])

	print(LOG,tmp)
	print(LOG,sum_count)
	return tmp,sum_count