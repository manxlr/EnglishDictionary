# 📖 English Dictionary App
A modern Python GUI application to explore and search an English dictionary stored in SQLite. The app allows users to view all words or search for specific entries, with a sleek, copyable interface built using Dear PyGui.

English Dictionary App is a lightweight, visually appealing tool that lets you interact with an embedded dictionary database effortlessly. Whether you want to browse all entries or look up a specific word’s type and definition, this app provides a smooth experience with robust SQLite integration.

## 🔍 Key Features
Embedded SQLite Database
Includes a dictionary database within the executable—no external files needed!
Search and Browse
Search for a specific word and see its type and definition.
View the entire dictionary in alphabetical order.
Modern GUI Interface
Built with Dear PyGui, featuring a dark theme, rounded corners, and GPU-accelerated rendering for a contemporary look.
Copyable Results
Select and copy text from the results area for easy use elsewhere.
Thread-Safe Design
Handles SQLite queries safely across threads for reliable performance.
Open-Source Project
Fully transparent and open for contributions under the MIT license.

---

## 📝 Table of Contents

1. [Usage](#-usage)  
2. [Database Details](#-database-details)  
3. [Contribution](#-contribution)  
4. [License](#-license)  
5. [Contact](#-contact)  
6. [Donations](#-donations)

---
## 📥 **Download Executable**

### Windows [Program](https://github.com/manxlr/englishdictionary/releases/download/v1.0.0/dictionary.exe)

Includes the dictionary database—no additional setup required!

---
## 🚀 **Usage**
Download dictionary.exe from the assets folder.
Run it directly from any directory.
The GUI will launch, displaying all dictionary entries.
Type a word in the search bar and press Enter or click Search to find its details.
Click Show All to refresh the full list.
Select text in the results area and press Ctrl+C to copy.

---
## 🛡️ **Database Details**

The app includes an embedded SQLite database (dictionary.db) with a table named entries containing:
word (TEXT, primary key)
wordtype (TEXT)
definition (TEXT)
Example entry: "abandon", "v. t.", "To cast or drive out; to banish; to expel; to reject."
The database is bundled in the executable using PyInstaller, making it fully portable and read-only.
## 🤝 **Contribution**
We welcome contributions! If you have improvements, bug fixes, or new features, feel free to contribute:
Fork the repository.
Create a new branch.
Submit a Pull Request with a detailed description of your changes.
Repo Link: https://github.com/manxlr/EnglishDictionary

---
## 📜 **License**
This project is licensed under the MIT License, allowing you to freely use, modify, and distribute the code.

[MIT License](https://opensource.org/licenses/MIT)

---
## 📧 **Contact**

For any questions, suggestions, or feedback, please reach out:

- **Email**: [nszeeshankhalid@gmail.com](mailto:nszeeshankhalid@gmail.com)
- **GitHub**: [https://github.com/manxlr](https://github.com/manxlr)

---

## 💖 **Donations**

If you find this project helpful and would like to support its continued development, you can donate using the following cryptocurrency addresses:

- **Ethereum (ETH)**: `0x23774348bc491Ff70F39c63f39B0e542a59b5B14`  
- **Bitcoin (BTC)**: `bc1qp7wltg8frvecuujjs9f3ck28r0s0h0qzld2fu6`  
- **Dogecoin (DOGE)**: `DTbwxMs4wenN2kUea77rHPQ8nbJrSk4o7D` 
