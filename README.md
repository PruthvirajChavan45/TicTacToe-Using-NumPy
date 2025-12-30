# 🎮 Tic Tac Toe Game — Python | NumPy | Streamlit  

A clean, interactive **Tic Tac Toe web application** built using **Python, NumPy, and Streamlit**, showcasing logical thinking, array manipulation, and UI development skills.  
This project demonstrates how core NumPy concepts can be applied to build a real-world interactive game.

![Tic Tac Toe UI](./Project%20UI.jpg)

---

## 🚀 Project Highlights

✅ Interactive 3×3 Tic Tac Toe board  
✅ Two-player gameplay (❌ vs ⭕)  
✅ Real-time winner & draw detection  
✅ Clean and responsive UI  
✅ Restart functionality  
✅ Efficient NumPy-based logic  
✅ Beginner-friendly yet recruiter-ready project  

---

## 🧠 Key Concepts Demonstrated

### 🔹 NumPy Concepts
- Fancy indexing  
- Conditional selection  
- Array-based game state handling  
- Row, column & diagonal evaluation  
- Logical operations using NumPy  
- Efficient matrix manipulation  

### 🔹 Programming Concepts
- Clean modular functions  
- Conditional logic  
- State management  
- Loop-based rendering  
- UI–logic separation  

### 🔹 Streamlit Concepts
- `st.session_state` for game memory  
- Dynamic buttons  
- Layout using columns  
- Custom CSS styling  
- Interactive UI updates  

---

## ⚙️ Game Logic Overview

The game board is represented using a **3×3 NumPy array**:

| Value | Meaning |
|------|---------|
| `1`  | Player ❌ |
| `-1` | Player ⭕ |
| `0`  | Empty cell |

### ✅ Win Condition
A player wins when:
- Any row sum = ±3  
- Any column sum = ±3  
- Any diagonal sum = ±3  

### 🤝 Draw Condition
- No empty cells left  
- No winning condition satisfied  

---

## 🧩 Core Logic Example

```python
if abs(np.sum(board[i, :])) == 3:
    return "X" if np.sum(board[i, :]) == 3 else "O"
```

```python
if not (board == 0).any():
    return "DRAW"
```

---

## 🛠 Tech Stack

- **Python**
- **NumPy**
- **Streamlit**
- HTML + CSS (for UI styling)

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install streamlit numpy
```

### Step 2: Run the application
```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
tic-tac-toe/
│
├── app.py              # Main Streamlit application
├── Project UI.jpg      # App UI screenshot
└── README.md           # Project documentation
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Apply NumPy indexing in real applications  
- Build game logic using matrix operations  
- Manage app state using Streamlit  
- Create interactive UIs with Python  
- Convert theory into a working project  
- Write clean and professional documentation  

---

## 💼 Why This Project Matters (For Recruiters)

✔ Demonstrates problem-solving skills  
✔ Shows practical NumPy usage  
✔ Combines logic + UI development  
✔ Clean and readable code structure  
✔ Real-world mini-project approach  
✔ Ready to scale with AI or multiplayer logic  

---

## 🔮 Future Improvements

- Add AI opponent using Minimax  
- Highlight winning line  
- Scoreboard system  
- Sound effects  
- Online multiplayer mode  
- Mobile UI optimization  

---

⭐ If you like this project, feel free to ⭐ the repository and connect with me!

📌 *Built with learning, logic, and passion for Python & Data Science.*
