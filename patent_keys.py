# -*- coding: utf-8 -*-
def patent_keys_extract(read_path,write_path):
    import nltk
    from nltk.corpus import stopwords
    import csv
    import re
    from copy import deepcopy
    r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    stop = stopwords.words('english')
    csv_data=csv.reader(open(read_path,'r'))#读取专利源文件
    print '++++++++++++++++++++数据读取完毕++++++++++++++++++++'
    dict_data=[]
    for lines in csv_data:
        dict_data.append(lines)
    row_num=len(dict_data)
    result={}
    i=0
    print '++++++++++++++++++++正在处理数据++++++++++++++++++++'
    words=[]
    while(i < row_num):
        text=str(dict_data[i])
        sens=nltk.sent_tokenize(text)
        for sent in sens:
            sent_stoped=[]
            words2=[]
            for j in sent.split():
                if j not in stop:
                    sent_stoped.append(j)
            sent_stoped_punctuation=re.sub(r,'',str(sent_stoped))
            words.append(nltk.word_tokenize(str(sent_stoped_punctuation)))
            for m in words:
                words2=words2+m
        words3=list(set(words2))
        result[i]=deepcopy(words3)
        words[:]=[]
        i=i+1
    patent_words_results=open(write_path,'w')#将处理结果写入文件
    for j in range(len(result)):
        patent_words_results.write(str(result[j]))
        patent_words_results.write('\n')
    patent_words_results.close()
    print '++++++++++++++++++++数据处理完毕，已写入文件++++++++++++++++++++'
