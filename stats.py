from typing import List, Dict
def count_book_words(book):
    words = book.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    return num_words

def count_chars(text:str):
    counter = {}
    for char in text:
        if char.lower() in counter:
            counter[char.lower()] +=1
        else:
            counter[char.lower()] = 1
    return counter

def sorter(counts:Dict):
    counts_list = []
    for char in counts:
        counts_list.append({"char": char, "num": counts[char]})
    counts_list.sort(reverse = True, key = sort_on)
    return counts_list

def sort_on(items):
    return items["num"]