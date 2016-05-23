
import os
import json
from parse import *
from gensim import corpora

def replace(txt):
    txt = txt.replace("\n", "")

    r = parse("{number}\u3000{text}", txt)
    if r and 'text' in r:
         txt = r['text']
    
    r = parse("{number}　{text}", txt)
    if r and 'text' in r:
         txt = r['text']

    txt = txt.replace("\u3000", "")
    txt = txt.replace("　", "")
    txt = txt.replace("○", "")

    return txt

def load_text(obj):
    for k, v in obj.items():
        if 'text' in v and v['text'] != '':
            text = replace(v['text'])
            f.write(text + '\n')
        else:
            load_text(obj)


if __name__ == '__main__':

    files = os.listdir('all')
    print('== load ==')
    data = []
    for name in files:
        fin = open('all/'+name)
        data.append(json.load(fin))
        fin.close()
    print('== done ==')

    
    f = open('input.txt', 'w')
    print('== write ==')
    for i in range(len(data)):
        js = data[i]['provision']
        load_text(js)
    print('== done ==')
    f.close()


