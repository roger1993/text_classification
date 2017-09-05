import pandas as pd
from bs4 import BeautifulSoup
import re

def clean_str(string):
    string = re.sub("[\s+\.\!,\"\'“ ”]+", "", string)   
    string = re.sub("[！，。？、~（）%/]+", "", string)  
    string = re.sub("[【】『』「」︰：]+", "", string) 
    string = re.sub("[《》〈〉”“；｜-]+","",string)
    string = re.sub("[():]+","",string)
    return string.strip()


train_path = "./dataset/train_set.csv"
test_path = "./dataset/test_set.csv"
data_train = pd.read_csv(train_path)
data_test = pd.read_csv(test_path)
print ("training data: ", data_train.shape)
print ("testing data: ", data_test.shape)


texts = []
labels = []
counter = 0
texts_num = 0
with open("wiki_texts.txt",'w',encoding='utf-8') as output:
    for idx in range(data_train.content.shape[0]):
        soup = BeautifulSoup(data_train.content[idx],"html.parser")
        text = soup.get_text()
        text = " ".join(text.split())
        text = clean_str(text)
        output.write("".join(str(n) for n in text) + '\n')
        texts_num += 1
        if texts_num % 1000 == 0:
            print("已處理 %d 篇文章" % texts_num)