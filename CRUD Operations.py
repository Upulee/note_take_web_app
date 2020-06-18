# DATABASE FUNCTIONS STARTS
conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")


def db_create_db(conn):
    mycursor = conn.cursor()
    query = "CREATE DATABASE IF NOT EXISTS db_notes"
    mycursor.execute(query)


def db_create_table(conn):
    db_create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (" \
          "note_id INT AUTO_INCREMENT PRIMARY KEY, " \
          "title VARCHAR(255) NOT NULL, " \
          "note VARCHAR(2000) NOT NULL)"
    mycursor.execute(query)


def db_insert_note(conn, title, note):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO tb_notes (title, note) VALUES (%s, %s)"
    val = (title, note)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid


def db_select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from tb_notes"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def db_select_specific_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title, note FROM tb_notes WHERE note_id = " + str(note_id))
    return mycursor.fetchone()


def db_update_note(conn, title, note, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE tb_notes SET title = %s, note = %s WHERE note_id = %s"
    val = (title, note, note_id)
    mycursor.execute(query, val)
    conn.commit()


def db_delete_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "DELETE FROM tb_notes WHERE note_id = %s"
    adr = (note_id,)
    mycursor.execute(query, adr)
    conn.commit()

