# -*- coding: utf-8 -*-
import pandas as pd
import numpy
import copy
import sys
import codecs
import csv
from pandas import Series,DataFrame
from xml.etree import ElementTree as ET

def main():
    print('开始处理,正在读取数据')
    csv_data=pd.read_csv('D:/pydata/mypydata/title_abstract_2.csv')
    text_patent=DataFrame(csv_data,columns=['num','title','abstract','open_num','claims'])
    num_open_get=copy.deepcopy(text_patent['open_num'])
    text_patent.set_index('open_num',inplace=True)
    len_num_open_get=len(num_open_get)
    list1 = []
    for i in range(len_num_open_get):
        print('正在处理第'+str(i)+ '条专利')
        csvfile = open('D:/pydata/mypydata/patentdata_chinese.csv', 'a', newline='',encoding='utf-8')
        spamwriter = csv.writer(csvfile, dialect='excel')
        j=num_open_get[i]
        claim_text_2=claims_xml(j)
        list1=[str(text_patent.ix[j,'num']),j,str(text_patent.ix[j,'title']),str(text_patent.ix[j,'abstract']),str(claim_text_2)]

        spamwriter.writerow(list1)
        #text_patent.loc[j,'claims']= claim_text_2
        #print(sys.getsizeof(spamwriter)
    print('处理完成，已写入文件')
    return

def claims_xml(num_open):
    file_path='D:\pydata\mypydata\claim\\'
    file_type='_ori.xml'
    with open( file_path + num_open + file_type,'r',encoding='utf-8') as xml_file:
        text_pt=xml_file.read()
    text_pt=text_pt.replace('<br/>','')
    text_pt=text_pt.replace('<sub>','')
    text_pt=text_pt.replace('</sub>','')
    text_pt=text_pt.replace('<sup>','')
    text_pt=text_pt.replace('</sup>','')
    text_pt.strip()
    tree=ET.fromstring(text_pt)
    p=tree.findall('.//claim')
    claim_text=''
    for oneper in p:
        for child in oneper.getchildren():
            if child.text is None:
                child.text=''
            claim_text_part=''.join(child.text.split())
            claim_text=claim_text+str(claim_text_part)

    return claim_text

if __name__=="__main__":
    main()


