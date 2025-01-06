# first class
class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, book_name, author, number_of_pages, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved


list_of_books = [
    Book('Мёртвые души', 'Н.В. Гоголь', 450, '7610984310', False),
    Book('Руслан и Людмила', 'А.С. Пушкин', 129, '7610984132', False),
    Book('Белая гвардия', 'М.А. Булгаков', 620, '7610984321', False),
    Book('Ревизор', 'Н.В. Гоголь', 72, '7610984270', False),
    Book('Бедные люди', 'Ф.М. Достоевский', 180, '7610984002', True)
]

for book in list_of_books:
    if book.reserved:
        print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
              f'материал: {book.page_material}, зарезервирована')
        continue
    print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
          f'материал: {book.page_material}')

print('-' * 100)


# second class
class SchoolBook(Book):

    def __init__(self, book_name, author, number_of_pages, isbn, reserved, subject, school_class, presence_of_tasks):
        super().__init__(book_name, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.presence_of_tasks = presence_of_tasks


list_of_schoolbooks = [
    SchoolBook('Математика 8кл', 'А.В. Перов', 300, '7610933330', False,
               'Математика', 9, True),
    SchoolBook('География Родины', 'М.С. Калинина', 180, '0010933330',
               False, 'География', 8, False),
    SchoolBook('Химия 10кл', 'К.С. Жаров', 269, '7693323330', True,
               'Химия', 10, True)
]

for book in list_of_schoolbooks:
    if book.reserved:
        print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
              f'предмет: {book.subject}, класс: {book.school_class}, зарезервирована')
        continue
    print(f'Название: {book.book_name}, Автор: {book.author}, страниц: {book.number_of_pages}, '
          f'предмет: {book.subject}, класс: {book.school_class}')
