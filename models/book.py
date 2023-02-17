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

    def __init__(self) -> None:
        self.add = {}

    def add_book(self) -> None:
        self.add = {
            "name": super().name,
            "genre": super().genre,
            "description": super().desc
        }

        return self.add


all_books = [
    AddBook(
        "Michael Jonson",
        "Biography",
        "It's biography about interesting person whose name is Michael"
    ),
    AddBook(
        "Michael Roberton",
        "Biography",
        "It's biography about interesting person whose name is Michael"
    ),
    AddBook(
        "Michael Windon",
        "Biography",
        "It's biography about interesting person whose name is Michael"
    )
]
