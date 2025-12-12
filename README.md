# Price Tracker

A robust, Python-based tool designed to track product prices on e-commerce platforms (currently supporting Amazon). It features an automated scraper, a SQLite database for historical data storage, and a Streamlit dashboard for data visualization.

## Key Features

*   **Smart Scraping**: Uses `BeautifulSoup` with header rotation and caching to bypass basic anti-bot protections.
*   **Data Persistence**: Stores price history using **SQLAlchemy** and **SQLite**.
*   **Scalable Architecture**: Built with the **Factory Pattern** to easily add new shops (e.g., PCComponentes, eBay).
*   **CLI Interface**: Manage products via command-line arguments.
*   **Interactive Dashboard**: Visualize price trends over time using **Streamlit** and **Plotly**.

## Tech Stack

*   **Language**: Python 3.10+
*   **Core**: `Requests`, `BeautifulSoup4`
*   **Database**: `SQLAlchemy`, `SQLite`
*   **Visualization**: `Streamlit`, `Pandas`, `Plotly`
*   **Code Quality**: `Black`, `Pytest`

## Project Structure

```text
price_tracker/
├── config/         # Configuration settings and environment variables
├── data/           # SQLite database storage
├── src/            # Source code
│   ├── dashboard/  # Streamlit web application
│   ├── scrapers/   # Scraping logic (AmazonScraper, Factory)
│   ├── models.py   # Database models
│   └── tracker.py  # Core tracking logic
├── tests/          # Unit tests with mocked data
└── main.py         # Application entry point (CLI)