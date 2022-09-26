# import pyshorteners
import  pyshorteners
# Enter the url to shorten
long_url = input("Enter the url to shorten : ")
# pyshorteners. Shortener
type_tiny = pyshorteners.Shortener()
# Returns a short url.
short_url = type_tiny.tinyurl.short(long_url)
# Prints the shorten url
print("The shorten url is : "+ short_url)