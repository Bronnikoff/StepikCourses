from solution3 import *

class AdvancedPerson(Person):
    """ класс - продвинутый читатель """
    def search(self, book, chapter):
        """возвращает номер страницы chapter из книги book"""
        try:
            return book.search(chapter)
        except AttributeError:
            raise NotExistingExtensionError

    def read(self, book, page):
        """ продвинутое чтение из книги """
        if isinstance(page, str):
            page = self.search(book, page)
        return super().read(book, page)


    def write(self, book, page, text):
        """ продвинутая запись в книгу """
        if isinstance(page, str):
            page = self.search(book, page)
        super().write(book, page, text)


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    def __init__(self, author, year, title, content=None, table=None):
        super().__init__(author, year, title, content)
        self.table = table or {}

    def search(self, chapter):
        """поиск номера страницы по оглавлению"""
        if chapter in self.table:
            return self.table[chapter]
        raise PageNotFoundError

    def add_chapter(self, chapter, page):
        """добавление главы в оглавление"""
        self.table[chapter] = page

    def remove_chapter(self, chapter):
        """удаление главы из оглавления"""
        if chapter in self.table:
            del self.table[chapter]
        else:
            raise PageNotFoundError
        