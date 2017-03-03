#!/usr/bin/env python3
# -- coding: utf-8 --
LOG = '-->utils_file Log: '

def getListfromFile():
	list = []
	# openfile
	with open('foo.txt', 'r') as f:
		for line in f.readlines():
			a=line.strip().split('.')
			list.append(a)
	print(LOG,list)
	return list;
	

def initCaiDaXiaofromFile():
	list = []
	count = [0,0,0]
	last_index = [0,0,0]
	fa_interval = []
	# openfile
	with open('daxiao.txt', 'r') as f:
		for line in f.readlines():
			a = line.strip()
			if a is not '':
				list.append(a)
	print(LOG,list)
	for i in range(len(list)):			
		#process the init data
		if list[i] is 's':
			count[0] += 1
			last_index[0] = i
			pass
		elif list[i] is 'f':
			count[1] += 1
			fa_interval.append(i-last_index[1])
			last_index[1] = i
			pass
		else:
			count[2] += 1
			last_index[2] = i
			pass
	
	print(LOG,len(list),count,last_index)
	return list,count,last_index,fa_interval;