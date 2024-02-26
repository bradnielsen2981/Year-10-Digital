numberlist = [1,2,3,6,7]
numberlist.append(13)
numberlist.remove(5)
print(numberlist[3])

for number in numberlist:
    print(number)

for index in range(2,len(numberlist),2):
    print(numberlist[index])

