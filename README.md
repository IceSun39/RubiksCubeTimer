# Rubik's Cube Timer

A web-based Rubik's Cube timer for tracking solves and analyzing your solving statistics.

## Features

* ⏱️ Rubik's Cube solve timer
* 📝 Automatic recording of solve times
* 📊 Solve history and statistics
* 📈 Tracking of average solve times
* 🎲 Scramble generation
* 💾 Persistent storage of solves
* 🌐 Web interface

## Tech Stack

* **Python**
* **Django**
* **HTML / CSS**
* **JavaScript**
* **SQLite**

## Project Structure

```text
RubiksCubeTimer/
├── cubing_hub/       # Main Django application
├── tracker/          # Solve tracking and timer functionality
├── manage.py         # Django management script
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/IceSun39/RubiksCubeTimer.git
cd RubiksCubeTimer
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Usage

1. Open the timer in your browser.
2. Generate or view the current scramble.
3. Start the timer.
4. Stop the timer when you finish the solve.
5. Your solve time is saved to the history.
6. Use the statistics to track your progress.

## Statistics

The application is designed to help track solving progress over time, including individual solve times and averages.

This makes it possible to monitor improvements in solving speed and identify consistency issues.

## Roadmap

* [ ] More detailed statistics
* [ ] WCA-style averages (`Ao5`, `Ao12`, etc.)
* [ ] Solve time charts
* [ ] Multiple puzzle types
* [ ] User accounts
* [ ] Personal best tracking
* [ ] Improved mobile support

## Author

**Vlad Kolesnyk**

GitHub: [IceSun39](https://github.com/IceSun39)
