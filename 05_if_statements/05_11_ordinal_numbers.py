#5-11. Ordinal Numbers
#Store the numbers 1 through 9 in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Loop through the list
for num in numbers:
    #Use an if-elif-else chain inside the loop to print the proper ending
    if (num==1):
        print(f"{num}st")
    elif (num==2):
        print(f"{num}nd")
    elif (num==3):
        print(f"{num}rd")
    else:
        print(f"{num}th")