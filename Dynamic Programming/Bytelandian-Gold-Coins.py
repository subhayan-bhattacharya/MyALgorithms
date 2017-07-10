# Dynamic programming problems#
#http://www.spoj.com/problems/COINS/

value = {}
value[0] = 0
value[1] = 1
value[2] = 2

def cal_value(n):
	global value
	if n in value:
		return value[n]
	else:
		value[n] = max(n,cal_value(int(n/2)) + cal_value(int(n/3)) + cal_value(int(n/4)))
		return value[n]
        
try:
    while True:
        n = int(input())
        print (cal_value(n))
except:
    pass