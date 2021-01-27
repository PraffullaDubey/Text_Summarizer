# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:59:26 2021

@author: Praffulla
"""
#install required library pip install sumy and pip install textrank

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

#function to read data from file
def find_file_data(pathname):
    file1 = open(pathname,encoding="utf8")  #open the text file
    line = file1.read() #read the file
    print(line,"\n") #printing the text present in file
    file1.close() #close the file

#function to find summary using lexrank summarizer
def find_summary_lexrank():
    p = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    summarizer = LexRankSummarizer() #creating lexrank object
    summ = summarizer(p.document, 2) #Summarizing the document
    #display the summary
    for s in summ:
        print(s)

#function to find summary using stopwords method using lsa summarizer
def find_summary_stopwords():
    p = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    s_lsa = LsaSummarizer()
    s_lsa = LsaSummarizer(Stemmer("english"))
    s_lsa.stop_words = get_stop_words("english")
    for s in s_lsa(p.document,2):
        print(s)

#function to find summary using lsa summarizer      
def find_summary_lsa():
    p = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    sumlsa = LsaSummarizer()
    su =sumlsa(p.document,2)
    for s in su:
        print(s)

#function to find summary using luhn summarizer
def find_summary_luhn():
    p = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    s_luhn = LuhnSummarizer()
    su =s_luhn(p.document,2)
    for s in su:
        print(s)
    
pathname = "testtext.txt"
find_file_data(pathname)
find_summary_lexrank() #function call
find_summary_stopwords() #function call
find_summary_lsa() #function call
find_summary_luhn() #function call