a = "string"
k = """
yaser arafath studied in mdit endineering collage,and he graduated in 2024 
and he had a weekness in english ,but now he has been improving his english spoken skill
"""  # for multi line string\
c = "  h        1.   "
d = "yaser isfree"
# print(a[1]) #out is t
# print(a[-1])# last char =g
print(len(c))
b = (
    "Free" in d
)  # space count for every operation,so space like a charactor and also case sensitive
# print(b)
# e = "hello yaser"
# print(e[5:0])  #  starting index to end-1 index,[5:0]->reverse is not this way
# a = "                          Hello, World! "
# print(a.strip())  # returns "Hello, World!"
# print(k.upper())
# print(a.lower().strip())
s = "yaser arafath is the best student"
w = ",he has studied in mdit"
# print(s.lower().split(" "))
# print(s + " ", b)
# print(k.splitlines())
s = list()
l = k.splitlines()
print(l[1])
for i in range(0, len(l)):
    s.append(l[i].split())
print(s)
