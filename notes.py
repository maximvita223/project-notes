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



def edit_note():
 notes = load_notes()
 note_id = input("Введите идентификатор заметки, которую хотите отредактировать: ")

 if note_id in notes:
    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новый текст заметки: ")
    timestamp = input("Введите новую дату/время изменения заметки: ")

    note = {
    'title': title,
    'body': body,
    'timestamp': timestamp
    }

    notes[note_id] = note
    save_notes(notes)
    print("Заметка отредактирована")

 else:
    print("Заметка с таким идентификатором не существует")



def delete_note():
    notes = load_notes()
    note_id = input("Введите идентификатор заметки, которую хотите удалить: ")
    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print("Заметка удалена")

    else:
        print("Заметка с таким идентификатором не существует")



def view_note():
 notes = load_notes()
 note_id = input("Введите идентификатор заметки, которую хотите посмотреть: ")

 if note_id in notes:
    note = notes[note_id]
    print("Заголовок:", note['title'])
    print("Тело заметки:", note['body'])
    print("Дата/время создания/изменения:", note['timestamp'])

 else:
    print("Заметка с таким идентификатором не существует")



def list_notes():
 notes = load_notes()

 for note_id, note in notes.items():
    print("Идентификатор:", note_id)
    print("Заголовок:", note['title'])
    print("Тело заметки:", note['body'])
    print("Дата/время создания/изменения:", note['timestamp'])
    print()


