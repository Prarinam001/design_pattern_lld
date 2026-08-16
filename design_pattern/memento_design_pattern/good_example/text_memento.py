class TextMemento:
    def __init__(self, text):
        self.__save_text = text

    def get_saved_text(self):
        return self.__save_text