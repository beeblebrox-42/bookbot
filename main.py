def main():
    
    book_path = "books/frankenstein.txt"

    text = get_text(book_path)
    
    words = ()

    count_words = count_the_words(text)

    print(f"{count_words} words found in the document") 

    
def count_the_words(text):
    words = text.split()
    words_n = 0
    for i in range(len(words)):
        words_n += 1
    return words_n

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



        

main()