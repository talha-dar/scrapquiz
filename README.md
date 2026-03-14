# scrapquiz
Project Purpose
The purpose of this project was to create a Python-based web scraper which automatically collects product information from an e-commerce website. The scraper reads through the website’s category structure, navigates through paginated listing pages and subcategories, retrieves product details, and saves the collected data in structured files. This allows the scraped data to be used later for processing or analysis.

Project Setup Using UV
This project was set up using uv, which is utilized for managing Python environments and dependencies. First, a project directory was initialized with uv. A virtual environment was created, then the required packages were added for web scraping and HTML parsing. The codebase was organized into distinct modules such as crawler, parsers, exporters, and utilities to keep the project organized and maintainable.

Installing Dependencies
Dependencies can be installed using uv by running:
uv sync to install all dependencies defined in the project, or
uv pip install -r requirements.txt to manually install the required libraries.

Running the Scraper
The scraper is executed from the project’s root directory by running the main script:
python main.py
The scraper discovers the website’s category structure, visits each listing page, extracts product information, and exports the collected data to files in the data directory, when executed.

Branch Workflow
A simple Git branching workflow was followed. The main branch was used as the stable version of the project, while new features or modifications were developed in separate branches. After testing, these changes were merged back into the main branch to maintain a clean and stable codebase.

Assumptions and Limitations
Some assumptions were made during working. For one, it was assumed that the website structure is consistent, product links show in elements with the same HTML selector, and pagination uses a standard “Next” button.
However, the scraper also contains some limitations. If the website’s HTML structure changes, the selectors used by the scraper perhaps stop working. Moreover, the scraper can not handle advanced anti-scraping mechanisms such as strict rate limiting or CAPTCHAs, and network errors are only minimally handled.
