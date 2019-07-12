#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'
QUESTIONS = {
    "Top 3 Articles": '''
    select title, count(1) "views"
    from log, articles
    where '/article/' || articles.slug = log.path
      and status = '200 OK'
    group by "title"
    order by "views" desc
    limit 3;
    ''',
    "Most Popular Authors":'''
    select name, count(1) "views"
    from log, articles, authors
    where '/article/' || articles.slug = log.path
      and articles.author = authors.id
      and status = '200 OK'
    group by "name"
    order by "views" desc;
    ''',
    "Days w/ Page Errors > 1%": '''
    select date(time) "day", round(avg(case when status = '200 OK' then 0 else 1 end)*100, 2) "erros_percent"
    from log
    group by "day"
    having avg(case when status = '200 OK' then 0 else 1 end) > 0.01 ;
    '''
}


def query(sql, params=''):
    conn = psycopg2.connect(dbname=DBNAME)
    try:
        with conn.cursor() as curs:
            curs.execute(sql, params)
            return curs.fetchall()
    except e:
        print('Unable to connect')
        raise e
    finally:
        conn.close()


def report():
    for question in QUESTIONS.items():
        title = question[0]
        results = query(question[1])
        print('-'*len(title))
        print(title)
        print('-'*len(title))
        for row in results:
            print(' | '.join([str(value) for value in row]))

        print()

if __name__ == "__main__":
    report()
