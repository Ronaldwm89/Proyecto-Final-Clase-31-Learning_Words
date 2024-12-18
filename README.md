# Flashcards Program 📚

This is a simple flashcards program built in Python. The program helps users learn new words by displaying them in two languages and tracking their progress. It uses a CSV file as the database for the words.

---

## Features ✨

- Displays words in English and their translations in Spanish. 🌎
- Users can indicate whether they know a word or not. ✅❌
- Words marked as known are removed from the list. 🗑️
- Automatically updates the CSV file to only include unknown words for future practice. 🔄

---

## How It Works 🛠️

1. **CSV File as Database**: 
   - The program reads a CSV file containing the words.
   - Converts the data into a Python dictionary for easy manipulation.

2. **User Interaction**:
   - A graphical interface allows users to view a word and decide if they know it or not.
   - Two buttons: `I Know` 👍 and `I Don't Know` 👎.

3. **Data Update**:
   - If the user knows a word, it is removed from the dictionary.
   - The updated dictionary is saved back to the CSV file, ensuring that only unknown words are shown in the future.

---

## Prerequisites 🖥️

Make sure you have the following installed:

- Python 3.x 🐍
- The `pandas` library for working with the CSV file. 📂

You can install pandas using:
```bash
pip install pandas
```

---

## How to Run the Program ▶️

1. Clone or download the project. 📥
2. Prepare a CSV file with the following structure:
   ```csv
   english,spanish
   room,cuarto
   house,casa
   ```
3. Run the program:
   ```bash
   python flashcards.py
   ```

---

## Future Improvements 🚀

- Add support for additional languages. 🗣️
- Include a progress tracker to show how many words have been learned. 📊
- Implement a feature to review previously learned words. 🔙

---

## Notes ✍️

This project is part of my learning journey in Python. Feedback and suggestions are welcome to help me improve! 💡

---

### License 📜
This project is free to use and modify for personal or educational purposes.
