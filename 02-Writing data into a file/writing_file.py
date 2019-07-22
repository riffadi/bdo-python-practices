# writing data into a file
# f = open("data.txt", "w+")

# append data into a file
f = open("data.txt", "a+")

contents = f.write("\r6,5,4\n3,2,1")

print(contents)
