import sqlite3

persons = [
        ("Ioana", "Amariei"),
        ("Daniel", "Amariei")
    ]


def create_person_table():
    connection = sqlite3.connect(":memory:")

    connection.execute("CREATE TABLE person(firstname, lastname)")
    connection.executemany("INSERT INTO person(firstname, lastname) VALUES (?, ?)", persons)
    cursor = connection.cursor()

    for row in cursor.execute("SELECT firstname, lastname FROM person"):
        print(row)

    connection.commit()
    connection.close()


create_person_table()
