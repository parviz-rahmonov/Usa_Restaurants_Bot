# USA Restaurants Bot

A Telegram restaurant directory built with **Python 3.12+** and **aiogram 3**. Users can browse restaurants by US state, search listings, view restaurant details and map links, and filter by delivery availability. Authorized administrators can manage restaurant records through an interactive Telegram interface.

## Features

- Browse the restaurant catalog by US state
- Search restaurant listings
- View restaurant details and map links
- Filter restaurants by delivery availability
- Add, edit, view, and delete restaurants from the admin panel
- Multi-step admin forms using aiogram FSM
- Admin access control for messages and callback queries
- JSON persistence using atomic file replacement

## Tech stack

Python 3.12+, aiogram 3, python-dotenv, JSON local storage, unittest, and GitHub Actions.

## Installation

Clone the repository:

```bash
git clone https://github.com/parviz-rahmonov/Usa_restaurants_Bot.git
cd Usa_restaurants_Bot
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set the values:

```dotenv
BOT_TOKEN=your_telegram_bot_token
ADMIN_IDS=123456789
```

Use comma-separated Telegram user IDs for multiple administrators. Never commit `.env` or share your bot token.

Run the bot:

```bash
python bot.py
```

Only one polling process should run for the same Telegram bot token.

## Tests and continuous integration

Run the test suite locally:

```bash
python -m unittest discover -s tests -v
```

The suite covers JSON persistence, corrupt JSON handling, and administrative access filters. GitHub Actions runs these tests automatically on pushes and pull requests targeting `main`.

## Project structure

```text
.
├── .github/workflows/  # Continuous integration
├── data/               # Catalog and JSON storage
├── filters/            # Access and chat-type filters
├── handlers/           # Public bot handlers
│   └── admin/          # Administrative workflows
├── keyboards/          # Telegram keyboards
├── states/             # FSM states
├── tests/              # Unit tests
├── utils/              # Formatting helpers
├── bot.py              # Entry point
├── config.py           # Settings
├── constants.py        # Shared constants
├── .env.example        # Example environment configuration
└── requirements.txt    # Dependencies
```

## Data storage and limitations

The initial catalog is defined in `data/restaurants.py`. Administrator edits are saved in `data/db.json`, which is excluded from Git. **Back up `data/db.json`** to preserve edits.

Storage uses temporary files and atomic replacement to reduce the risk of incomplete JSON writes. It is not designed for multiple concurrent bot instances.

FSM state is stored in memory, so unfinished forms are lost on restart. Restaurant entries are example data and may be outdated. This is a portfolio/demo project, not a production-ready multi-instance service.

## Security

Administrative actions require an allowlisted Telegram user ID. Keep tokens and configuration private. Automated unit tests are not a substitute for end-to-end testing or a security audit.

## License

No license has been specified. All rights remain with the repository owner unless a license is added.
