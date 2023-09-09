import json


def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)

    except FileNotFoundError:
        notes = {}

    return notes



def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)



def add_note():
 notes = load_notes()
 note_id = input("Введите идентификатор заметки: ")
 title = input("Введите заголовок заметки: ")
 body = input("Введите текст заметки: ")
 timestamp = input("Введите дату/время создания заметки: ")

 note = {
 'title': title,
 'body': body,
 'timestamp': timestamp
 }

 notes[note_id] = note
 save_notes(notes)
 print("Заметка добавлена")


