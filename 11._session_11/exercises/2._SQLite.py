from sqlite3 import connect

with connect('exercises/zoo.db') as conn:
    cur = conn.cursor()

    cur.execute('CREATE TABLE animals(id int PRIMARY KEY, name text, weight int, food text)')
    cur.execute('INSERT INTO animals(id, name, weight, food) VALUES (1, "Monkey", 100, "Banana")')
    cur.execute('INSERT INTO animals(id, name, weight, food) VALUES (2, "Tiger", 70, "Meat")')
    cur.execute('INSERT INTO animals(id, name, weight, food) VALUES (3, "Butterfly", 1, "Nectar")')

    for i in cur.execute('SELECT * FROM animals'):
        print(i)

    cur.execute('DELETE FROM animals WHERE NAME = "Tiger"')
    print('Tiger deleted')

    for i in cur.execute('SELECT * FROM animals'):
        print(i)

    cur.execute('DROP TABLE animals')

    