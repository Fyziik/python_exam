import csv, json
from sqlite3 import connect

""" def conn():
    with connect('exercises/text_files/bohr.db') as conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS quotes')
        cur.execute('CREATE TABLE quotes(id int PRIMARY KEY, quote text, author text)')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES (1, "An expert is a person who has made all the mistakes that can be made in a very narrow field.", "bohr")')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES (2, "Prediction is very difficult, especially about the future.", "bohr")')
        cur.execute('INSERT INTO quotes(id, quote, author) VALUES(3, "Those who are not shocked when they first come across quantum theory cannot possibly have understood it.", "bohr")')
        return cur """

def text_file_decorator(func):
    def inner(*args):
        with open('exercises/text_files/bohr.txt', 'r') as f:
            func(''.join(f.readlines())) # or *list -> list unpacking
    return inner



def csv_decorator(func):
    def inner(*args):
        with open('exercises/text_files/bohr.csv', 'r') as f:
            csv_r = csv.reader(f, delimiter=',')
            next(csv_r)                            # skip first row
            func(*[row[1] for row in csv_r])       # get content column, and unpack list
    return inner



def json_decorator(func):
    def inner(*args):
        with open('exercises/text_files/bohr.json', 'r') as f:
            txt = f.read()
            js = json.loads(txt)
        func(*[i['quote'] for i in js])
    return inner



def sqlite_decorator(func):
    def inner(*args):
        with connect('exercises/text_files/bohr.db') as conn:
            cur = conn.cursor()
            func(*(i[0] for i in cur.execute('SELECT quote FROM quotes'))) # result from db is return as rows of tuples. i[0] gives the first element of the tuple
    return inner




#@text_file_decorator
#@csv_decorator
#@json_decorator
@sqlite_decorator
def quotes(*args):
    for _ in args:
        print(_)

quotes(('Honey Im home!', 'A car is a car until ...'))