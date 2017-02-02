from bs4 import BeautifulSoup
import urllib
import urllib.request
import sys




def make_soup(url): #function for getting the website address
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

pdf_id = 0
myurl="http://www.rewardinglearning.org.uk/microsites/mathematics/gce/past_papers/index.asp"
soup = make_soup(myurl) #calling the make soup function and passing in an html link
file = open("pdf.out", 'wb') #opens the file and enables write back
sys.stdout = file
for pdf in soup.findAll(class_="pdf"):#finds all the span tags which is where all the pdfs are located
    pdf = str(pdf.text)
    pdf_id = pdf_id+1
    pdf = pdf + "\n"
    file.write(bytes(pdf, encoding="ascii",errors='ignore'))
file.close()

