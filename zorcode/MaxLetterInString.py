"""
Bir jolda eng kop kaitalangan aripti shygaryngyz

Misal uchun: "Hello World" -> l
"""
def max_letter_in_string(string):
    string = string.lower()
    max_letter = string[0]
    max_count = 0
    for letter in string:
        if string.count(letter) > max_count:
            max_count = string.count(letter)
            max_letter = letter
    return max_letter