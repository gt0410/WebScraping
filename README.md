# Gowtham Teja Kanneganti

## CS 5293, Spring 2019 Project 0

In this project we are trying to download the arrests pdf from the [norman police website](http://normanpd.normanok.gov/content/daily-activity) using the url. The website consists of Public Records of Daily Incident Summary, Daily Case Summary and Daily Arrests Summary. In this project we will take into consideration only arrests summary. The first page of the pdf is read and saved in to db. Using text mining techniques it is ensured that proper field in the pdf are saved into relevant fields in db. This project is done with the use of Python and Linux command line tools. 

## Getting Started

The following instructions will help you to run the project.

### Prerequisites

The project is done in python 3.7.2 version. Any version of python-3 will be sufficient to run the code. Also pip environment should be installed. Pyenv and pipenv can be created by using the folowong code in the project. Also a account in [github](https://github.com/) is necessary.
~~~
pyenv install python 3.7.2
pipenv --3.7.2
~~~

### Installing

After setting up the python environment and pip environment the following packages ehich are used in the code need to be installed.

~~~
pipenv install re
pipnev install PyPDF2
pipenv install sqlite3
~~~

The above packages need not be installed in the pip environment you are working but should be available to import.


## Project Description

### Directory Structure

The structure of the directory of this project is as given below.

cs5293p19-project0/ \
├── COLLABORATORS \
├── LICENSE \
├── Pipfile \
├── Pipfile.lock \
├── README.md \
├── project0 \
│   ├── __init__.py \
│   └── main.py \
├── docs \ 
├── setup.cfg \
├── setup.py \
└── tests \
    ├── test_download.py \
    └── test_fields.py \
    └── ... 

The structure is received initially from the repository created in the git. This repository can be brought into Ubuntu by cloning that repository. This can be done by using the following code

~~~
git clone "git repository link"
~~~

After that the Pipfile and Pipfile.lock will be created when piipenv is created. All other files are created in command line. 
If any changes are made in the repository then they need to be pushed into git. The status of the git can be checked using the following code.
~~~
git status
~~~

When the above command is run, it shows all the files that are modified. These files need to be added, commited and then pushed into git. The following code is followed:
~~~
git add file-name
git commit -m "Message to be displayed in git"
git push origin master
~~~

### Functions description

#### main.py

The main function is written in main.py . Your code should take a url from the command line and perform each operation. After the code is installed, you should be able to run the code using the command below.

~~~
pipenv run python project0/main.py --arrests <url>
~~~

Using argparse the url given in the command line will be passed to main. All the functions defined in project0.py are imported in main.py.

#### Download Data

fetchincidents() uses the python urllib.request library to grab the pdf from the given url. 

You can use the code below to grab the daily activity web page.
~~~
url = ("http://normanpd.normanok.gov/filebrowser_download/"
       "657/2019-01-24%20Daily%20Arrest%20Summary.pdf")

data = urllib.request.urlopen(url).read()
~~~

The data downloaded from the pdf is saved into a temporary file in any directory. This file should be available to read for the next method.

#### Extract Data

The function extractincidents() takes no parameters and it reads data from the above saved fils and extracts the arrests. The each arrest includes a Arrest Date/Time, Case Number, Arrest Location, Offense, Arrestee, Arrestee Birthday, Arrestee Address, City, State, Zip Code, Status and Officer. A city, state, and zip code will typical be available if the arrested person(s) is not homeless or transient. This data is hidden inside of a PDF file.

To extract the data from the pdf files, use the PyPdf2.PdfFileReader class. It will allow you to extract pages and pdf file and search for the rows. Extract each row and add it to a list.

Here is an example python script that takes data from a bytes object that contained pdf data, writes it to a temporary file, and reads it using the PyPdf2 module.

~~~
import tempfile
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
~~~

This function can return a list of rows so another function can easily insert the data into a database. In this prooject we are only considering the first page of any pdf.

#### Create Database

The createdb() function creates an SQLite database file named normanpd.db and inserts a table with the schema below.

~~~
CREATE TABLE arrests (
    arrest_time TEXT,
    case_number TEXT,
    arrest_location TEXT,
    offense TEXT,
    arrestee_name TEXT,
    arrestee_birthday TEXT,
    arrestee_address TEXT,
    status TEXT,
    officer TEXT
);
~~~

Note, all the columns correspond directly to the columns in the arrest pdfs. The arrest address contains information from the arrestee address, city, state, and zip code. Notice some “cells” have information on multiple lines, your code should take care of this.

#### Insert Data

The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database. Again, the signature of this function can be changed as needed.

#### Status Print

The status() function prints to standard out, a random row from the database. Each field of the row should be separated by the thorn character (þ).

~~~
2/16/2019 10:49þ2019-00013113þ36TH AVE NW / QUAIL DRþDRIVING WITH LIC. CANCELED/SUSPENDED/REVOKE D
 - DUSþCHRISTINA JENISE WARDENþ6/20/1976þ908 E COMANCHE ST Norman OK 73071þFDBDC (Jail)þ1527 - Rog
ers;
~~~

### Running the tests

The test files test the different features of the code. This will allow us to test if the code is working as expected. There are several testing frameworks for python, for this project use the
py.test framework. For questions use the message board and see the pytest
documentation for more examples http://doc.pytest.org/en/latest/assert.html .
This tutorial give the best discussion of how to write tests
https://semaphoreci.com/community/tutorials/testing-python-applications-withpytest.

Install the pytest in your current pipfile. You can install it using the command
pipenv install pytest. To run test, you can use the command pipenv run
python -m pytest. This will run pytest using the installed version of python.
Alternatively, you can use the command pipenv run python setup.py test.

Test cases are written for all the five functions. For the purpose of testing a url link is already given and the tests are written based on this url only. The test cases are written for each function.

#### Testing Download url

In this test case we are testing if the function fetchincidents() is downloading from the url and writing in the text file. After calling the function we are testing checking whether the file is none or not. This test case only checks whether the data is downloaded from the url but donot check if that is arrests url or not.

#### Testing Extract Data

In this test case we are testing the data extracted from the function extractincidents(). Since, I am converting the arrests data in to lists the tests are done to check if the length of the list is same as the number of observations and whether each observation is having eight fields to write into db.

#### Testing Created db

In this test case we are testing if the createdb() function is creating a database and also a table with name arrests. 

#### Testing fields in db

In this test we are checking if the extracted fields are saved exactly as we need or not. To check this we are giving a arrestee birthday and getiing the name of arrestee with that birth date. Tests are written to check the data type of thid name and to verify whether the name of the arrestee is same or not.

#### Testing Status

In this test case we are checkin if the status() function is returning string data type or not.


