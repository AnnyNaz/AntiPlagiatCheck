from tkinter import *
from tkinter.messagebox import *
import re, math
from collections import Counter
from nltk import sent_tokenize
WORD = re.compile(r'\w+')
res = "";
main_color = 'white'
additional_color = 'coral'
text_color = 'black'
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
def compareStrings( i, j, words1, words2, num, a):
    global res 
    k = 0
    m = i;
    n = j;
    while(m<len(words1) and n<len(words2) and get_cosine(text_to_vector(words1[m]), text_to_vector(words2[n]))>0.5):
        
        k+=1
        m+=1
        n+=1
    if (k<num):
        return 0
    else:
        #print(k)
        for tr in range (i, m):
             #print(words1[tr])
             if (tr in a):
                 return 
             a.add(tr)
        print(words1[i:m])
        res = res + '_' + (''.join(words1[i:m]))
        return k;
def check_plagiat(text1, text2, num, a):
    words1 = text1
    words2 = text2
    result = 0;
    i = 0
    while(i<len(words1)):
        j = 0
        while(j<len(words2)):
            compareStrings( i, j,words1, words2, num, a)
            j = j + 1
        i = i + 1
    return len(words1)

"""text1 = 'He won the election.  Hello. It is amazing. Ze won election. He is happy. It is nice'
text2 = 'Wow I couldn`t think about it. He is so lucky. It is good. He won election. We will have a new president'
sentence = "My friend holds a Msc. in Computer Science."
a1 = sent_tokenize(text1)
a2 = sent_tokenize(text2)
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
the_longest_consequent_plagiat = 0
plagiat = []

cosine = get_cosine(vector1, vector2)

print ('Cosine:', cosine)
plag = set()
lab2(a1, a2, 2, plag)
print(res)"""





def show_answer():
    global res
    plag = set()
    res = ""
    check_plagiat(sent_tokenize(num1.get()), sent_tokenize(num2.get()), 2, plag) 
    blank.insert(0, res)


main = Tk()
main.title('Антиплагіат')
main.geometry("800x400")
main.iconbitmap(r'1.ico')
main.configure(bg=main_color)

Label(main, text = "Введіть Ваш текст", bg=main_color, foreground=text_color).grid(row=0)
Label(main, text = "Введіть текст для провірки на плагіат", bg=main_color, foreground=text_color).grid(row=1)
Label(main, text = "Знайдено наступні повторення", bg=main_color, foreground=text_color).grid(row=2)


num1 = Entry(main)
num2 = Entry(main)
blank = Entry(main)


num1.grid(row=0,column=1, sticky=W+E)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', bg= additional_color, command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', bg= additional_color, command=show_answer).grid(row=4, column=1, sticky=W, pady=4)

mainloop()