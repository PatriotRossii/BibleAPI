from lxml import etree, objectify


class TitleInfo:
    def __init__(self, book_title, genre, lang):
        self.book_title = book_title
        self.genre = genre
        self.lang = lang


class DocumentInfo:
    def __init__(self, author: AuthorInfo, src_url, date, version, id):
        self.author = author
        self.src_url = src_url
        self.date = date
        self.version = version
        self.id = id


class Description:
    def __init__(self, title_info: TitleInfo, document_info: DocumentInfo):
        self.title_info = title_info
        self.document_info = document_info


class FB2Parser:
    def __init__(self, path):
        self.path = path
        content = None
        
        with open(path) as file:
            content = file.read()
        
        self.root = objectify.fromstring(
            content
        )

    def extract_description(self):
        return self.root.description
        
    def extract_title_info(self, description):
        return description.title-info
    