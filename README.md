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

cs5293p19-project0/
├── COLLABORATORS
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── project0
│   ├── __init__.py
│   └── main.py
├── docs
├── setup.cfg
├── setup.py
└── tests
    ├── test_download.py
    └── test_fields.py
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

