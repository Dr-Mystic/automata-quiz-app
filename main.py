from tkinter import Tk
from gui import QuizGUI

def main():
    root = Tk()
    app = QuizGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
