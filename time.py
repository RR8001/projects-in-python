#pinting good morning,goodevening and good night according to tht time of the user

import time

if int(time.strftime("%H"))<12:
    print("Goodmorning sushant")
    print("current date and time  is :",time.ctime())

elif int(time.strftime("%H")) >=12 and int(time.strftime("%H")) <17 :
    print("Goodevening sushant!")
    print("current date and time  is :",time.ctime())
    
else:
    print("Good Night sushant!")
    print("current date and time is:",time.ctime())