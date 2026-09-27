# 🧮 Calculator

A feature-rich and elegant Command Line Calculator application built with Python. It allows users to perform basic and advanced arithmetic operations, store values in memory, maintain a persistent calculation history, and navigate a clean, interactive terminal UI.

---

## ✨ Features

* 🔢 **Multiple Operation Support:** Perform Addition, Subtraction, Multiplication, Division, Exponents, and Modulus.
* 💾 **Memory Management:** Save, recall, and clear values (`MS`, `MR`, `MC`), or type `M` directly into calculations.
* 📜 **Calculation History:** Track your operations continuously throughout the active session.
* 🗑️ **Delete History:** Clear stored calculation history on command.
* 🛡️ **Defensive Error Handling:** Built-in safeguards against invalid inputs and division-by-zero errors.
* 🎨 **Formatted CLI Interface:** Features ANSI colored highlights and automated screen clearing for a smooth experience.

---

## 🛠️ Built With

* **Python** (Core Language)
* **Standard Libraries:** `os`, `sys`

---

## 📸 Preview

```text
==========================================
          PYTHON TERMINAL CALCULATOR       
==========================================
Memory (M): 42.0

Choose an operation:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Power (^)
  6. Modulus (%)
  --- Memory Operations ---
  7. Memory Store (MS) - Save number/result
  8. Memory Recall (MR) - View current memory
  9. Memory Clear (MC) - Reset memory to 0
  --- History Operations ---
  10. View History
  11. Clear History
  12. Exit
------------------------------------------
Select an option (1-12): 1

[ Hint: Type 'M' during input to use the saved memory value ]
Enter first number: M
Using value from Memory: 42.0
Enter second number: 8

Result: 42.0 + 8.0 = 50.0

Save result (50.0) to memory? (y/n): y
Memory updated to: 50.0
📂 Project Structure
Plaintext
terminal-calculator/
│
├── calculator.py
└── README.md
🚀 Installation & Usage
1. Clone the Repository
Bash
git clone [https://github.com/yourusername/Calculator]
2. Navigate to the Project Directory
Bash
cd Calculator
3. Run the Application
Bash
python calculator.py
🎯 What I Learned
Global & Local State Management: Managing dynamic global variables (memory, history) across function calls.

Input Validation & Exception Handling: Using try-except blocks to handle invalid inputs gracefully.

Cross-Platform System Commands: Using os.system with ternary conditions for cls/clear across Windows and Unix OSs.

ANSI Escape Sequences: Formatting terminal text with colors and bold styling without external libraries.

Data Structure Manipulation: Tracking chronological execution logs using Python lists and enumerate().

Modular Code Architecture: Structuring helper functions cleanly with a standard if __name__ == "__main__": entry point.

🔮 Future Improvements
💾 Persistent History Storage: Save calculation history to a local .txt or .json file across sessions.

📐 Scientific Calculator Mode: Add trigonometry, square roots, and logarithms using Python's math module.

🔣 Complex Expression Parser: Evaluate full string expressions (e.g., (5 + 3) * 2) in a single prompt.

🎚️ Theme Customization: Allow users to choose custom ANSI color themes.

🌐 Web/GUI Expansion: Port the calculator engine into a graphical application using tkinter or PyQt.