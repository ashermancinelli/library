import csv
import os
from flask import Flask, render_template
app = Flask(__name__)

cs_lines = []
religion_lines = []

# https://docs.python.org/3/howto/sorting.html
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def cmp(x, y):
    return (x > y) - (x < y)

def lname_sorter(x):
    x = x[2]

    # Only grab first author
    if ';' in x:
        x = x.split(';')[0]

    if ',' in x:
        x = x.split(',')[0].strip()
    else:
        x = x.split(' ')[-1]

    return x

def name_sorter(x, y):
    '''
    Sort by last name, than first
    '''

    x = x[2]
    y = y[2]

    # Only grab first author
    if ';' in x:
        x = x.split(';')[0]

    # only grab first name
    if ' ' in x:
        if ',' in x:
            x_lname = x.split(',')[0].strip()
            x_fname = x.split(',')[-1].strip()
        else:
            x_lname = x.split(' ')[-1].strip()
            x_fname = x.split(' ')[0].strip()
    else:
        x_lname = x
        x_fname = None

    # Only grab first author
    if ';' in y:
        y = y.split(';')[0]

    # only grab first name
    if ' ' in y:
        if ',' in y:
            y_lname = y.split(',')[0].strip()
            y_fname = y.split(',')[-1].strip()
        else:
            y_lname = y.split(' ')[-1].strip()
            y_fname = y.split(' ')[0].strip()
    else:
        y_lname = y
        y_fname = None

    if y_fname is None or x_fname is None:
        return cmp(x_lname, y_lname)
    else:
        return cmp(x_lname, y_lname) or cmp(x_fname, y_fname)

@app.route('/')
def hello():
    return render_template(
        'base.html',
        cs_lines=cs_lines,
        religion_lines = religion_lines
    )

if __name__ == '__main__':
    with open('data/cs.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        cs_lines = [*csv_reader,][1:]
    with open('data/religion.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        religion_lines = [*csv_reader,][1:]

    cs_lines = sorted(cs_lines, key=cmp_to_key(name_sorter))
    religion_lines = sorted(religion_lines, key=cmp_to_key(name_sorter))
    app.run(debug=True, port=5000)

