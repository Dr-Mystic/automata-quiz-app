import tkinter as tk
from tkinter import messagebox
from quiz_engine import QuizEngine

class QuizGUI:
    def __init__(self, master):
        self.master = master
        master.title("Automata Quiz App")
        master.geometry("600x400")
        master.configure(bg="#009570")

        self.engine = QuizEngine("questions.json")

        self.content_frame = tk.Frame(master, bg="#009570", bd=0, relief="groove")
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.question_label = tk.Label(self.content_frame, text="", wraplength=500, font=("Lucida Calligraphy", 16), bg="#009570", fg="white")
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []

        for _ in range(4):
            btn = tk.Radiobutton(self.content_frame, text="", variable=self.var, value="",
                                font=("Lucida Calligraphy", 14), bg="#009570", fg="white", selectcolor="#009570",  anchor="w")
            btn.pack(anchor="w", padx=20)
            self.options.append(btn)

        self.submit_button = tk.Button(self.content_frame, text="Submit", command=self.submit, bg="#009571", fg="white", font=("Lucida Calligraphy", 12))
        self.submit_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        question = self.engine.get_next_question()
        if not question:
            self.show_result()
            return

        self.var.set(None)
        self.question_label.config(text=question["question"])

        for i, opt in enumerate(question["options"]):
            self.options[i].config(text=opt, value=opt)

    def submit(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please choose an option.")
            return

        correct, right_answer, explanation = self.engine.check_answer(selected)
        if correct:
            messagebox.showinfo("Correct", f"Good job! That's correct.\nExplanation: {explanation}")
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer was: {right_answer}\nExplanation: {explanation}")

        self.load_question()

    def show_result(self):
        total = 10
        score = self.engine.score
        messagebox.showinfo("Quiz Complete", f"You scored {score} out of {total}.")
        self.master.quit()
