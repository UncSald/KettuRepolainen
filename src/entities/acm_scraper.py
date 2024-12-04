from bs4 import BeautifulSoup

def __parse_article_authors(soup: BeautifulSoup):
    authors = []
    
    for author in soup.select('.authors a'):
        first_name = author.find('span', property="givenName").get_text()
        last_name = author.find('span', property="familyName").get_text()

        authors.append(f"{last_name}, {first_name}")

    return ' and '.join(authors) if len(authors) > 1 else authors[0]

def __parse_article_published_date(soup: BeautifulSoup, element: str):
    text = soup.select_one(element).get_text()
    parts = text.split(' ')
    
    return {
        'day': int(parts[0]),
        'month': parts[1],
        'year': int(parts[2]),
    }

def __parse_article_published_date(soup: BeautifulSoup):
    text = soup.select_one('.core-date-published').get_text()
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

    date_data = __parse_article_published_date(soup)

    article_data = {
        'author': __parse_article_authors(soup),
        'title': soup.select_one('.core-container h1').get_text(),
        'journal': soup.select_one('.core-enumeration span[property="name"]').get_text(),
        'year': date_data['year'],
        'volume': int(soup.find('span', property='volumeNumber').get_text()),
        'number': __parse_article_number(soup),
        'pages': __parse_article_pages(soup),
        'month': date_data['month'],
        'type': "article"
    }

    return article_data


def __parse_book_published_date(soup: BeautifulSoup):
    text = soup.select_one('.dot-separator').get_text()
    parts = text.split(' ')
    
    return {
        'month': parts[0],
        'year': int(parts[1]),
    }

def __parse_book_editors_or_authors(soup: BeautifulSoup):
    element = soup.select_one('.item-meta-row')
    author_type = soup.select_one('.item-meta-row li[class="label"]').get_text()
    
    author_elements = element.find_all('a')

    authors = []

    for a_element in author_elements:
        first_name, last_name = a_element['title'].split(' ')
        authors.append(f"{last_name}, {first_name}")

    concatinated = ' and '.join(authors) if len(authors) > 1 else authors[0]

    if  'editor' in author_type.lower():
        return ('e', concatinated)
    
    return ('a', concatinated)

def __parse_book_publisher(soup: BeautifulSoup):
    div = soup.select_one('.published-info')

    return div.find_next('li').get_text()

def __parse_book_title(soup: BeautifulSoup):
    div = soup.select_one('.colored-block__title')

    return div.find_next('span').get_text()

def scrape_book(html: str | bytes):
    # parsed tree object of page html
    soup = BeautifulSoup(html,'html.parser')

    date_data = __parse_book_published_date(soup)
    author_type, authors = __parse_book_editors_or_authors(soup)

    book_data = {
        'title': __parse_book_title(soup),
        'publisher': __parse_book_publisher(soup),
        'year': date_data['year'],
        'month': date_data['month'],
        'type': "book"
    }

    if author_type == 'e':
        book_data['editor'] = authors
    else:
        book_data['author'] = authors

    return book_data
