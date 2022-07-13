lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for number in lst1:
    if type(number) is int:
        lst2.append(number)
    else:
        pass


print(lst1)
print(lst2)