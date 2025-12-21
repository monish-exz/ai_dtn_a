import gspread
from oauth2client.service_account import ServiceAccountCredentials


# This function uploads news data to Google Sheets
def upload_to_google_sheets(news_data):
    # Required permissions for Google Sheets & Drive
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Load service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope
    )

    # Authorize Google Sheets client
    client = gspread.authorize(creds)

    # Open the Google Sheet
    sheet = client.open("Daily AI News").sheet1

    # Clear old data before adding new data
    sheet.clear()

    # Add header row
    sheet.append_row(["Title", "Date", "Source", "Link", "Summary"])

    # Add news rows
    for row in news_data:
        sheet.append_row(row)
