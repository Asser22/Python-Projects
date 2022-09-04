def translate(str):
    translation = ""
    for letter in str:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
