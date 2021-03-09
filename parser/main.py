import requests
import pickle
import time

API_SERVER = "https://api.bibleonline.ru"


class Verse:
    def __init__(self, index, content):
        self.index = index
        self.content = content

    def __repr__(self):
        return f"Verse({self.index}, \"{self.content}\")"


class Chapter:
    def __init__(self, index, verses):
        self.index = index
        self.verses = verses

    def __repr__(self):
        return f"Chapter({self.index}, \"{self.verses}\")"


class Book:
    def __init__(self, index, locale):
        self.index = index
        self.locale = locale
        self.chapters = {}

    def __repr__(self):
        return f"Book({self.index}, \"{self.locale}\")"


class Parser:
    @staticmethod
    def decode(data: str):
        return eval(data[1:-2])

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
        for i in range(1, 999):
            print(f"Пытаемся получить информацию о {name} {i}")
            resp = requests.get(f"{API_SERVER}/bible?q={name} {i}")
            data = Parser.decode(resp.text)

            if not data:
                print(f"В главе {i} книги {name} стихи не обнаружены. Останавливаем поиск.")
                break

            verses = {e["v"]["n"]: Verse(e["v"]["n"], e["v"]["t"]) for e in data[1:]}
            book.chapters[i] = Chapter(i, verses)
            print(f"В книгу {name} загружена глава {i}, состоящая из {len(verses)} стихов.")
            time.sleep(0.05)
        print(f"Загрузка книги {name} завершена. Она содержит {len(book.chapters)} глав")
        time.sleep(1)
        return book

    @staticmethod
    def load():
        books = [Parser.load_chapters(e) for e in Parser.load_books()]
        print("Загрузка книг завершена")
        return books

    @staticmethod
    def save(books):
        savings = {}
        for book in books:
            savings[book.locale] = book
        with open("books.dump", "wb") as file:
            pickle.dump(savings, file)
        print("Сохранение успешно завершено")


Parser.save(Parser.load())
