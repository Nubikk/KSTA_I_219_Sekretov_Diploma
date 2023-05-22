import sqlite3
import os

db_file = '/path/to/db.sqlite3'
migrations_dir = '/path/to/migrations'

conn = sqlite3.connect(db_file)
c = conn.cursor()

# Применить миграции
for migration_file in os.listdir(migrations_dir):
    with open(os.path.join(migrations_dir, migration_file), 'r') as f:
        migration_sql = f.read()
        c.execute(migration_sql)

conn.commit()
conn.close()
