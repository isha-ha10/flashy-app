# 🧠 Flashy – French Flashcard Learning App

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Pandas](https://img.shields.io/badge/Data-Pandas-orange)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)

An interactive flashcard app built with Python to help you learn French vocabulary through repetition and active recall.

---

## 📸 Preview

<img width="1499" height="971" alt="image" src="https://github.com/user-attachments/assets/971797a8-5822-45e8-835c-d08135a3090d" />

<img width="1536" height="960" alt="image" src="https://github.com/user-attachments/assets/a2051a5d-383a-40cf-b382-fa175c513bb5" />


---

## 🚀 Features

* 🎴 Random French word generator
* ⏱️ Auto-flip card after 3 seconds
* ✅ Mark words as known (removes them permanently)
* ❌ Skip words to revisit later
* 💾 Progress saved automatically using CSV
* 🔁 Resume learning where you left off

---

## 🧠 How It Works

* The app loads vocabulary from:

  * `words_to_learn.csv` (if available), OR
  * `french_words.csv` (default dataset)

* Each flashcard:

  1. Shows a French word
  2. Flips after 3 seconds
  3. Reveals the English translation

* User interaction:

  * ✔ Known → word removed + progress saved
  * ✖ Unknown → word stays in rotation

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** → GUI
* **Pandas** → CSV handling
* **Random module** → card selection

---

## 📂 Project Structure

```
flashy-app/
│── main.py
│── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/isha-ha10/flashy-app.git
cd flashy-app
```

### 2. Install dependencies

```bash
pip install pandas
```

### 3. Run the app

```bash
python main.py
```

---

## ⚠️ Important Notes

* Use **relative paths** for images:

```python
PhotoImage(file="images/card_front.png")
```

* Ensure your folder structure matches the project layout
* `words_to_learn.csv` will be created automatically

---

## 🎯 Future Improvements

* 📊 Progress bar / words remaining
* 🔊 Audio pronunciation support
* 🌙 Dark mode UI
* 📱 Mobile-friendly version (using Kivy or web app)
* 🧩 Multiple language support

---

## 🧪 Learning Outcomes

This project demonstrates:

* GUI design with Tkinter
* Event-driven programming
* File persistence with CSV
* State management in Python apps
* Real-world app logic (not just scripts)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss ideas.

---

## ⭐ Show Your Support

If you found this useful, give it a ⭐ on GitHub!

---

## 📌 Author

Built as part of a hands-on Python learning journey focused on building real applications.
-Isha

