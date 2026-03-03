f = open("yaser.txt", "w")
f.write("power marker")
f.close()

with open("yaser.txt", "r") as f:
    x = f.read()
print(x)
