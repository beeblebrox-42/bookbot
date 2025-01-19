def main():

    
    
    book_path = "books/frankenstein.txt"

    text = get_text(book_path)
    
    words = ()

    count_words = count_the_words(text)

    characters_n = count_the_characters(text)
        
    x = characters_n.items()
    

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print(f"{x}") 
    print("--- End report ---") 

def count_the_characters(text):
    characters = {}
    for i in text:
            lower_i = i.lower()
            if lower_i in characters:
                characters[lower_i] += 1
            else:
                characters[lower_i] = 1
    return characters

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