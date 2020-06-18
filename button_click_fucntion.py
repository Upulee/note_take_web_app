# BUTTON CLICK FUNCTION 
def save_note():
    global conn
    title = note_title.get()

    if len(title) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the note title")
        return

    note = note_text.get("1.0", tk.END)
    if len(note.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the notes")
        return

    # Check if title exist
    title_exist = False
    existing_titles = list_notes.get(0, tk.END)

    for t in existing_titles:
        if t == title:
            title_exist = True
            break

    if title_exist is True:
        tk.messagebox.showerror(title="ERROR!!!", message="Note title already exist. Please choose a new title")
        return

    # save in database
    inserted_id = db_insert_note(conn, title, note)
    print("Last inserted id is: " + str(inserted_id))

    # insert into the listbox
    list_notes.insert(tk.END, title)

    notes_ids.append(inserted_id)  # save notes id

    # clear UI
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)


def update_note():
    global selected_index, conn

    title = note_title.get()

    if len(title) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the note title")
        return

    note = note_text.get("1.0", tk.END)
    if len(note.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter the notes")
        return

    note_id = notes_ids[selected_index]  # get the id of the selected note

    # save in database
    db_update_note(conn, title, note, note_id)

    # update list_note
    list_notes.delete(selected_index)
    list_notes.insert(selected_index, title)

    # clear UI
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)


def delete_note():
    global selected_index, conn, notes_ids
    title = note_title.get()
    notes = note_text.get("1.0", tk.END)

    print("Selected note is: " + str(selected_index))

    if len(title) < 1 or len(notes.rstrip()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="Please select a note to delete")
        return

    result = tk.messagebox.askquestion("Delete", "Are you sure you want to delete?", icon='warning')

    if result == 'yes':
        # remove notes from db
        note_id = notes_ids[selected_index]
        db_delete_note(conn, note_id)
        del notes_ids[selected_index]

        # remove from UI
        note_title.delete(0, tk.END)
        note_text.delete('1.0', tk.END)
        list_notes.delete(selected_index)


def display_note(index, value):
    global notes_ids, conn
    # clear the fields
    note_title.delete(0, tk.END)
    note_text.delete('1.0', tk.END)

    note = db_select_specific_note(conn, notes_ids[index])

    # insert data
    note_title.insert(tk.END, note[0])
    note_text.insert(tk.END, note[1])

    btn_delete.config(state=tk.NORMAL)
    btn_edit.config(state=tk.NORMAL)

window.mainloop()
