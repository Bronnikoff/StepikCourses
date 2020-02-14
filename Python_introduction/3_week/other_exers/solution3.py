from solution2 import NotExistingExtensionError, TooLongTextError
from solution2 import PageNotFoundError, PermissionDeniedError

class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content = None):
        """конструктор"""
        super().__init__(title, content)
        self.year = year
        self.author = author
        self.bookmark = dict()

    def read(self, page):
        """возвращает страницу"""
        if 0 <= page < self.size:
            return self.content[page]
        raise PageNotFoundError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        if 0 <= page < self.size:
            self.bookmark[person] = page
        else:
            raise PageNotFoundError

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person in self.bookmark:
            return self.bookmark[person]
        raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        if person in self.bookmark:
            del self.bookmark[person]
        else:
            raise PageNotFoundError


    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size = 12, max_sign = 2000, content = None):
        """конструктор"""
        if content is None:
            content = ["" for _ in range(12)]
        super().__init__(title, content)
        self.max_sign = max_sign

    def read(self, page):
        """возвращает страницу с номером page"""
        if 0 <= page < self.size:
            return self.content[page]
        raise PageNotFoundError

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if 0 <= page < self.size:
            if len(text) + len(self.content[page]) > self.max_sign:
                raise TooLongTextError
            self.content[page] += text
        else:
            raise PageNotFoundError


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        try:
            book.set_bookmark(self, page)
        except AttributeError:
            raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        try:
            return book.get_bookmark(self)
        except AttributeError:
            raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        try:
            book.del_bookmark(self)
        except AttributeError:
            raise NotExistingExtensionError
