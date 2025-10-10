# Automata Quiz App

An interactive quiz application built with **Python** and **Tkinter**, designed to help students learn and practice concepts from the **Theory of Automata** course.  
It includes multiple-choice questions, immediate feedback with explanations, and a modern GUI.

## 🚀 Features

- 🎯 Multiple-choice quiz on Automata Theory (100+ questions)  
- 💡 Detailed explanations after each answer  
- 📊 Score tracking and progress management  
- 🎨 Modern Tkinter GUI with custom styles and background  
- 🧩 Easily expandable `questions.json` file for new topics  

## 🧰 Tech Stack

- **Python 3.x**  
- **Tkinter** for GUI  
- **JSON** for question storage  

## 📂 Project Structure

```
Automata-Quiz-App/
│
├── gui.py              # Main GUI file
├── quiz_engine.py      # Handles quiz logic and question loading
├── questions.json      # Contains all questions, options, and answers
├── main.py             # Main entry point of project
├── README.md           # Project documentation
└── LICENSE             # MIT license
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/automata-quiz-app.git
   cd automata-quiz-app
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Enjoy learning Automata!**

## 🧩 Adding New Questions

You can easily add more questions to the `questions.json` file using the following structure:

```json
{
  "question": "What is the function of the δ (delta) function in DFA?",
  "options": ["Transition function", "Start state", "Set of final states", "Input alphabet"],
  "answer": "Transition function",
  "explanation": "The δ (delta) function defines how the automaton transitions between states based on input symbols."
}
```

## 👨‍💻 Authors

**Muhammad Farooq Nawaz Khan**  
📧 [farooqnawaz.fk@gmail.com](mailto:farooqnawaz.fk@gmail.com)
