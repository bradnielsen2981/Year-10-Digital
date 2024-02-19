city = 'sydney'
citylist = ['brisbane','paris',city]
print(citylist[2])
citylist[2] = "canberra"
print(len(citylist))
for c in citylist: #for loop through a list
    print(c)
for index in range(len(citylist)): #0 - 2
    print(index)
    print(citylist[index])
citylist.append('melbourne')
citylist.remove('brisbane')
print(citylist)
mycity = citylist.pop(1)
print(mycity)
print(citylist)