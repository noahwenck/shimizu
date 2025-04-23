from bs4 import BeautifulSoup
from datetime import datetime
from film import Film
import requests

NETFLIX_URL = "https://www.netflix.com/tudum/articles/whats-leaving-netflix"
DATE_HEADER_CLASS = "css-1i31ble"
DATA_DIV_CLASSES = ["css-15bwy6z", "eohwfup4"]

def extract_expiring_netflix():
    """
    Extracts the films that are expiring from Netflix.
    """
    netflix_text = requests.get(NETFLIX_URL).text
    netflix_soup = BeautifulSoup(netflix_text, 'html.parser')

    # This article saves dates and films leaving on that date in h3 tags
    headers = netflix_soup.find_all("h3")

    expiring_films = []
    current_expiration_date = None
    for header in headers:
        if header["class"] == [DATE_HEADER_CLASS]:
            raw_date = header.text[8:] + ", " + str(datetime.now().year)
            current_expiration_date = datetime.strptime(raw_date, "%B %d, %Y").date()
        else:
            film_title = header.text

            # Noticed issue with a single extra empty h3 tag, may have to add further checks with monthly updates to site
            if film_title is not None and film_title.strip() != "":
                # This data contains runtime (xH xxM format), MPAA rating, and year (can be null if not available)
                raw_data = header.find_next("div", class_=DATA_DIV_CLASSES).text.split("\xa0")
                filtered_data = [data for data in raw_data if data] # Remove empty strings

                film_year = filtered_data[2] if len(filtered_data) > 2 else None

                film = Film(film_title, film_year, current_expiration_date, "NETFLIX")
                expiring_films.append(film)

    return expiring_films
