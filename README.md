# indeed-job-webscraper

About the project
--
Stay ontop of the drop with www.nike.com SNKRS launch web scraper for all available countries. Scrape upcoming product details:

- `audience_suggestedGender`: Product suggested gender male/female/unisex.
- `brand_name`: Product brand name Jordan, Nike Sportswear etc.
- `category`: Product categories.
- `color`: Product color.
- `description`: Product description.
- `image`: Product image link.
- `name`: Product name.
- `offers_url`: Product url.
- `offers_price`: Product price in local currency.
- `offers_priceCurrency`: Local currency.
- `offers_seller_name`: Product seller.
- `releaseDate`: Release datetime in iso format.
- `sku`: Product SKU.

Note: if more additional data fields required e.g. product sizes, refer to the Support section below.

<img width="1440" alt="Screen Shot 2021-11-11 at 9 12 36 am" src="https://user-images.githubusercontent.com/61095925/141202388-47905df2-aa2e-4ff9-a458-285bca4b9168.png">


Installation
--

#### Install python 3.8 ####
    $ https://www.python.org/downloads/release/python-387/

#### Clone repo ####

    $ git clone https://github.com/jcoleiro/indeed-job-webscraper.git

#### Create virtual environment (Recommended) ####

macOS

    $ python3 -m venv venv

Windows

    $ c:\>c:\Python35\python -m venv venv

#### Start virtual environment (Recommended) ####

macOS

    $ source venv/bin/activate

Windows

    $ source venv/Scripts/activate

#### Install python requirements ####

    $ pip install -r requirements.txt

Usage
--

#### Update COUNTRY in scraper.py ####

    COUNTRY: str = 'United States'

#### Execute scraper.py ####

    $ python scraper.py

#### Output ####

All filed out output to the folder `/data` in csv and json format.

<img width="870" alt="Screen Shot 2021-11-11 at 9 16 41 am" src="https://user-images.githubusercontent.com/61095925/141202798-fd68147c-37ef-45d3-875c-6af6fba079a7.png">

![Screen Shot 2021-11-11 at 9 16 59 am](https://user-images.githubusercontent.com/61095925/141202807-ce8b6b55-5bc3-4daa-8f61-e1a84bf9ec8c.png)

Support
--

[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Ultimate-Facebook-Scraper.svg?style=flat&label=Issues&maxAge=2592000)](https://github.com/jcoleiro/nike-snkrs-launch-webscraper/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

Alternatively, you can contact me at joshuacoleiro@gmail.com.

Licence
--
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](LICENSE)

Copyright (c) 2021-present, jcoleiro, Joshua Coleiro

