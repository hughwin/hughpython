from lxml import html
import sys
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')

# // selects all nodes with the same start
# @ selects the attributes of those nodes 

print "Buyers: ", buyers 
print "Prices: ", prices

file1 = "buyers.txt"
file2 = "prices.txt"

file = open(file1, 'w+')
file.write(str(buyers))
print("Buyers Complete")
file.close()

pricesoutput = open(file2, 'w+')
pricesoutput.write(str(prices))
print("Prices Complete")
pricesoutput.close()