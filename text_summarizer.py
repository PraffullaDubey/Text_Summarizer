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

#function to find summary using textrank
def find_summary_textrank():
    p = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    summarizer = LexRankSummarizer() #creating lexrank object
    summ = summarizer(p.document, 2) #Summarizing the document
    #display the summary
    for s in summ:
        print(s)
        
def find_summary_stopwords():
    parser = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    summarizer_lsa2 = LsaSummarizer()
    summarizer_lsa2 = LsaSummarizer(Stemmer("english"))
    summarizer_lsa2.stop_words = get_stop_words("english")
    for sentence in summarizer_lsa2(parser.document,2):
        print(sentence)
        
def find_summary_lsa():
    parser = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    summarizer_lsa = LsaSummarizer()
    summary_2 =summarizer_lsa(parser.document,2)
    for sentence in summary_2:
        print(sentence)
    
def find_summary_luhn():
    parser = PlaintextParser.from_file("testtext.txt", Tokenizer("english"))
    summarizer_luhn = LuhnSummarizer()
    summary_1 =summarizer_luhn(parser.document,2)
    for sentence in summary_1:
        print(sentence)
    

pathname = "testtext.txt"
find_file_data(pathname)
find_summary_luhn() #function call