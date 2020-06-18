from Tkinter import *
import tkinter as tk
from tkinter import messagebox

notes_ids = []
selected_index = 0


def onselect(evt):
    global selected_index
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    selected_index = index

    display_note(index, value)


window = tk.Tk()
window.title("Note Taking")

top_frame = tk.Frame(window)
scroll_list = tk.Scrollbar(top_frame)
scroll_list.pack(side=tk.RIGHT, fill=tk.Y)

list_notes = Listbox(top_frame, height=15, width=40)
list_notes.bind('<<ListboxSelect>>', onselect)
list_notes.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0), pady=(10, 10))


scroll_list.config(command=list_notes.yview)
list_notes.config(yscrollcommand=scroll_list.set, cursor="hand2", background="#fff5e6", highlightbackground="grey", bd=0, selectbackground="#c9b922")
top_frame.pack(side=tk.TOP, padx=(0, 5))


text_frame = tk.Frame(window)
note_title = tk.Entry(text_frame, width=39, font = "Helvetica 13")
note_title.insert(tk.END, "Title")
note_title.config(background="#F4F6F7", highlightbackground="grey")
note_title.pack(side=tk.TOP, pady=(0, 5), padx=(0, 10))


scroll_text = tk.Scrollbar(text_frame)
scroll_text.pack(side=tk.RIGHT, fill=tk.Y)
note_text = tk.Text(text_frame, height=7, width=40, font = "Helvetica 13")
note_text.pack(side=tk.TOP, fill=tk.Y, padx=(5, 0), pady=(0, 5))
note_text.tag_config("tag_your_message", foreground="blue")
note_text.insert(tk.END, "Notes")
scroll_text.config(command=note_text.yview)
note_text.config(yscrollcommand=scroll_text.set, background="#F4F6F7", highlightbackground="grey")

text_frame.pack(side=tk.TOP)

button_frame = tk.Frame(window)
photo_add = PhotoImage(file="add.gif")
photo_edit = PhotoImage(file="edit.gif")
photo_delete = PhotoImage(file="delete.gif")

btn_save = tk.Button(button_frame, text="Add", command=lambda : save_note(), image=photo_add)
btn_edit = tk.Button(button_frame, text="Update", command=lambda : update_note(), state=tk.DISABLED, image=photo_edit)
btn_delete = tk.Button(button_frame, text="Delete", command=lambda : delete_note(), state=tk.DISABLED, image=photo_delete)

btn_save.grid(row=0, column=1)
btn_edit.grid(row=0, column=2)
btn_delete.grid(row=0, column=3)

button_frame.pack(side=tk.TOP)