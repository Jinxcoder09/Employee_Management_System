import psycopg2

conn = psycopg2.connect(
    dbname="ems_db",
    user="postgres",
    password="mannu1234",
    host="localhost",
    port="5432"
)

print("Connected!")
