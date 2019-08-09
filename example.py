import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
import spacy

class sentence_parse:

    nlp = spacy.load('en_core_web_lg')

    def single_line_address(self, sentence):

        address_lines = [line for line in sentence.split('\n') if line]
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(sentence)
        custom_stopwords = ["Hey!","man","address"]
        stop_words = list(set(stopwords.words('english')))
        total_stop = custom_stopwords + stop_words
        filtered_words = [w for w in tokens if not w in total_stop]
        for i in range(0, len(filtered_words)):
            if filtered_words[i] in ['Street', 'st', 'street', 'Avenue','ave','rd', 'dr','hwy','blvd','way','lane','route','loop']:
                print(filtered_words[i-2], filtered_words[i-1], filtered_words[i])
        return " ".join(filtered_words)

    def find_person_name(self, sentence):      #function to find person name
        nlp = spacy.load('en_core_web_lg')  #loading the package from spacy
        doc = nlp(sentence)                    
        for ent in doc.ents: #iterating through address lines
            if ent.label_ == 'PERSON':      #finding the label of the entities if label is PERSON then 
                print(ent, ent.label_)      #print person name
            if ent.label_ == 'GPE':
                print(ent)
            if ent.label_ == 'LOC' or ent.label_ == 'FAC':
                print(ent)
            if len(str(ent)) == 5 or len(str(ent)) == 4 and str(ent).isnumeric():
                print(ent)
sentence = """Hey man! Joe lives here: 44 West 22nd Street, New York, NY, 1234, USA. Can you contact him now? """
obj = sentence_parse()
obj.single_line_address(sentence)
obj.find_person_name(sentence)


#expected output 
#West 22nd Street
#Joe PERSON
#New York
#NY
#1234
#USA
