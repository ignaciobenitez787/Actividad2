first_word = input("Ingrese la primera palabra:")
second_word = input("Ingrese la segunda palabra:")
if sorted(first_word.lower()) == sorted(second_word.lower()) and first_word != second_word:
    print("Son anagramas.")
else:
    print("No son anagramas.")