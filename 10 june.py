#conditional operator
#==, !=,>, <, >=, <=

cab_fare = 500
e_wallet = 200

result = e_wallet >= cab_fare

print( "can i book my cab:", result)
print (type(result))

email = input("enter email:")
password = input("enter password:")

print ("is login success ?")
result = (email =="diksha@example.com") and (password == "john123")
print (result)

otp = 3042
user_otp = int(input("enter otp recived"))
print ("is otp correct?", otp == user_otp)

#membership testing
a= 10
b= 10

print(a==b)
print(a is b)
print (a is not b)
