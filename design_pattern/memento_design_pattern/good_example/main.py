from history import History
from text_memento import TextMemento
from text_editor import TextEditor

text_editor = TextEditor()
history = History()

text_editor.write("Hello")
text_editor.write(" World")

print(text_editor.get_text())

history.save_state(text_editor.saved())

text_editor.write(" Good")
text_editor.write(" Byy")

print(text_editor.get_text())
history.save_state(text_editor.saved())


text_editor.write(" Goood")
text_editor.write(" Morning")

print(text_editor.get_text())
history.save_state(text_editor.saved())

history.get_history()

print("-----------------------------")

undo = history.undo()
print("After undo getting previous state: ", undo.get_saved_text())
text_editor.restore(undo)
print(text_editor.get_text())