import time
import os

def num(x):
	if x==0:
		return ["****",
				"*  *",
				"*  *",
				"*  *",
				"****"]
	elif x==1:
		return ["  **",
				" * *",
				"*  *",
				"   *",
				"   *"]
	elif x==2:
		return [" ** ",
				"*  *",
		        "  * ",
			    " *  ",
				"****"]
	elif x==3:
		return ["*** ",
				"   *",
				"*** ",
				"   *",
				"*** "]
	elif x==4:
		return ["  * ",
				" *  ",
				"****",
				"   *",
				"   *"]
	elif x==5:
		return ["****",
				"*   ",
				"****",
				"   *",
				"****"]
	elif x==6:
		return ["****",
				"*   ",
				"****",
				"*  *",
				"****"]
	elif x==7:
		return ["****",
				"   *",
				"   *",
				"   *",
				"   *"]
	elif x==8:
		return ["****",
				"*  *",
				"****",
				"*  *",
				"****"]
	elif x==9:
		return ["****",
				"*  *",
				"****",
				"   *",
				"****"]


while True:
	h1 = num(time.localtime()[3]/10)
	h2 = num(time.localtime()[3]%10)
	m1 = num(time.localtime()[4]/10)
	m2 = num(time.localtime()[4]%10)
	s1 = num(time.localtime()[5]/10)
	s2 = num(time.localtime()[5]%10)
	for i in range(5):
		print (str(h1[i])+" "+str(h2[i])+"   "+str(m1[i])+" "+str(m2[i])+"   "+str(s1[i])+" "+str(s2[i]))
	print("Press ctrl+c to close")
	time.sleep(1)
	os.system("clear")
	
	
	
