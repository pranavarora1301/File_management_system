**File Management App**

A simple command-line Python application that provides basic file operations like **create**, **view**, **delete**, **read**, and **edit**. Built using core Python features including `os` and file I/O.

---

**Project Structure**

- `app.py` – Main CLI program to manage files
- `read.py` – Standalone script to read from `naya.txt`
- `write.py` – Standalone script to write a line to `naya.txt`

---

**Features**

- Create a new text file
- View all files in the current directory
- Delete any existing file
- Read content from a file (hardcoded to `naya.txt`)
- Append new data to a file (hardcoded to `naya.txt`)
- Exit the application

---

**Getting Started**

**Prerequisites**

Make sure Python 3 is installed:

```bash
python --version
```

**Run the App**

Clone the repository and run the main app:
```
git clone https://github.com/yourusername/file-management-app.git
cd file-management-app
python app.py
```

**Alternative Scripts**

You can also run the following utility scripts:
```
python write.py   # Writes a default line to 'naya.txt'
python read.py    # Reads and prints content from 'naya.txt'
```

**Example Usage**
FILE MANAGEMENT APP
1. CREATE FILE
2. VIEW ALL FILE
3. DELETE FILE
4. READ FILE
5. EDIT FILE
6. EXIT
Enter your choice(1-6): 1
Enter the file-name to create: demo.txt
File name demo.txt: Created successfully!

**Known Issues**

- read_file() and edit_file() use hardcoded 'naya.txt' instead of the user-provided filename
- The file creation block does not create a new file; it just tries to open an existing one (use 'x' mode instead of default)

**Improvements for Future**

- Accept dynamic filenames correctly in all operations
- Add file existence checks with os.path.exists()
- Add options for overwriting vs. appending in editing
- Convert into a class-based design for modularity
- Add GUI support (e.g., with tkinter or PyQt)
