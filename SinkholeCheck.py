import urllib2
from urllib2 import urlopen

ipverifier = "http://ip.42.pl/raw"
publicip = urlopen(ipverifier).read()

url = "http://iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com/"

def sinkholetest(endpoint):
    try:
        urllib2.urlopen(endpoint).read()
        print "WannaCry Sinkhole was reached"
        print "Your public ip is", publicip
    except urllib.error.URLError as e:
        print "WannaCry Sinkhole not reachable"
        try:
            print "Your public ip is", publicip
        except urllib.error.URLError as e:
            print "Are you sure you're connected to the internet?"
    return

sinkholetest(url)