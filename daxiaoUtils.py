#!/usr/bin/env python3
# -- coding: utf-8 --
LOG = '-->daxiaoUtils Log: '

def one_six():
	while True:
		try:
			tmp = input("Please enter a number(1-11): ")
			if tmp is '':
				break
			x = int(tmp)
			if x < 1 or x > 11:
				print("That was out of range number.  Try again  ")
				continue
			else:
				sourceData.append(x)
				
				#process the number
				if x >=1 and x<=5:
					count[0] += 1
					pass
				elif x is 6:
					count[1] += 1
					pass
				else:
					count[2] += 1
					pass
		except ValueError:
			print("Oops!  That was no valid number.  Try again   ")
		finally:
			print("sourceData:",sourceData)
			print(" ".rjust(5),"small".rjust(5),"fa".rjust(5),"big".rjust(5))
			print("-----------------------------------")
			print("count".rjust(5), end = " ")
			for c in count:
				print('{0:5d}'.format(c).rjust(5), end = " ")
			print()
			print("rate".rjust(5), end = " ")
			for c in count:
				print('{0:.2f}'.format(c/len(sourceData)).rjust(5), end = " ")
			#print("count",'{0:5d} {1:5d} {2:5d}'.format(small_count,fa_count,big_count).rjust(5))
			#print("rate:",'{0:.2f} {1:.2f} {2:.2f}'.format(small_count/len(sourceData),fa_count/len(sourceData),big_count/len(sourceData)).rjust(5))
			print()
			print(' ', 5/11,1/11,5/11)
			print()
	return