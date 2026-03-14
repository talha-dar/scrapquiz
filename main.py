from scraper.crawler import Crawler
from scraper.parsers import parse_product_details
from scraper.exporters import export_data
from scraper.utils import resolve_url

def main():
    bot = Crawler()
    collected_items = []
    visited_links = set()

    print("--- Beginning Structure Scan ---")
    site_map = bot.discover_structure()

    for section in site_map:
        page_url = section['url']
        page_index = 1

        while page_url:
            print(f"Processing: {section['subcategory']} | Page {page_index}")
            page_soup = bot.get_soup(page_url)

            # Locate product links from the listing page
            links = page_soup.select("a.title")

            for element in links:
                product_url = resolve_url(page_url, element['href'])

                if product_url not in visited_links:
                    product_page = bot.get_soup(product_url)

                    if product_page:
                        product_data = parse_product_details(
                            product_page,
                            product_url,
                            section['category'],
                            section['subcategory'],
                            page_index
                        )

                        collected_items.append(product_data)
                        visited_links.add(product_url)

            # Check if a next page exists
            next_page = page_soup.select_one("ul.pagination li a[aria-label='Next »']")

            if next_page:
                page_url = resolve_url(page_url, next_page['href'])
                page_index += 1
            else:
                page_url = None

    export_data(collected_items)
    print("--- Scraping Finished. Output saved in data folder. ---")


if __name__ == "__main__":
    main()