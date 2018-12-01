def opened(file):   
    f = open(file, encoding='utf-8')
    s = f.readlines()
    f.close
    text = s.strip("\n")

    return text


def letters(text):
    answer = []
    for line in text:
        if line[i] >= 35:
            print(line)
        else:
            pass
        
    return list_of_lines

def print_list(lines):
    print(lines)

def main():
    a = opened("Extinct_languages.tsv")
    b = letters(a)
    c = printing(b)

if __name__=='__main__':
    main


