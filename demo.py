
import spacy
import code

nlp = spacy.load('en_core_web_lg')

class AddressParse:
    
    def __init__(self, address):
        self.address = address
        self. result = {        #appends all the labels with the values to the result
            'name': '',
            'street': '',
            'country': '',
            'ORG': '',
           'house number': '',
        }

    def parse_lines(self):
        lines = [line for line in self.address.split('\n') if line]  #parsing the address based on new line
        lines_cl = []
        for line in lines:
            words = [word.title() for word in line.split(' ')] #makes the first letter of every word capital
            line = ' '.join(words)
            lines_cl.append(line)
        return lines_cl

    def get_name(self, lines):
        """identifies the name of person, country, and organisation using ent.label_ in spacy"""
        for line in lines:   
            doc = nlp(line)
            for ent in doc.ents:   #iterates through all entities in list
                if ent.label_ == 'PERSON':  #checks if the label is PERSON
                    self.result['name'] = ent.text 
                if ent.label_ == 'GPE':     #checks if the label is GPE
                    self.result['country'] = ent.text
                if ent.label_ == 'ORG':     #checks if the label is ORG
                    self.result['organisation'] = ent.text             
    
    def get_street(self, lines): 
        for line in lines:
            words = [word.lower() for word in line.split(' ')] 
            if 'street' in words or 'st' in words or 'strt' in words or 'ave' in words or 'avenue' in words or 'rd' in words or 'dr' in words or 'hwy' in words or 'blvd' in words or 'way' in words or 'lane' in words or 'route' in words or 'loop' in words:
                self.result['street'] = line
            elif 'suite' in words or "house no." in words or "house number" in words or "apt" in words or "hno." in words or "floor" in words:
                self.result['house number'] = line  #identifies house number

    def street_using_ent(self, lines):
        """ 
        identifies street based on entity label
        """
        for line in lines:
            doc = nlp(line) 
            for ent in doc.ents:  #iterates through all entities in list
                #print(ent.label_)
                if ent.label_ in ['FAC', 'LOC']:  #checks if the label is location
                    self.result['street'] = line    #appends to result

    def parse_street(self):
        lines = self.parse_lines()
        self.get_name(lines) #method call
        self.get_street(lines) #method call
        if self.result['street'] == '':  #after getting the street name its stored in result
            self.street_using_ent(lines)  #method call
        print(self.result)

