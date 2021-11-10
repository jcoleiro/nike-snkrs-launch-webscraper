"""Webscraper for nike.com SNKRS upcoming launch products.

    Usage:
        Update COUNTRY constant to local country.
        Execute script: $ python scraper.py
"""
import csv
import json
from typing import Any, Dict, List, Optional, Union

import requests
from bs4 import BeautifulSoup
from bs4 import element

### UPDATE COUNTRY ###

COUNTRY: str = 'United States'

######################

DOMAIN: str = 'https://www.nike.com/'

def flatten_dict(obj: Dict[str, Any], parent_key=None) -> Dict[str, Any]:
    """Recurrsive function to flatten nested dictionary.

    Args:
        obj (Dict[str, Any]): Nested dictionary.
        parent_key ([type], optional): Parent key of nested dicted. Defaults to None.

    Returns:
        Dict[str, Any]: Flat dictionary with nested keys underscore seperate with parent_key.
    """
    flat: Dict[str, Any] = {}
    for key, value in obj.items():
        new_key = f'{parent_key}_{key}' if parent_key is not None else key
        items = flatten_dict(value, new_key) if isinstance(value, dict) else {new_key: value}
        flat = {
            **flat,
            **items,
        }
    return flat

def main():
    """Main function to scrape Nike SNKRS upcoming products"""
    # Get country domain
    response: requests.Response = requests.get(DOMAIN)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    country_menu_item: Optional[Union[element.Tag, element.NavigableString]] = soup.find(
        'a',
        attrs={
            'class': 'hf-language-menu-item',
            'title': COUNTRY.title(),
        },
    )

    if country_menu_item is None:
        print('Invalid country.')
        return

    country_domain: str = DOMAIN\
        if COUNTRY == 'United States'\
        else country_menu_item.get('href', DOMAIN)

    # Get product links list
    response: requests.Response = requests.get(f'{country_domain}launch?s=upcoming')
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    product_hrefs: List[str] = [a.get('href') for a in soup.find_all('a', attrs={'class': 'card-link'})]

    products = []
    # Get product data
    for product_href in product_hrefs:
        response: requests.Response = requests.get(f'{DOMAIN}{product_href[1:]}')
        soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
        script: Optional[Union[element.Tag, element.NavigableString]] = soup.find('script', attrs={'type': 'application/ld+json'})
        if script is None:
            continue
        content: Dict[str, Any] = json.loads(script.text)
        flat_content: Dict[str, Any] = flatten_dict(content)
        products.append({key: value for key, value in flat_content.items() if '@' not in key})

    # Write products to csv files
    with open('data/products.csv', 'w') as csv_file:
        fieldnames: List[str] = list(products[0].keys() if products else [])
        dict_writer: csv.DictWriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(products)
        print('Saved to data/products.csv')

    # Write products to json file
    with open('data/products.json', 'w') as json_file:
        json.dump(products, json_file)
        print('Saved to data/products.json')

if __name__ == "__main__":
    main()
