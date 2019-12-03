import csv
import os
from flask import Flask, render_template
app = Flask(__name__)

cs_lines = []
religion_lines = []

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
    cs_lines.sort(key=lambda x: x[2], reverse=False)
    religion_lines.sort(key=lambda x: x[2], reverse=False)
    app.run()

