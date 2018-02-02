# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import numpy
import csv
import copy
import pandas as pd
from pandas import Series,DataFrame
def patent_key_chinese(patent_data_path,words_result_path,stopwords_path,mydict_path):
    jieba.load_userdict(mydict_path)
    patent_data=pd.read_csv(patent_data_path,encoding='utf-8')
    print('已载入专利数据')
    patent_dataframe=DataFrame(patent_data)
    patent_opennum=copy.deepcopy(patent_dataframe['open_num'])
    patent_dataframe.set_index('open_num',inplace=True)
    csvfile=open(words_result_path,'a',newline='',encoding='utf-8')
    wordswriter=csv.writer(csvfile)
    stopwords=open(stopwords_path,'r',encoding='utf-8')
    stopwords_list=[]
    for line in stopwords:
        line=line.strip()
        stopwords_list.append(str(line))
    print('+++++开始处理+++++')
    for i in range(len(patent_opennum)):
        print('正在处理第'+str(i)+ '条专利')
        text=''
        butoff=[]
        text_words_processed=''
        j=patent_opennum[i]
        text = patent_dataframe.loc[j, ['title', 'abstract', 'claims']]
        text_str=str(text.tolist())
        text_words=jieba.cut(text_str)

        for m in text_words:
            m=m.replace(' ','')
            m=m.replace('"','')
            if m not in stopwords_list:
                butoff.append(m)
        text_words_processed= ' '.join(butoff)
        list2=[j,text_words_processed]
        wordswriter.writerow(list2)
    print('处理完毕，结果已写入文件')
patent_key_chinese('D:\pydata\mypydata\patentdata_chinese.csv','D:\pydata\mypydata\patentdata_chinese_words.csv','D:\pydata\mypymodule\chinese_stopword.txt','D:\pydata\mypymodule\mydict.txt')




