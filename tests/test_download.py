import pytest
import sqlite3

import project0

from project0 import project0

url = "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-17%20Daily%20Arrest%20Summary.pdf"

def test_download_sanity():

    project0.fetchincidents(url)
    data = open('link.txt', 'rb')
    assert data is not None

def test_extract_fields():
    project0.fetchincidents(url)
    l = project0.extractincidents()
    assert len(l) == 15
    assert len(l[0]) == 9

def test_table_name():
    project0.createdb()
    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    m = c.fetchone()

    assert m[0] == 'arrests'

def test_table_check():
    project0.fetchincidents(url)
    incidents = project0.extractincidents()
    project0.createdb()
    project0.populatedb(incidents)

    conn = sqlite3.connect('normanpd.db')
    c = conn.cursor()
    c.execute("SELECT arrestee_name FROM arrests WHERE arrestee_birthday = '2/18/1999';")

    f = c.fetchone()
    assert type(f[0]) == str
    assert f[0] == 'CHASE LESLIE'



def test_final_status():
    project0.fetchincidents(url)
    incidents = project0.extractincidents()
    project0.createdb()
    project0.populatedb(incidents)
    s = project0.status()
    assert type(s) == str
