# 🧠 Flashy – French Flashcard Learning App

A simple and interactive flashcard app built with Python and Tkinter to help you learn French vocabulary efficiently.

---

## 🚀 Features

* 📖 Displays random French words
* 🔄 Automatically flips the card after 3 seconds to show English translation
* ✅ Mark words as “known” to remove them from the learning pool
* ❌ Skip difficult words without removing them
* 💾 Saves progress so you only study words you haven’t learned yet

---

## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* Pandas (data handling)

---

## 📂 Project Structure

```
day-31/
│── main.py
│── data/
│   ├── french_words.csv
│   └── words_to_learn.csv (generated automatically)
│── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
```

---

## ▶️ How It Works

1. The app loads words from:

   * `words_to_learn.csv` (if it exists), or
   * `french_words.csv` (default dataset)

2. A random French word is shown.

3. After 3 seconds:

   * The card flips to show the English translation.

4. User actions:

   * ✔ **Known** → removes the word and saves progress
   * ❌ **Unknown** → keeps the word for future review

---

## 🧪 How to Run

1. Install dependencies:

```bash
pip install pandas
```

2. Run the app:

```bash
python main.py
```

---

## 💡 Key Concepts Used

* Tkinter Canvas for UI rendering
* `after()` method for timed events
* Global state management (`current_card`, `flip_timer`)
* CSV read/write using Pandas
* Random selection for flashcards

---

## ⚠️ Notes

* Make sure image paths are correct or use relative paths:

```python
PhotoImage(file="images/card_front.png")
```

* If `words_to_learn.csv` doesn’t exist, it will be created automatically.

---

## 🎯 Future Improvements

* Add score tracking
* Add progress bar (words remaining)
* Add sound pronunciation
* Add difficulty levels

---

## 🙌 Credits

Built as part of a Python learning project to practice GUI development and data handling.

---

## 📌 Final Thoughts

This project is a great example of combining:

* UI development
* Data persistence
* User interaction

It’s small, but it teaches real-world app logic.
