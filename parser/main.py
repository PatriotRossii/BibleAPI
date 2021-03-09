import requests

API_SERVER = "https://api.bibleonline.ru"


class Verse:
    def __init__(self, content):
        self.content = content


class Chapter:
    def __init__(self, verses):
        self.verses = verses


class Book:
    def __init__(self, id, locale):
        self.id = id
        self.locale = locale
        self.chapters = []

    def __repr__(self):
        return f"Book({self.id}, \"{self.locale}\")"


class Parser:
    @staticmethod
    def decode(data: str):
        return eval(data.text[1:-2])

    @staticmethod
    def load_books():
        resp = requests.get(f"{API_SERVER}/booklist")
        book_list = Parser.decode(resp.text)

        book_list = [e for e in book_list if "li" in e]
        book_list = [Book(e["li"]["id"], e["li"]["locale"]) for e in book_list]

        return book_list

    @staticmethod
    def load_chapters(book: Book):
        name = book.locale
        for i in range(999):
            resp = requests.get(f"{API_SERVER}/bible?q={name} {i}")
            data = Parser.decode(resp.text)

            if not data:
                break

            verses = [e["v"]["t"] for e in data[1:]]
            book.chapters.append(Chapter(verses))
        return book
