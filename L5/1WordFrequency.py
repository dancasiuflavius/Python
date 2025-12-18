import string


def word_frequency(text):
    text = text.lower()

    for punct in string.punctuation:
        text = text.replace(punct, "")

    cuvinte = text.split()

    frecventa = {}
    for cuvant in cuvinte:
        if cuvant in frecventa:
            frecventa[cuvant] += 1
        else:
            frecventa[cuvant] = 1

    return frecventa


def main():
    text = input("Introduceti un text: ")
    rezultat = word_frequency(text)
    print(rezultat)

if __name__ == "__main__":
    main()