
class Publication:
    __title = ""
    __author = ""

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return f"Title: {self.__title}"

    def get_author(self):
        return f"Author: {self.__author}"


    def set_title(self, title):
        self.__title = title


    def set_author(self, author):
        self.__author = author


    def display_info(self):
        print(f"Title: {self.__title}\nAuthor: {self.__author}")


    
class Book(Publication):
    __number_of_pages = 0

    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_pages

    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_of_pages}"

    def set_number_of_pages(self, number_pages):
        if number_pages>0:
            self.__number_of_pages = number_pages

        else:
            print("The number of pages must be positive")
        

class Magazine(Publication):
    __issue_number = 0

    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return f"Issue number: {self.__issue_number}"

    def set_issue_number(self, issue_number):
        if issue_number>0:
            self.__issue_number = issue_number
        else:
            print("The number of pages must be positive")



pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
