# Online Student Marks Alert System

This repository contains an Online Student Marks Alert System built with Python and Flask. The application allows for managing student data and sending alerts based on their marks.

## Project Structure
Online-Student-Marks-Alert-System/  
├── app.py            # Main Flask application file  
├── init_db.py        # Script to initialize the SQLite database  
├── school.db         # SQLite database file  
├── static/           # Static files (CSS, JS, images, etc.)  
│   └── ...  
├── templates/        # HTML templates for the Flask app  
│   └── ...  
└── requirements.txt  # List of Python dependencies  


## Features

- **CRUD Operations:** Create, Read, Update, and Delete student data.
- **Marks Alerts:** Send alerts based on student marks.
- **SQLite Database:** Persistent data storage with SQLite.
- **Flask Framework:** Lightweight web framework to handle routing and rendering.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rudransh-pokhriyal/Online-Student-Marks-Alert-System.git
   cd Online-Student-Marks-Alert-System
2. **Install the dependencies:**
   ```bash
      pip install -r requirements.txt
3. **Initialize the database:** 
   ```bash
     python init_db.py
4. **Run the application:**
   ```bash
      python app.py
5. **Open your browser and navigate to:**
   ```bash
      http://127.0.0.1:5000/

### Deployment
This project can be deployed using Firebase Hosting and Cloud Functions.

### Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Contributions are always welcome!
