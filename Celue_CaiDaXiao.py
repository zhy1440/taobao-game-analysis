#!/usr/bin/env python3
# -- coding: utf-8 --
LOG = '-->CeLue_CaiDaXiao Log: '
DEBUG = '-->>Debug:'
XiaZhu = 10
Sum_Pay = 0
yingli = 0
cnt = 0
#default value
rate = 8
min_yingli = 10
#get input
try: 
	str_rate = input("Please enter the rate: ")
	if str_rate is not '':
		rate = int(str_rate)
	str_min_yingli = input("Please enter your hope reward: ")
	if str_min_yingli is not '':
		min_yingli = int(str_min_yingli)
	myCoin = int(input("Please enter how much you have now: "))
except ValueError:
	print("Oops!  Try again   ")

print (DEBUG,rate,min_yingli,myCoin)

while Sum_Pay < myCoin:

	cnt += 1
	while True:
		if XiaZhu*rate - (Sum_Pay + XiaZhu) >= min_yingli:
			break
		XiaZhu += 10
		
		
	Sum_Pay += XiaZhu
	reward = XiaZhu * rate
	yingli = reward - Sum_Pay
	print(cnt.rjust(6),XiaZhu.rjust(6),reward.rjust(6),Sum_Pay.rjust(6),yingli.rjust(6))