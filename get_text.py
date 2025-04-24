def get_book_text(arquivo):
    """Path do livro como input, string como output."""
    with open(arquivo, "r", encoding='utf-8') as livro:
        leitura = livro.read()
    return leitura

def count(book_str):
        char_count = 0
        for x in book_str:
            char_count += 1
        print (f"This book has {char_count} characters")