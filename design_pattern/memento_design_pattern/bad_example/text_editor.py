class TextEditor:
    def __init__(self):
        self.__text = ""

    def write(self, new_text):
        self.__text += new_text

    def get_text(self):
        return self.__text

text_editor = TextEditor()
text_editor.write("Hello")
text_editor.write(" world")
text_editor.write(" Goodbye")

print(text_editor.get_text())
