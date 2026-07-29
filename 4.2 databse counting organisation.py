import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (
    org TEXT,
    count INTEGER
)
''')

fname = input('Enter file name: ')

if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    conn.close()
    quit()

for line in fhand:
    if not line.startswith('From '):
        continue

    words = line.split()

    if len(words) < 2:
        continue

    email = words[1]

    if '@' not in email:
        continue

    org = email.split('@', 1)[1]

    cur.execute(
        'SELECT count FROM Counts WHERE org = ?',
        (org,)
    )

    row = cur.fetchone()

    if row is None:
        cur.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)',
            (org,)
        )
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?',
            (org,)
        )

conn.commit()

sqlstr = '''
SELECT org, count
FROM Counts
ORDER BY count DESC
'''

for row in cur.execute(sqlstr):
    print(row[0], row[1])

fhand.close()
cur.close()
conn.close()