print "Lets practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "________________"
print poem
print "________________"

five = 10 - 2 + 3 -6
print "This is Number Five: %s" % five

def secret_formular(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formular(start_point)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars and %d crates." % secret_formular(start_point)

