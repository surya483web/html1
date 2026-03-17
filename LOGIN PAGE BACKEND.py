user_name= input("USER NAME : ")
password = "08102006"
secret = ""
guess_count= 0
guess_limit = 3
out_of_limit = False

while secret != password and not out_of_limit:
    if guess_count < guess_limit:
     guess_count += 1
     secret = input("PASSWORD : ")
    else:
     out_of_limit = True
if out_of_limit:
   print("LOGIN FAILED")
elif user_name == "Surya":  
   print("WELCOME", user_name)
   print("LOGIN SUCESSFUL..!")
else:
   print("INCORRECT USER NAME...")
 