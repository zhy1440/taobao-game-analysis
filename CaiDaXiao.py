#!/usr/bin/env python3
# -- coding: utf-8 --
LOG = '-->CaiDaXiao Log: '
GAILV = {500/11,100/11,500/11}
import utils_file
sourceData = []
count =[0,0,0]
last_index = [0,0,0]
fa_interval = []

def output(count,sourceData,last_index,fa_interval):
	print(" ".rjust(5),"small".rjust(5),"fa".rjust(5),"big".rjust(5))
	print("-----------------------------------")
	print("count".rjust(5), end = " ")
	for c in count:
		print('{0:5d}'.format(c).rjust(5), end = " ")
	print()
	print("rate".rjust(5), end = " ")
	for c in count:
		print('{0:.2f}'.format(c*100/len(sourceData)).rjust(5), end = " ")
	#print("count",'{0:5d} {1:5d} {2:5d}'.format(small_count,fa_count,big_count).rjust(5))
	#print("rate:",'{0:.2f} {1:.2f} {2:.2f}'.format(small_count/len(sourceData),fa_count/len(sourceData),big_count/len(sourceData)).rjust(5))
	print(' '.rjust(5))
	print(" ".rjust(5),'{0:.2f}'.format(500/11).rjust(5), '{0:.2f}'.format(100/11).rjust(5),'{0:.2f}'.format(500/11).rjust(5))
	print()
	print(last_index,'fa_interval:',fa_interval)
	print(len(sourceData)-1-last_index[1])
	return
	
	return

def fenxi(interval):
	result = [0,0,0]
	for i in interval:
		if i <= 9:
			result[0] += 1
		elif i > 9 and i <= 24:
			result[1] +=1
		else:
			result[2] +=1

	return result

def s_f_b():
	#get previous result from file
	result = utils_file.initCaiDaXiaofromFile()
	sourceData = result[0]	
	count = result[1]
	last_index = result[2]
	fa_interval = result[3]
	print(LOG)
	output(count,sourceData,last_index,fa_interval)
	while True:
		try:
			tmp = input("Please enter the result(s,f,b): ")
			if tmp is '':
				break
			if tmp not in ['s','f','b']:
				print("That was out of range (s,f,b).  Try again  ")
				continue
			else:
				sourceData.append(tmp)
				
				#process the number
				if tmp is 's':
					count[0] += 1
					last_index[0] = len(sourceData)- 1
					pass
				elif tmp is 'f':
					count[1] += 1
					fa_interval.append(len(sourceData)- 1 - last_index[1])
					last_index[1] = len(sourceData)- 1
					pass
				else:
					count[2] += 1
					last_index[2] = len(sourceData)- 1
					pass
		except ValueError:
			print("Oops!  Try again   ")
		finally:
			output(count,sourceData,last_index,fa_interval)
			print(fenxi(fa_interval))
	return

	
s_f_b()