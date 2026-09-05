"""
Undo Behavior Using Stack
📌 Problem
You're building a text editor (or any app) that supports Undo.

Every action (like typing a character, deleting, formatting) is stored in a stack.

When the user presses Undo, you pop the last action from the stack and reverse it.
"""
#Thinking process.
"""
Core Idea
Stack follows LIFO (Last In, First Out).

The most recent action is undone first.

Optionally, you can use two stacks:

Undo stack → stores performed actions.

Redo stack → stores undone actions (so you can redo them later).
"""

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
        
    def type(self, word:str):
        self.undo_stack.append(self.text) #store prev text
        self.text += word
        self.redo_stack.clear()
        print(f"Typed '{word}', text = '{self.text}'")
    
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print(f"Undo performed, text = '{self.text}'")
    
    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo!")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print(f"Redo performed, text = '{self.text}'")
        
editor = TextEditor()
editor.type("Hello ")
editor.type("World")
editor.undo()   # Undo → text = "Hello "
editor.redo()   # Redo → text = "Hello World"
editor.undo()   # Undo → text = "Hello "
editor.undo()   # Undo → text = ""
