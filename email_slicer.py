# get user email address
email = input("What is your email address? ").strip()

#slice out user name
user = email[:email.index("@")]


#slice domain name
domain = email[email.index("@") + 1:]




#format message
output = "Your user name is {} and your domain is {}.".format(user, domain)



#display output message
print(output)










#get information from customer
Fname = input("What is your first name? ")

Lname = input("What is your last name? ")

Phone = input("What is your phone number? ")

Zip = input("What is your zip code? ")

output = "Your first name is {} and your last name is {}. Your phone number is {} and your zip code is {}.". format(Fname, Lname, Phone, Zip)

print(output)

