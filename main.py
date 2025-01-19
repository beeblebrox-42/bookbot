def main():

    characters_list = []
    
    book_path = "books/frankenstein.txt"

    text = get_text(book_path)
    
    words = ()

    count_words = count_the_words(text)

    characters_n = count_the_characters(text)
        
    x = characters_n.items()

    for (x, y) in characters_n.items():
        if x.isalpha() == True :
            print(x, y)
            characters_list.append({"name" : x, "num" : y})
    
    

    print(characters_list)
    characters_list.sort(reverse=True, key=sort_it)
    print(characters_list)

    

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    for character in characters_list:
        print(f"{character["name"]} was found {character["num"]} times") 
    print("--- End report ---") 


def sort_it(list):
    return list["num"]


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