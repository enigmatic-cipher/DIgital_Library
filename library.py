class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendBooksDict = {}

    def displayBooks(self):
        print(f'List of Books in Library: {self.name}')
        for book in self.booksList:
            print(book)

    def lendBooks(self, book, user):
        if book not in self.lendBooksDict.keys():
            self.lendBooksDict.update({book:user})
            print(f'Books in library has been updated.'
                  f'This book is now assigned to you')
        else:
            print(f'Book is already assigned to {self.lendBooksDict[book:user]}')

    def addBooks(self, book):
        self.booksList.append(book)

    def returnBooks(self, book):
        self.lendBooksDict.pop(book)

if __name__ == '__main__':
    cipher = Library (['1) Clean Code: A Handbook of Agile Software Craftsmanship',
                       '2) Design Patterns: Elements of Reusable Object-Oriented Software',
                       '3) Patterns of Enterprise Application Architecture',
                       '4) Enterprise Integration Patterns',
                       '5) Code Complete: A Practical Handbook of Software Construction',
                       '6) Refactoring: Improving the Design of Existing Code',
                       '7) Soft Skills: The Software Developer’s Life Manual',
                       '8) User Stories Applied: For Agile Software Development',
                       '9) Peopleware: Productive Projects and Teams',
                       '10) The Pragmatic Programmer'],'CipherLibrary')

    while(True):
        print('Welcome to the Digital Library.\n Enter choice to proceed')
        print('Press 1: To Display List of Books in Library')
        print('Press 2: To Lend Book from Library')
        print('Press 3: To Add Book in Library')
        print('Press 4: To Return Book to Library')
        user_choice = int(input())

        if user_choice == 1:
            cipher.displayBooks()

        elif user_choice == 2:
            book = input('Enter the book name: ')
            user = input('Enter your name: ')
            cipher.lendBooks(user, book)

        elif user_choice == 3:
            book = input('Enter thr book name to add: ')
            cipher.addBooks(book)

        elif user_choice == 4:
            book = input('Enter the name of book to return: ')
            cipher.returnBooks(book)

        else:
            print('Invalid Input')

        print('Press q to quit and c to continue')
        choice = ''
        while(choice != 'q' and choice != 'c'):
                choice = input()
                if choice == 'q':
                    exit()
                elif choice == 'c':
                    continue