# Memento class to store the state of the text editor
class TextMemento:
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

# Originator class representing the text editor
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def append_text(self, new_text):
        self.history.append(TextMemento(self.text))  # Save current state
        self.text += new_text

    def undo(self):
        if self.history:
            last_memento = self.history.pop()
            self.text = last_memento.get_text()

    def get_text(self):
        return self.text

# Example usage
editor = TextEditor()
editor.append_text("Hello, ")
editor.append_text("World!")
print("Current Text:", editor.get_text())

editor.undo()
print("After Undo:", editor.get_text())