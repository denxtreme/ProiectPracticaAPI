import re

class CCArticol:
    def __init__(self, id=None, name=None, author=None , title=None , description=None, url=None, urlToImage=None , publishedAt=None, content=None):
        self.name = name
        self.id = id 
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content

    def PresentArticols(self):
        stringARTICOLE="ID: "+self.AlignText(self.id)+"\n"
        stringARTICOLE+="Name: "+self.AlignText(self.name)+"\n"
        stringARTICOLE+="Author: "+self.AlignText(self.author)+"\n"
        stringARTICOLE+="Title: "+self.AlignText(self.title)+"\n"
        stringARTICOLE+="PublishedAt: "+self.AlignText(self.publishedAt)+"\n"
        return stringARTICOLE
    def PresentArticolsDesc(self): 
        stringARTICOLE="Description: "+self.AlignText(self.description)+"\n\n"
        stringARTICOLE+="Content: " +self.AlignText(self.content)+"\n"
        return stringARTICOLE
    
    def AlignText(self,Mystring):
        if len(Mystring) > 7 :
            Mystring=insert_newline_every_7th_word(Mystring)
            return Mystring
        else :
            return Mystring

def insert_newline_every_7th_word(text):
        words = text.split()
        count = 0
        new_text = ""
        for word in words:
            count += 1
            new_text += word + " "
            if count % 7 == 0:
                new_text += "\n"
        return new_text

        
        