import get_text as gt

def __main__():
    
    book_name = input("Type in file name: \n")
    book_str = gt.get_book_text(book_name)
    print (book_str)

    gt.count(book_str)
    gt.get_num_words(book_str)

    contagem_caracteres = gt.get_char_count(book_str)
    print (contagem_caracteres)

    gt.report_dict(book_str)
    

__main__()
