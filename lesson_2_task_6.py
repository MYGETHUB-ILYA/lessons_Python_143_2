lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

length_lst = len(lst)

for i in range(1, length_lst + 1):
    if i < 30 and i % 3 == 0:
        print(i)
