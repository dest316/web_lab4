import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(rid, conn):
    return pd.read_sql(f'''SELECT title as 'Название', GROUP_CONCAT(author_name, ', ') as 'Автор(-ы)',
                    borrow_date as 'Дата выдачи', return_date as 'Дата возврата'
                       FROM book JOIN book_reader USING (book_id) JOIN book_author USING (book_id) JOIN author USING (author_id) 
                       WHERE reader_id = {rid}
                        GROUP BY book_id, book_reader_id''', conn)
