from jinja2 import Template
import sqlite3
from model import get_data, get_genres

max_available_numbers = 2
chosen_genre_id = 3

conn = sqlite3.connect('../library.sqlite')

df_data = get_data(max_available_numbers, chosen_genre_id, conn)
df_genre = get_genres(conn)

conn.close()

f_template = open('view.html', 'r', encoding='utf-8-sig')

html = f_template.read()
f_template.close()

template = Template(html)

result_html = template.render(
    data=df_data,
    genres=df_genre,
    len=len

)


f = open('result.html', 'w', encoding='utf-8-sig')

f.write(result_html)
f.close()
