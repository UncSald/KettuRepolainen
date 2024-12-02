from bs4 import BeautifulSoup

def __parse_article_authors(soup: BeautifulSoup):
    authors = []
    
    for author in soup.select('.authors a'):
        first_name = author.find('span', property="givenName").get_text()
        last_name = author.find('span', property="familyName").get_text()

        authors.append(f"{last_name}, {first_name}")

    return ' and '.join(authors) if len(authors) > 1 else authors[0]

def __parse_published_date(soup: BeautifulSoup, element: str):
    text = soup.select_one(element).get_text()
    parts = text.split(' ')
    
    return {
        'day': int(parts[0]),
        'month': parts[1],
        'year': int(parts[2]),
    }

def __parse_article_pages(soup: BeautifulSoup):
    start = soup.find('span', property='pageStart').get_text()
    end = soup.find('span', property='pageEnd').get_text()

    return f"{start}-{end}"

def __parse_article_number(soup):
    element = soup.find('span', property='issueNumber')
    if not element:
        return None

    return int(element.get_text())

def scrape_article(html: str | bytes):
    # parsed tree object of page html
    soup = BeautifulSoup(html,'html.parser')

    date_data = __parse_published_date(soup=soup, element='.core-date-published')

    article_data = {
        'author': __parse_article_authors(soup),
        'title': soup.select_one('.core-container h1').get_text(),
        'journal': soup.select_one('.core-enumeration span[property="name"]').get_text(),
        'year': date_data['year'],
        'volume': int(soup.find('span', property='volumeNumber').get_text()),
        'number': __parse_article_number(soup),
        'pages': __parse_article_pages(soup),
        'month': date_data['month']
    }

    return article_data
