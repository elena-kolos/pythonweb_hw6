import sqlite3
import sys


help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів з найбільшим середнім балом по всіх предметах
2 -- Знайти студента з найбільшим середнім балом з певної дисципліни. 
3 -- Знайти середній балл в групі з певної дисципліни. 
4 -- Знайти середній бал на потоці (по всій таблиці оцінок)
5 -- Знайти, які курси веде певний викладач. 
6 -- Список студентів в певній групі. 
7 -- Оцінки студентів в окремій групі за конкретною дисципліною.
8 -- Знайти середній балл, який ставить певний викладач по своїм дисциплінам. 
9 -- Знайти список курсів, які відвідує певний студент.
10 -- Знайти список курсів, які конкретному студенту читає конкретний викладач.
"""

def query_sql(file):
    with open(file) as f:
        sql = f.read()

    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


def main():
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        result = query_sql(f'query_{task}.sql')
        print(result)


if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        exit()
