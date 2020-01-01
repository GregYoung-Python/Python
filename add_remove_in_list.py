app_users = ["Alice", "Bob", "Cindy", "Bill", "Joey", "Susan", "Walter"]
print(len(app_users))

while True:
    print("Hello my name is William! ")
    name = input("What is your name?: ").strip().capitalize()

    if name in app_users:
        print("Hello {}! " .format(name))
        remove = input("Would you like to be removed from the list? (y/n)?: ").strip().lower()

        if remove == "y":
            print(app_users)
            app_users.remove(name)
            print(app_users)
        elif remove == "n":
                print("Great we are glad you have decided to stay with us!")
    
    else:
        print("Your name is not in the list yet {}".format(name))
        add_name = input("Would you like to be added to the list (y/n)?: ").strip().lower()
        if add_name == "y":
            print(app_users)
            app_users.append(name)
            print(app_users)
        elif add_name == "n":
            print("No problem let us know if you change your mind!")
            


>>> L =[1,3, 5, 7, 9, 11, 13]
>>> del L[0]
>>> print(L)
[3, 5, 7, 9, 11, 13]
>>> del L [4:]
>>> print(L)
[3, 5, 7, 9]
>>> 
>>> L = [1,3,5,7,9,11,13,15]
>>> del L[5:]
>>> L
[1, 3, 5, 7, 9]
>>> L = [1,3,5,7,9,11,13,15]
>>> del L[3]
>>> L
[1, 3, 5, 9, 11, 13, 15]
