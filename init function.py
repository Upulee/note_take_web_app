def init(conn):
    db_create_db(conn)  # create database if not exist
    db_create_table(conn)  # create table if not exist

    # select data
    notes = db_select_all_notes(conn)

    for note in notes:
        list_notes.insert(tk.END, note[1])
        notes_ids.append(note[0])  # save the id

init(conn)
