# Game-Recommendation

An application that recommends video games based on user data from Steam.


---

## Table of Contents

- [Introduction](#introduction)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Structure](#structure)  
- [Possible Improvements](#possible-improvements)  
- [License](#license)  


---

## Introduction

Game-Recommendation is a Python application that generates personalized video game recommendations using data from the Steam platform. It analyzes a user’s game library, including playtime and owned titles, and matches it with game metadata such as genres and tags.

The system uses a content-based approach to identify patterns in user preferences and suggest relevant games from a larger dataset.


---

## Features

- Fetches user data from Steam API (owned games, playtime)  
- Processes game datasets stored in JSON format  
- Extracts and analyzes:
  - genres  
  - tags  
  - ratings  
- Builds a user preference profile based on playtime distribution  
- Scores and ranks games based on similarity to user preferences  
- Outputs a list of recommended games  


---

## Requirements

These are the minimal prerequisites to run the project:

- Python (version 3.10 or newer)  
- Required Python packages (see `requirements.txt`)  

You may also need:

- access to Steam API  
- a prepared dataset of games (JSON format)  


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ynzulak/Game-recommendation
cd Game-recommendation
```

2. (Recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS / Linux

# Windows:
# venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```


---

## Usage

Run the application:

```bash
python main.py
```

Example:

```
Enter Steam ID: 7656119XXXXXXXXXX

Top recommendations:
1. Game A (score: 0.85)
2. Game B (score: 0.81)
3. Game C (score: 0.78)
```


---

## Structure

```
Game-recommendation/
├── steamAPI/              # Steam API integration
├── steamUserData.py       # User data handling
├── recommender.py         # Recommendation logic
├── data/                  # Game datasets
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── README.md
└── .gitignore
```


