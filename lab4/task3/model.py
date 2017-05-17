import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists
from sqlalchemy import and_


Base = declarative_base()


class Author(Base):
    __tablename__ = 'Авторы'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='имя')
    country = Column(String, name='страна')
    years = Column(String, name='годы жизни')
    books = relationship('Book', back_populates='author')

    def insert_book(self, book):
        self.books.append(book)

    def __repr__(self):
        return "<Автор(имя='{}', страна='{}', годы жизни='{}')>" \
                .format(self.name, self.country, self.years)


class Book(Base):
    __tablename__ = 'Книги'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('Авторы.id'), name='id автора')
    title = Column(String, name='название')
    pages_count = Column(Integer, name='количество страниц')
    publisher = Column(String, name='издательство')
    publishing_year = Column(Integer, name='год издания')
    author = relationship('Author', back_populates='books')

    def __repr__(self):
        return "<Книга(название='{}', количество страниц='{}', " \
               "издатель='{}', год издания='{}')>" \
               .format(self.title,
                       self.pages_count,
                       self.publisher,
                       self.publishing_year)


class User(Base):
    __tablename__ = 'Пользователи'

    id = Column(Integer, primary_key=True)
    login = Column(String, name='логин')
    password = Column(String, name='пароль')

    def __repr__(self):
        return "<Пользователь(логин='{}', пароль='{}')>" \
               .format(self.login,
                       self.password)


class DB(object):
    def __init__(self, DBNAME):
        self.engine = sqlalchemy.create_engine('sqlite:///' + DBNAME)
        DB.Session = sessionmaker(bind=self.engine)
        self.session = DB.Session()

    def init_tables(self):
        # создаем таблицы в базе на основе всех существующих наследников Base
        Base.metadata.create_all(self.engine)

        # определяю значения по умолчанию с помощью строки
        authors = ("L.N.Tolstoi    |Russia |1828-1910\n"
                   "F.M.Dostoyevsky|Russia |1821-1881\n"
                   "B.Vian         |France |1920-1959\n"
                   "A.Camus        |France |1913-1960\n"
                   "F.Kafka        |Austria|1883-1924")

        books = ("1|War and Peace   |1225|The Russian Messanger|1869\n"
                 "1|Resurrection    |483 |Niva                 |1899\n"
                 "2|The Idiot       |678 |The Russian Messanger|1868\n"
                 "2|The Gambler     |241 |The Moscow Renaisanse|1867\n"
                 "3|The Foam of days|219 |Gallimard            |1947\n"
                 "4|The Stranger    |159 |Hamish Hamilton      |1946\n"
                 "4|The Rebel       |238 |Gallimard            |1951\n"
                 "5|The Trial       |395 |Verlag Die Schmiede  |1925\n"
                 "5|Amerika         |351 |Routledge            |1938")

        # d4d1c9e67f05a7785990dea88020f20a = хеш для пароля `admin`
        users = "admin|d4d1c9e67f05a7785990dea88020f20a"

        # замыкание для заполнения таблицы table_type значениями из
        # str_table по столбцам из field_names
        def fill_table(str_table, table_type, field_names):
            # перебираем строки
            for row in str_table.split('\n'):
                # разбиваем строку на поля
                fields = list(map(str.strip, row.split('|')))

                # строим компаратор
                # с помощью getattr(table_type, field_name)
                # получаем конструкции table_type.field_name
                # наподобие Author.country
                # сравниваем столбцы с соотв. полями
                # для каждого поля и имени столбца
                # делаем and для всех полученных сравнений
                comparator = and_(*[getattr(table_type, field_name) == field
                                    for field_name, field
                                    in zip(field_names, fields)])

                # проверяем, существует ли запись
                # с таким набором значений в таблице
                # если существует, идём дальше
                if (self.session.query(exists()
                                       .where(comparator))
                                .scalar()):
                    continue

                # создаем элемент таблицы
                instance = table_type()
                # заполняем элемент данными
                # setattr(instance, field_name, field) разворачивается
                # в конструкции instance.field_name = field
                # например author.country = 'Russia'
                for field_name, field in zip(field_names, fields):
                    setattr(instance, field_name, field)
                # добавляем элемент в базу
                self.session.add(instance)
                self.session.commit()

        # заполняем таблицы с помощью созданного ранее замыкания
        fill_table(authors, Author, ['name', 'country', 'years'])
        fill_table(books, Book, ['author_id', 'title', 'pages_count',
                                 'publisher', 'publishing_year'])
        fill_table(users, User, ['login', 'password'])

    def read_authors(self):
        return (self.session.query(Author))

    def read_books(self):
        return (self.session.query(Book))

    def read_users(self):
        return (self.session.query(User))

    def is_user_exists(self, login, password):
        return self.session.query(exists()
                                  .where(and_(User.login == login,
                                              User.password == password))) \
                            .scalar()

    def get_author_by_id(self, id):
        return self.read_authors().filter(Author.id == id).first()

    def insert_author(self, author):
        self.session.add(author)
        self.session.commit()

    def insert_book(self, book):
        self.session.add(book)
        self.session.commit()

    def __del__(self):
        self.session.close()
