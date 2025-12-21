# Usage Guide — Daily AI Tech News Automation

This guide explains how to set up, run, and schedule the project to automatically collect daily AI news.

---

## 1. Clone the Repository
```bash
git clone <your-repo-url>
cd "AI_DAILY TECH NEWS_AUTOMATION"
```

---

## 2. Set Up Virtual Environment

It is recommended to create a virtual environment:
```bash
python -m venv venv
```

### Activate the environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Install required dependencies
```bash
py -m pip install -r requirements.txt
# or
python -m pip install -r requirements.txt
```

---

## 3. Configure Google Sheets

1. Create a Google Cloud service account
2. Download the `credentials.json` and place it in the project root
3. Share your target Google Sheet with the service account email
4. Make sure the sheet name is **"Daily AI News"** (or update `google_sheets.py` accordingly)

---

## 4. Run the Main Script

The main workflow collects news, saves to Excel, and uploads to Google Sheets:
```bash
python main.py
```

- Logs are saved in `logs/execution.log`
- Excel output is saved in `data/output/daily_ai_news.xlsx`

---

## 5. Run the Scheduler

To automate daily collection:
```bash
python main_scheduler.py
```

- By default, it runs every day at **9:00 AM**
- Keeps running in the background; logs each execution
- You can modify the schedule by editing the `schedule.every().day.at("09:00")` line in `main_scheduler.py`

---

## 6. Project Output

- **Excel file:** `data/output/daily_ai_news.xlsx`
- **Google Sheet:** "Daily AI News" updated with latest scraped articles
- **Logs:** `logs/execution.log` for script execution history

---

## 7. Notes

- Local output files and credentials are ignored in Git for security
- Modify or add RSS feeds in `src/scraper/news_scraper.py` to include more sources
- Ensure internet connection is active for both scraping and Google Sheets upload

---

**End of Guide**