string = "Python Programming"
print (string[:6])#print python
print (string[7:])#print programming
if "Java" in string:
    print("already exists")
else:#as java doesnt exist in string,replace space with java
    string = string.replace(" "," java ")
    print(string)
print(len(string))#length of string
print(len(string.split()))#number of words
print(string.title())#capitalize each word
split_111  = ''.join(string.split())#remove all space
print(split_111)
print(string.count("A"))#find frequiencies of alpjabests
print(string.count("P"))
print(string.count("R"))