class Book:
    """Book."""

    def __init__(
            self,
            name: str,
            genre: str,
            desc: str
    ) -> None:
        self.name = name
        self.genre = genre
        self.desc = desc


class AddBook(Book):
    """Adding Book."""
    
    def add_book(self) -> None:
        add = {
            "name": self.name,
            "genre": self.genre,
            "description": self.desc
        }

        return add


all_books: list[AddBook] = [
    AddBook(
        "Michael Jonson",
        "Biography",
        "It's biography about interesting person whose name is Michael"
    ),
    AddBook(
        "Michael Roberton",
        "Fantazy",
        "It's Fantazy about interesting person whose name is Michael"
    ),
    AddBook(
        "Michael Windon",
        "Adventure",
        "It's Adventure about interesting person whose name is Michael"
    ),
    AddBook(
        "Michael Alexton",
        "Horror",
        "It's Horror about interesting person whose name is Michael"
    ),
    AddBook(
        "1984",
        "Fantazy",
        "Своеобразный антипод второй великой антиутопии XX века - О дивный новый мир Олдоса Хаксли."
    ),
    AddBook(
        "Master and Margarita",
        "Horror",
        "Один из самых загадочных и удивительных романов XX века. «Мастер и Маргарита» – визитная карточка Михаила Булгакова. "
    ),
    AddBook(
        "Шантарам",
        "Adventure",
        "Представляем читателю один из самых поразительных романов начала XXI века (в 2015 году получивший долгожданное продолжение – «Тень горы»)."
    ),
    AddBook(
        "Три товарища",
        "Proza",
        "Трое друзей - Робби, отчаянный автогонщик Кестер и последний романтик Ленц прошли Первую мировую войну. "
    ),
    AddBook(
        "Цветы для Элджернона",
        "Fantazy",
        "Сорок лет назад это считалось фантастикой. Сорок лет назад это читалось как фантастика."
    ),
    AddBook(
        "Портрет Дориана Грея",
        "Fantazy",
        "«Портрет Дориана Грея» – одно из величайших произведений последних полутора столетий, роман"
    ),
    AddBook(
        "Маленький принц",
        "Proza",
        "«Маленький принц» — аллегорическая повесть, наиболее известное произведение Антуана де Сент-Экзюпери."
    ),
    AddBook(
        "Над пропастью во ржи",
        "Proza",
        "Писатель-классик, писатель-загадка, на пике своей карьеры объявивший об уходе из литературы и поселившийся вдали от мирских соблазнов в глухой"
    ),
    AddBook(
        "Вино из одуванчиков",
        "Fantazy",
        "Войдите в светлый мир двенадцатилетнего мальчика и проживите с ним одно лето, наполненное событиями радостными и печальными, загадочными и тревожными"
    ),
    AddBook(
        "Атлант расправил плечи",
        "Proza",
        "Айн Рэнд – наша бывшая соотечественница, ставшая крупнейшей американской писательницей."
    ),
    AddBook(
        "Анна Каренина",
        "Proza",
        "Гениальный роман Льва Толстого, который не оставляет равнодушным никого, кто его прочел."
    ),
    AddBook(
        "Убить пересмешника",
        "Proza",
        "О книге <<Убить пересмешника>> (1960 г.) - пронзительная история семьи, живущей в вымышленном маленьком городке на юге Америки, в штате Алабама. "
    ),
    AddBook(
        "Преступление и наказание",
        "Proza",
        "Ф.М.Достоевский - один из тех немногих писателей, которые повлияли на умы не только современников, но и потомков."
    ),
    AddBook(
        "Сто лет одиночества",
        "Proza",
        "Странная, поэтичная, причудливая история города Макондо, затерянного где-то в джунглях, - от сотворения до упадка. "
    ),
    AddBook(
        "Библия. Синодальный перевод",
        "Biblia",
        "Библия, священная книга христиан, является книгой на все времена. "
    ),
    AddBook(
        "Двенадцать стульев",
        "Proza",
        "Знаменитый роман-фельетон И.Ильфа и Е.Петрова «Двенадцать стульев» впервые был опубликован в 1928 году, а сегодня его называют в числе культовых."
    ),
]
books_json: list = []

def adding_books_to_json(
        all_b: list[AddBook], 
        json: list[dict]
    ) -> list:
        for book in all_b:
            json.append(book.add_book())
        return json

books_json = \
    adding_books_to_json(
        all_books,
        books_json)
