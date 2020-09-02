import re

def word_count(s):
    string_array = s.lower().split() #just need to remove the characters 
    d = {i:string_array.count(i) for i in string_array}
    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))