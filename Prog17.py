n=input("Chocie you string:")
l=[]
for i in n.split():
    if i==i[::-1]:
        l.append(i)
print()
for i in range(len(l)):
    print(l[i])
print()
print(" The total{}palindrom:{}".format(len(l),l))
