
from bs4 import BeautifulSoup
import urllib2  # html parser
import pandas

# Parse html
html      = "http://www.iaaf.org/athletes/united-states/mary-cain-263803"
open_html = urllib2.urlopen(html)
data      = open_html.read()

cols = ['Event', 'Time','Place','Date']
df = pandas.DataFrame(columns = cols)
records=[]
# One way to do it, just uses urllib2.
for table in data.split("</table>"):
        if "<table" in table and 'class="records-table' in table:
                for item in table.split("</td>"):
                    if "<td" in item:
                    	element = item.split(">")[-1].strip()
                    	if element:
                        	records.append(element)
                print records
                   # df.append(records)
                records = []
# In the works. If you run it, you just get a bunch of vectors of data..

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Alternative, using BeautifulSoup. In the works, doesn't do what I want.
# (Want to strip the wind column. It's been too long.)
topics  = ["Wind"] # to not extract

soup    = BeautifulSoup(data) # read into BeautifulSoup
table = soup.find('table', {'class': 'records-table'})
cols = ['Event', 'Time','Place','Date']
df = pandas.DataFrame(columns = cols)
n = (len(table.findAll('tr')) - 1)
for row in table.findAll('tr')[0:n]:

	col = row.findAll('td')
	print col
	event = col[0].getText();
	performance = col[1].getText();
	place = col[3].getText();
	date = col[4].getText();
	df.append([event,performance,place,date])

print df

                

