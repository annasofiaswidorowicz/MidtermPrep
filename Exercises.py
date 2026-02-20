#Indicate the type of each
print(type(2+3))
print(type("abc".find))
print(type(print(2*2)))

#Indicate the result
print(2+3)
print(6/2)
print(5 or 6)
print([1,2,3].append("John"))
print("bubu"*2)
print(len(["abc", 2]))
print(2+3*2**2)

#Assume operations in order - what will each display
a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])




















