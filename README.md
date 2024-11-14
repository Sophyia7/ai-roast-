# AI GitHub Roast App

## Overview

This App is a flask application that analyzes user commits and generates feedback using a model from Nebius AI. This app is designed to help developers improve their commit messages and ensure they follow best practices.

## Features

- Analyze commit messages for best practices.
- Provide feedback on commit message quality.
- Suggest improvements for better commit messages.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- [Flask](https://flask.palletsprojects.com/en/latest/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/commit-feedback-flask-app.git
   cd commit-feedback-flask-app
   ```

2. Create a virtual environment 

  ```bash
  python3 -m venv venv
  source venv/bin/activate  #for mac
  venv\Scripts\activate #for windows
  ``` 

3. Install dependencies

  ```bash
    pip install -r requirements.txt
  ```


# Usage
1. Run your application

```bash
flask run
```

2. Open your web browser and go to http://127.0.0.1:5000 and enter your Github username and repository

# Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Make your changes.Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Open a pull request.

# License
This project is licensed under the MIT LICENSE. 

