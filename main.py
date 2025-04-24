
def get_book_text(arquivo):
    """Path do livro como input, string como output."""
    with open(arquivo, "r", encoding='utf-8') as livro:
        leitura = livro.read()
    return leitura

def __main__():
    book_name = input("Type in file name: \n")
    book_str = get_book_text(f"./books/{book_name}.txt")
    print(book_str)

    def count():
        char_count = 0
        for x in book_str:
            char_count += 1
        print (f"This book has {char_count} characters")
    
    count()

    


__main__()
