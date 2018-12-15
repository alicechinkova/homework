def text(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text

def clear_text(text):
    text = text.lower()
    text = text.split()
    for i, word in enumerate(text):
        text[i] = word.strip('!"#$%&\'-()*+,./:;<=>?@[\\]^_`{|}~«»—1234567890')
    return text

def main():
    a = text('book.txt')
    b = clear_text(a)
    print(b)

if __name__ == '__main__':
    main()
