# chapter 1 operators
# arithmatic operators
# def calculator (x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
# calculator(2,5 )    
 

# strig methods

# 1)upper()
# str1 = "akash"
# print(str1.upper())

# 2) lower()
# print(str1.lower())
      
      
# 3) rstrip("!")
# 4) str1.replace
# 5) capitalize() -- capiptal the first letter

# 6) endswith()
# str2 = "Welcome to the console !!!"
# print(str2.endswith("!!!"))


import time


timestamp = time.strftime('%H:%M:%S')
print(timestamp)

name = input("Enter your name : ")

hours = int(time.strftime('%H'))

if(0<= hours <= 11):
  print("hello", name , "good morning")

elif(12<= hours <=16):
  print("hello " , name , "good afternoon")

else:
  print("hello ", name , "good eveing")

