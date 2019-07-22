from urllib import urlopen

data = urlopen("http://humanstxt.org/humans.txt").read()

print(data)
