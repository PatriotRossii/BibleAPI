from lxml import etree, objectify


class TitleInfo:
    def __init__(self, book_title: str, genre: str, lang: str):
        self.book_title = book_title
        self.genre = genre
        self.lang = lang
    
    @staticmethod
    def parse(description):
        return TitleInfo(description.book-title.text, description.genre.text, description.lang.text)


class Author:
    def __init__(self, nickname, home_page, email):
        self.nickname = nickname
        self.home_page = home_page
        self.email = email
    
    @staticmethod
    def parse(document_info):
        author = document_info.author
        return Author(author.nickname.text, author.home-page.text, author.email.text)


class DocumentInfo:
    def __init__(self, author: Author, src_url: str, date: str, version: str, id: str):
        self.author = author
        self.src_url = src_url
        self.date = date
        self.version = version
        self.id = id
    
    @staticmethod
    def parse(description):
        document_info = description.document-info
        return DocumentInfo(
            Author.parse(document_info),
            document_info.src_url.text,
            document_info.date.text
            document_info.version.text
            document_info.id.text
        )


class Description:
    def __init__(self, title_info: TitleInfo, document_info: DocumentInfo):
        self.title_info = title_info
        self.document_info = document_info
    
    @staticmethod
    def parse(root):
        description = root.description
        return Description(
            TitleInfo.parse(description),
            DocumentInfo.parse(description)
        )
    

class Section:
    def __init__(self, title: str, content):
        self.title = title
        self.content = content


class Body:
    def __init__(self, title: str, sections: Section):
        self.title = title
        self.sections = sections


class FictionBook:
    def __init__(self, description: Description, body: Body):
        self.description = description
        self.body = body


class FB2Parser:
    def __init__(self, path):
        self.path = path
        content = None
        
        with open(path) as file:
            content = file.read()
        
        self.root = objectify.fromstring(
            content
        )

    def parse_description(self):
        return self.root.description
        
    def extract_title_info(self, description):
        return description.title-info
    