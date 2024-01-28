# Write and test a function that takes a string as a parameter and returns a sorted list
# of all the unique letters used in the string. So, if the string is cheese, the list
# returned should be ['c', 'e', 'h', 's'].

def sorter(s):
    new_list = []
    for i in s:
        new_list.append(i)
    new_list.sort()
    
    new_list = set(new_list)
    
    new_list = list(new_list)
    
    new_list.sort()
        
    return new_list

x = input("Enter a string: ")
y = sorter(x)
print(y)


# Write and test three functions that each take two words (strings) as parameters and
# return sorted lists (as defined above) representing respectively:
# Letters that appear in at least one of the two words.
# Letters that appear in both words.
# Letters that appear in either word, but not in both.

def list_return(w1, w2):
    word_1 = []
    for i in w1:
        word_1.append(i)
        
    word_2 = []
    for i in w2:
        word_2.append(i)
        
    return word_1, word_2    
    

def uni(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    unon = set.union(word1, word2)
    unon = list(unon)
    unon.sort()
    return unon

def inter(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    intern = set.intersection(word1, word2)
    intern = list(intern)
    intern.sort()
    return intern

def sym_diff(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    diff = set.symmetric_difference(word1, word2)
    diff = list(diff)
    diff.sort()
    return diff

w1 = input("Enter a word: ")
w2 = input("Enter a word: ")

print(f"Union = {uni(w1, w2)}")
print(f"Intersection = {inter(w1, w2)}")
print(f"Symmetric Difference = {sym_diff(w1, w2)}")



# Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).


countries_and_capitals = {
            "Nepal" : "Kathmandu",
            "UK" : "London",
            "France" : "",
            "Poland" : "Warsaw",
            "Germany" : "",
            "Hungary" : "Budapest"}

while True:
    country = input("Enter a country: ")

    found = False

    for i in countries_and_capitals:
        
        if i.lower() == country.lower():
            
            found = True
            
            if countries_and_capitals[i] == "":
                capital = input("Enter capital: ")
                
            else:
                print(countries_and_capitals[i])

    if found == False:
        print("Country not found")
    
    cont = input("Continue?(y/n) ").lower()
    
    if cont == "n" or cont == "no":
        break
    
    else:
        continue


# One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
    

message = input("Enter a string: ").lower()
words = []

for i in message:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        words.append(i)
    
freq = {}

for i in words:
    freq[i] = freq.get(i, 0) + 1

sorted_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)

for i in range(min(6, len(sorted_freq))):
    print(f"{sorted_freq[i][0]} : {sorted_freq[i][1]}")

# /-----------------------------------------------------------------------------/
mes = "Hello world"
mesa = []
for i in mes:
    mesa.append(i.lower())
    
nl = []

for i in mesa:
    char = i
    
    c = 1
    
    mesa.remove(i)
    
    for j in mesa:
        if j == char:
            c += 1
    
    nl.append([char, c])

nl