# Import the function that scrapes news from all websites
from src.scraper.news_scraper import scrape_all_websites

# Import Excel saving function
from src.utils.excel_handler import save_to_excel

# Import Google Sheets upload function
from src.sheets.google_sheets import upload_to_google_sheets

# Import logger setup
from src.utils.logger import setup_logger

import logging


# Main function that controls the whole workflow
def main():
    # Setup logging configuration
    setup_logger()
    logging.info("Script started")

    try:
        # Step 1: Scrape AI news articles
        news_data = scrape_all_websites()
        logging.info(f"Scraped {len(news_data)} articles")

        # Warning if no articles are found
        if not news_data:
            logging.warning("No articles scraped!")

        # Step 2: Save scraped data into Excel file
        excel_path = save_to_excel(news_data)
        logging.info(f"Saved to Excel: {excel_path}")

        # Step 3: Upload the same data to Google Sheets
        upload_to_google_sheets(news_data)
        logging.info("Uploaded to Google Sheets")

    except Exception as e:
        # Log any unexpected error
        logging.error(str(e))

    logging.info("Script finished")


# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
