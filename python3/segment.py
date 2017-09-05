import jieba

def main():

    stopwordset = set()
    with open('/Users/roger/Downloads/text_classification/stopwords.txt','r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    texts_num = 0

    output = open('wiki_seg.txt','w')
    with open('wiki_texts.txt','r') as content :
        for line in content:
            line = line.strip('\n')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word +' ')

            texts_num += 1
            if texts_num % 1000 == 0:
                print("已完成前 %d 行的斷詞" % texts_num)
    output.close()

if __name__ == '__main__':
    main()