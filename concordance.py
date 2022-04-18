import nltk.tokenize
from nltk.text import Text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def concordance(filepath, keyword = "Test", savefile = False, savepath = '/Users/User/Desktop/result.txt'):
    with open(filepath,'r',encoding='UTF-8') as f:
        data = f.read()
    text = Text(nltk.word_tokenize(data))
    text.concordance(keyword, lines=20, width=50)
    con_list = text.concordance_list("monstrous")

    if savefile:
        result = []
        for i in con_list:
            result.append(i)
        with open(savepath,'w') as f:
            for i in result:
                f.write(str(i)+'\n')