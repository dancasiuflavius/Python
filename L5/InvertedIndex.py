def inverted_index(documents):
    index = {}
    for i, doc in enumerate(documents):
        words = doc.lower().split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(i)
    return index


def main():
    documents = [
        "pisica a stat pe covor",
        "cainele a stat în ceață",
        "pisica și cainele s-au jucat împreună"
    ]
    index = inverted_index(documents)
    for word, doc_set in index.items():
        print(f"'{word}': {doc_set}")


if __name__ == "__main__":
    main()
