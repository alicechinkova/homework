def open_file(file):
    with open(file, encoding = 'utf-8') as f:
        s = f.read()
        text = s.strip()

    return text

def find(text):
    answer = 0 
    for word in text:
        if word == "Critically endangered":
            answer += 1
        else:
            pass
        break
    return answer

def print_answer(answer):
    print(answer)

def main():
    a = open("Extinct_languages.tsv")
    b = find (a)
    print_answer(b)
            
                
