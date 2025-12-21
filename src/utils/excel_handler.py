from openpyxl import Workbook
import os


# This function saves news data into an Excel file
def save_to_excel(news_data):
    # Create output folder if it does not exist
    os.makedirs("data/output", exist_ok=True)

    # Excel file path
    file_path = "data/output/daily_ai_news.xlsx"

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "AI News"

    # Add column headers
    ws.append(["Title", "Date", "Source", "Link", "Summary"])

    # Add each news row to Excel
    for row in news_data:
        ws.append(row)

    # Save the Excel file
    wb.save(file_path)

    return file_path
