import sqlite3
from jinja2 import Template
from library_model import get_data

conn = sqlite3.connect('../library.sqlite')

tables = ['genre', 'publisher', 'reader', 'author', 'book_author', 'book', 'book_reader']

df_list = list(map(lambda x: get_data(x, conn), tables))

conn.close()

f_template = open('library_temp.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(
    relations=df_list,
    tables=tables,
    len=len
)

f = open('library.html', 'w', encoding='utf-8-sig')

f.write(result_html)
f.close()
