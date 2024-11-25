class Reference:
    def __init__(self, reference_id, author, title, journal, year, url):
        self.reference_id = reference_id
        self.author = author
        self.title = title
        self.journal = journal
        self.year = year
        self.url = url

    def __str__(self):
        return f"{self.author}, {self.title}, {self.journal}, {self.year}, {self.url}"
