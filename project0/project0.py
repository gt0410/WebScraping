import re
import sqlite3
from PyPDF2 import PdfFileReader, PdfFileWriter

def fetchincidents(url):
    from urllib import request
    
    data = request.urlopen(url).read()
    with open('link.txt', 'wb') as lk:
        lk.write(data)

def extractincidents():
    import tempfile
    data = open('link.txt', 'rb')
    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)
    
    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    page1 = re.sub(r"\s\n", " ", page1)
    page1 = re.sub(r"Officer", "Officer;", page1)
    page1 = re.sub(r";\n", ";", page1)
        #page1 = re.sub(r"REVOKE\nD", "REVOKE D", page1)
    page1 = re.sub(r"-\n", "-", page1)
    page1 = re.sub(r"\nD - DUS", " D - DUS", page1)
    mylist = page1.split(';')
    del mylist[0]
    for i in range(len(mylist)):
        mylist[i] = mylist[i].splitlines()
    del mylist[-1]
    for i in range(len(mylist)):
        for j in range(len(mylist[i]) - 9):
            mylist[i][6] = mylist[i][6] + ' ' + mylist[i][7+j]
        del mylist[i][7:-2]
    #full_list.extend(mylist)
    #print(len(mylist))
    #print(mylist)
    return mylist


def createdb():
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS arrests (arrest_time TEXT, \
    case_number TEXT, \
    arrest_location TEXT, \
    offense TEXT, \
    arrestee_name TEXT, \
    arrestee_birthday TEXT,\
    arrestee_address TEXT,\
    status TEXT,\
    officer TEXT)')

   # return normanpd.db

def populatedb(incidents):
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    for i in range(len(incidents)):
        c.execute("INSERT INTO arrests VALUES(?,?,?,?,?,?,?,?,?)", incidents[i])
        conn.commit()
    c.close()
    conn.close()

def status():
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute('SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1')
    m = c.fetchone()
    sym = chr(254)
    l = []
    for i in range(len(m)):
        l.append(m[i])

    #l[0] = re.sub(r"\s", sym, l[0])
    #l[6] = re.sub(r"\s", sym, l[6])
    #page1 = re.sub(r"\s\n", " ", page1)
    s = sym.join(l)
    s = s + ';'
    return s
