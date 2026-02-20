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

#write a function that takes the name of a text file as parameter.
#Print out the 3-letter words that start with "b"

import requests
def download_book(url):
    """
    Downloads a book from a url
    :param url: the url for the book
    :return: None
    """
    response = requests.get(url)
    print(response.status_code)
    #save the book
    with open("book.txt", "w") as f:
        f.write(response.text)

download_book("https://www.gutenberg.org/ebooks/64317.txt.utf-8")

def find_3_letter_words(book_name):
    """
    find 3 letter words starting with B
    :param book_name: the file containing the book
    :return: None
    """
    unique_words = []
    special_chars = ",.?!;'"
    with open(book_name, "r") as f:
        for line in f:
            #remove punctuation
            for c in special_chars:
                line = line.replace(c, "")
            #break down the line into words
            words = line.split(" ")
            for word in words:
                if word not in unique_words and len(word) == 3 and word [0] == "b":
                    unique_words.append(word)
    print(unique_words)

find_3_letter_words("book.txt")
















