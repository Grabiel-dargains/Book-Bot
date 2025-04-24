def get_book_text(book_name):
    """Path do livro como input, string como output."""
    
    with open(f"./books/{book_name}.txt", "r", encoding='utf-8') as livro:
        leitura = livro.read()
    return leitura

def count(book_str):
        char_count = 0
        for x in book_str:
            char_count += 1
        print (f"This book has {char_count} characters")

def get_num_words(book_str):
    palavras = book_str.split()
    contagem = 0
    for x in palavras:
        contagem += 1
    print(f"{contagem} words found in the book.")

def get_char_count(book_str):
    char_count = {}
    for x in book_str.lower():
        char_count[x] = char_count.get(x, 0) + 1
    return char_count