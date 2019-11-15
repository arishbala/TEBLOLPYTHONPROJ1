#Teb Python Corpus Project

import io
import nltk

from nltk.corpus import wordnet

nltk.download('wordnet')


def main():
    _file = input ("Enter the file name for the words/synonyms you want to find")
    read = open (_file,'r')
    real_file = read.read()
    #print (real_file)
    count = 0
    _word = input ("Enter the word that you want to search or find")
    new_corp = nltk.WordPunctTokenizer().tokenize(real_file)
    #_pos = nltk.pos_tag(nltk.word_tokenize(_word))
    #print (_pos)
    #thing = nltk.wsd.lesk (lang_,_word)
    #print (thing)
    #print(new_corp)
    
    for x in new_corp:
        #print(x)
        for _syns in wordnet.synsets(_word):
            for i in _syns.lemmas():
                print (i.name())
                if x == i. name () or x == _word:
                    if i.name() == _word:
                        break 
                    else:
                        if x == _word:
                            count += 1
                            continue
                        print ("Your corpus has listed", count,"of the word", _word, "and it's synonyms")   
main()    
