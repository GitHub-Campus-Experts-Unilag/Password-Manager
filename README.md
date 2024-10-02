Password Manager Project

# Password Manager

A secure and simple command-line interface (CLI) password manager. This tool allows users to safely store, generate, and retrieve passwords. Contributions to improve security, features, and usability are welcome. 🎉

## What are we building?

We are building a **Password Manager** CLI application that securely manages user passwords through encryption. It allows users to store, retrieve, and generate strong passwords directly from the command line. The aim is to provide a fast, lightweight, and secure solution for managing passwords without the need for a graphical interface.

## Stacks

Here are the main tools/technologies being used for this build. These automatically form the prerequisites.

- **Python 3.8+**
- **SQLite** (for local password storage)
- **Cryptography** library (for encryption)
- **Click** (for command-line argument parsing)

## SETUP

1. **Clone the project:**

   ```bash
   git clone https://github.com/GitHub-Campus-Experts-Unilag/Password-Manager.git
   cd Password-Manager

2. **Install dependencies:**
    
    ```bash
    pip install -r requirements.txt

3. **Run the CLI:**
    
    ```bash
    python main.py --help


## Project Structure
    Password-Manager/
    ├── main.py
    ├── README.md
    └── requirements.txt

## GUIDELINES
- When creating new branch if you're fixing a bug or implementing a feature follow this pattern:
    - fixing: `fix/<name-of-fix>`
    - feature: `feat/<name-of-feature>`
- Never commit directly into the main branch. Always create a new branch and PR.


