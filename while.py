count = 25

while count <= 100:
    if count % 2 == 0:
        print(count)
    count = count + 1



number = 100
while number <= 130:
    if number % 2 != 0:
        print(number)
    number = number + 1
    

L = []
while len(L) < 4:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)
print("Sorry the list is full now.")
print(L)

