#!/usr/bin/env python
import urllib2

for url in ["URL_1","URL_2"]:
# from try block we get Response 200
# from except block we get response 404
    try:
        connection = urllib2.urlopen(url)
        print connection.getcode()
        connection.close()

    except urllib2.HTTPError, e:
        print e.getcode()    
    

