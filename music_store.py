cds = {
           "American Football":[3,3], "Better Oblivion":[21,3],
           "Two Hands":[10,3], "Young Enough":[15,3], "Stuffed & Ready":[4,3]
          }
while True:
    choice = input("Which cd would you like to purchase?: ").strip().title()
    if choice in cds:
        age = int(input("How old are you?: ").strip())
        if age >= cds[choice][0]:
            available = cds[choice][1]
            if available >0:
                print("Thank you for your purchase!")
                cds[choice][1] = cds[choice][1] -1
            else:
                print("Sorry we are sold out of that cd at this time, please try again later.")
        else:
            print("Sorry you are too young at this time to purchase this cd.")
    else:
        print("We don't sell that cd at this time.")
                
            
            

    
