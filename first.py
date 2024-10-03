#string
#convert my_str ="abcd1234" to new_str="4321dcba"
# [start: end: steps]


my_str = "abcd1234"
new_str = my_str [::-1]
print(new_str)


# total table

number = [1, 2, 3, 4, 5, 6]
total = 0
for item in  number:
    total = total+ item
    print(total)



# (x,y)


for x in range(3):
    for y in range(3):

        print(f'({x};{y})')