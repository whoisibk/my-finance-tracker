# My Finance Tracker

A web application that allows people track their income, expenses, and savings, helping them understand and manage their personal finances effectively.

## Key Features & Benefits

*   **Income Tracking:** Record and categorize income sources.
*   **Expense Tracking:** Monitor and classify expenses for detailed analysis.
*   **Savings Management:** Set savings goals and track progress.
*   **Data Visualization:** Gain insights through charts and graphs (planned feature).
*   **User-Friendly Interface:** Intuitive design for easy navigation.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python 3.x:**  (Required for running the application)
*   **pip:** (Python package installer)

The following Python packages are required. They can be installed using `pip`:

*   Flask
*   Flask-SQLAlchemy
*   SQLAlchemy
*   python-dotenv
*   blinker
*   click
*   colorama
*   itsdangerous
*   Jinja2
*   MarkupSafe
*   typing-extensions
*   Werkzeug
*   greenlet

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:whoisibk/my-finance-tracker.git
    cd my-finance-tracker
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following, replacing `<your_secret_key>` with a strong, randomly generated secret key:

    ```
    SECRET_KEY=<your_secret_key>
    ```

5.  **Run the application:**

    ```bash
    python run.py
    ```

    This will start the Flask development server.  You can then access the application in your web browser, typically at `http://127.0.0.1:5000/`.

## Usage Examples & API Documentation

The application provides a web interface for tracking finances. After setting up the database and running the application, create an account and log in.  You can then add income, expenses, and savings information through the provided forms.

*There is currently no API documentation for the application.*

## Configuration Options

*   **`SECRET_KEY`:**  This environment variable, defined in the `.env` file, is used to securely sign the session cookie.  **It is crucial to use a strong, randomly generated key.**

## Contributing Guidelines

We welcome contributions to enhance this project! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests to ensure the reliability of your code.
5.  Submit a pull request with a clear description of your changes.

Please adhere to the existing code style and structure.

## License Information

License not specified. All rights reserved by the owner.

## Project Structure

```
├── .gitignore
├── app.py
├── extensions.py
├── models.py
├── readme.md
├── requirements.txt
├── run.py
└── static/
    └── css/
        ├── dashboard.css
        └── login.css
    └── images/
        ├── favicon.ico
        ├── logo.png
        ├── logo1.png
        └── logo_.png
    └── js/
        ├── dashboard.js
        └── login.js
└── templates/
```

## Important Files:

### `app.py`

```py
from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
from extensions import db
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    return app

app = create_app()
```

### `extensions.py`

```py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### `models.py`

```py
from extensions import db
from sqlalchemy import ForeignKey, select
from datetime import datetime
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True) 
    password = db.Column(db.String(50), nullable=False)



    # def __repr__(self):
    #     return f"<User {self.name}>"
```

### `requirements.txt`

```txt
blinker==1.9.0
click==8.3.0
colorama==0.4.6
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
greenlet==3.2.4
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
SQLAlchemy==2.0.44
typing_extensions==4.15.0
Werkzeug==3.1.3
dotenv==0.9.9
```

### `run.py`

```py
from app import create_app
from extensions import db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(host="0.0.0.0", debug=True)
```