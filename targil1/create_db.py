import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Ahuva123!",
    database="corona_db"
)
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
         id INT PRIMARY KEY,
         first_name VARCHAR(255) NOT NULL,
         last_name VARCHAR(255) NOT NULL,
         address VARCHAR(255) NOT NULL,
         date_of_birth DATE NOT NULL,
         telephone VARCHAR(20),
         mobile_phone VARCHAR(20) NOT NULL,
         vaccine_1_date DATE,
         vaccine_1_manufacturer VARCHAR(255),
         vaccine_2_date DATE,
         vaccine_2_manufacturer VARCHAR(255),
         vaccine_3_date DATE,
         vaccine_3_manufacturer VARCHAR(255),
         vaccine_4_date DATE,
         vaccine_4_manufacturer VARCHAR(255),
         positive_result_date DATE,
         recovery_date DATE
    )
""")

insert_query = """
    INSERT INTO members (id,
         first_name,
         last_name,
         address,
         date_of_birth,
         telephone,
         mobile_phone,
         vaccine_1_date,
         vaccine_1_manufacturer,
         vaccine_2_date,
         vaccine_2_manufacturer,
         vaccine_3_date,
         vaccine_3_manufacturer,
         vaccine_4_date,
         vaccine_4_manufacturer,
         positive_result_date,
         recovery_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
members_data = [
    (364758365, "David", "Cohen","Tel Aviv, Alenbi, 30","1990-05-30", "098562547", "0584659824", "2022-03-15","Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-10", "2023-08-20"),
    (576038950, "Yosi", "Levi", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-10", "2023-08-20"),
    (125874639, "Daniel", "Abutbul", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (768904736, "Shir", "Idan", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (768098484, "Shimon", "Sitbon", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna","2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (685833959, "Shira", "Haim", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (888586848, "Tal", "Taliban", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (980967475, "Avi", "Ron", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (879687934, "Roni", "Halfon", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (678903546, "Or", "Elbaz", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (890765432, "Ari", "Ye", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna","2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (908756892, "Colon", "Bia", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna","2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (123456789, "Hadar", "Avidan", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15", "Moderna","2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (768124653, "Cor", "Ona", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15","Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
    (676109738, "Shilat", "Davis", "Tel Aviv, Alenbi, 31", "2002-05-30", "084525476", "05846525875", "2022-03-15","Moderna", "2022-04-01", "Moderna", "2022-04-20", "Pfizer", None, None, "2023-08-20", "2023-08-20"),
]
cursor.executemany(insert_query, members_data)

# Commit changes and close the connection
connection.commit()
cursor.close()
connection.close()