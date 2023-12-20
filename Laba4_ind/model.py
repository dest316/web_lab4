import pandas as pd


def get_data(max_av_numbers, gen_id, conn):
    return pd.read_sql(f'''SELECT title AS 'Название', CASE
  WHEN publisher_name = 'ПИТЕР' OR publisher_name = 'ДРОФА' THEN 'ПИТЕР-ДРОФА'
  ELSE publisher_name
  END AS 'Издательство', year_publication AS 'Год'
                FROM book JOIN publisher USING (publisher_id)
                 WHERE available_numbers < {max_av_numbers} AND genre_id = {gen_id}
                 ORDER BY year_publication DESC, title''', conn)


def get_genres(conn):
    return pd.read_sql('''SELECT * FROM genre''', conn)

