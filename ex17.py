from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "copying from %s to %s now." % (from_file, to_file)
in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long" % len(in_data)
print "Does the output file exists? %r" % exists(to_file)

print "Ready to go, Return to start / STRG-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)
print "Done!"
out_file.close()

