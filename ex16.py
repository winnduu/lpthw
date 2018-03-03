from sys import argv
script, filename = argv

print "we are going to erase .%r." % filename
print "If you dont want it, press STRG-C to stop the script right now!"
print "If you want to continue, press RETURN"
raw_input("?")

print "opening file .%r now!" % filename
target = open(filename, 'w')

print "truncation the file now! GoodBye!"

target.truncate()

print "im going to ask you for three new lines to add into .%r" % filename

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Im going to write those into the file now!"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally closing the file after succesfull writing"
target.close()
