d = {} #empy dictionary
print(d)
print(type(d))
d = {"yes": "si", "no": "no", "one": "uno", "two": "dos", "tree": "arbol"}
print(d)
print(len(d))
#indexing
print(d["tree"])
#word = input("I speak Spanish, give me a word to translate ")
#print(d[word])
for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)

#can add more words to the dictionary
d["peacock"] = "pavo real"
print(d)

print(d.get("carrot", "undefined"))
print(d.get("tree", "undefined"))
print(d.values())
print(d.keys())

