# # Assignment on operators

# # pre-set password
# name="Messi is the GOAT"
# # prompt to input password
# password=input("Enter your password:")

# if name==password:
#     print("Access Granted:")
# else:
#     print("Access Denied:")  

name=str(input("Enter your name: "))
score=int(input("Enter your score: "))

if score>=90 and score <=100:
    print("We Mzee {}, wow! Congratulations you've scored an A".format(name))
elif score>=80 and score <=89:
    print("We Mzee {}, a mile journey starts with a step and guess what! You are one step closer, you've scored a B".format(name))
elif score>=70 and score <=79:
    print("We Mzee {}, pull up your socks, you have scored a C".format(name))
elif score>=60 and score <=69:
    print("We mzee {}, ukikaa vibaya utachimba, you've scored a D".format(name))
elif score>=0 and score<=59:
    print("We mzee {}, we ni bundu, you've scored an F".format(name))
else:
    print("You've entered an invalid mark:")