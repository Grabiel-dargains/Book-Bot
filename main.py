from get_text import count, get_book_text

def __main__():
    book_name = input("Type in file name: \n")
    book_str = get_book_text(f"./books/{book_name}.txt")
    print(book_str)
    
    count(book_str)

__main__()
