# Python Script: Movie Data Fetcher

This Python script fetches movie data from the [Dummy API](https://dummyapi.online/api/movies) and stores it in a local SQLite database file called `mydatabase.db`.

## Features
- Connects to an external API to retrieve movie data.
- Saves the fetched data into a SQLite database for easy access and local storage.

## Requirements

- Python 3.x
- The necessary packages are listed in `requirements.txt`.

## Setup

Follow these steps to set up and run the script:

### 1. Clone the repository 
```bash
git clone <repository_url>
`cd <repository_directory>`
```
### 2. Create and activate a virtual environment (optional)
```bash
# For Linux and macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run the Script
```bash
python main.py
```
