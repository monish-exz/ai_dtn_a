# Daily AI Tech News Automation

This project is a fully automated system to collect daily AI and Machine Learning news from trusted tech websites and store it in both **Excel** and **Google Sheets**. It simplifies monitoring the latest developments in AI and provides an easily accessible, organized format for daily review.

---

## Features

- Scrapes AI news from multiple trusted sources via RSS feeds.
- Stores news articles in an **Excel** file for offline access.
- Automatically uploads the data to **Google Sheets** for cloud-based access.
- Maintains logs of execution for tracking and debugging.
- Fully automated with configurable scheduling.
- Handles network errors gracefully and logs issues.

---

## Project Architecture

The project is organized as follows:
```
AI_DAILY TECH NEWS_AUTOMATION/
├── src/                          # Source code modules
│   ├── scraper/                  # Web scraping scripts
│   │   └── news_scraper.py       # Scrapes RSS feeds from multiple websites
│   ├── sheets/                   # Google Sheets integration
│   │   └── google_sheets.py      # Uploads data to Google Sheets
│   └── utils/                    # Utility modules
│       ├── excel_handler.py      # Saves data to Excel
│       └── logger.py             # Sets up logging
├── data/output/                  # Stores Excel files (ignored by Git)
├── logs/                         # Execution logs (ignored by Git)
├── main.py                       # Main script to run the workflow
├── main_scheduler.py             # Scheduler to run the workflow daily
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview
├── LICENSE                       # License file
├── .gitignore                    # Ignored files
└── credentials.json              # Google API credentials (ignored)
```

---

## Supported News Sources

- TechCrunch (Artificial Intelligence Tag)
- MIT Technology Review (AI Section)
- Analytics India Magazine

---

## Dependencies

- Python 3.8+
- `requests`
- `beautifulsoup4`
- `openpyxl`
- `pandas`
- `gspread`
- `oauth2client`
- `schedule`
- `lxml`

> All dependencies can be installed using `requirements.txt`.

---

## Logging

Execution logs are stored in the `logs/` folder (`execution.log`) and track:

- Script start and finish times
- Number of articles scraped
- Any errors or warnings encountered

---

## Notes

- The project requires a **Google Cloud service account** with access to Google Sheets.
- All local output (`Excel` files, logs) are ignored in Git via `.gitignore`.
- The project is designed to be extendable — you can add more news sources or output formats.
