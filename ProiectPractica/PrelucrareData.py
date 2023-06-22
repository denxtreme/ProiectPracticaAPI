import requests
import re
import CArticol
import sys


def delimiteaza_cuvinte(text, delimitatori):
    regex_pattern = "[" + re.escape("".join(delimitatori)) + "]+"
    cuvinte = re.split(regex_pattern, text)
    cuvinte = [cuvant.strip() for cuvant in cuvinte if cuvant.strip()]
    return cuvinte


class APIdata:
    def __init__(self, name, url):
        self.name = name
        self.url = url 
        self.vectorArticole=[]
        self.Vector_CArticol=[]
        self.nrArticole=0        

    def DecUrl(self):
        response=requests.get(self.url)
        if response.status_code == 200:  
            self.data=response.text                  
        else:
            print("Error: Unable to access the API.")


    def NewUrl(self,url):
        self.url = url
        self.DecUrl()


    def DataTOarticle(self):
        delimitatori = [",", "!", "?"," ","}","{","[","]","\"","\""]
        cuvinte = delimiteaza_cuvinte(self.data, delimitatori)
        contor = 0
        cuvant_cautat="source"
        Articol="" 
        # Iterăm prin cuvinte
        for index, cuvant in enumerate(cuvinte):
            if cuvant == cuvant_cautat:
               if contor != 0:
                  self.vectorArticole.append(Articol.strip())                  
               contor += 1 
               Articol=""
            Articol=Articol+' '+cuvant
        print(self.nrArticole)
        for articols in self.vectorArticole:
            print(articols)
            print("\n")

     
    def ExtractDataArticle(self,Article_string):
        delimitatori = [",", "!", "?"," ","}","{","[","]","\"","\""]
        cuvinte = delimiteaza_cuvinte(Article_string, delimitatori)
        ElementArticol=""
        ok=0
        for word in cuvinte:
            ok=0
            if word == "id":
                ElementArticol=""
                ok=1
            if word == "name":
                id=ElementArticol
                ok=1
                ElementArticol=""
            if word == "author":
                name2=ElementArticol
                ElementArticol=""
                ok=1
            if word == "title":
                author=ElementArticol
                ElementArticol=""
                ok=1
            if word == "description":
                title=ElementArticol
                ElementArticol=""
                ok=1
            if word == "url":
                description=ElementArticol
                ElementArticol=""
                ok=1
            if word == "urlToImage":
                url2=ElementArticol
                ElementArticol=""
                ok=1
            if word == "publishedAt":
                urlToImage=ElementArticol
                ElementArticol=""    
                ok=1            
            if word == "content":
                publishedAt=ElementArticol
                ElementArticol=""
                ok=2
            if ok == 0 and word !=":" :      
                if word == ":null":
                    word="null"
                if len(ElementArticol) > 0 :
                    ElementArticol=ElementArticol+" "+str(word)
                else :
                    ElementArticol=str(word)
        
        
        content=ElementArticol
        cArticolOBJ=CArticol.CCArticol(id, name2, author, title, description, url2, urlToImage, publishedAt, content)
        self.Vector_CArticol.append(cArticolOBJ)


    def CreateCArticol(self):   
        for Articol in self.vectorArticole:
            self.ExtractDataArticle(Articol)
        #for CArticole in self.Vector_CArticol:
            #CArticole.PresentArticols()    

    def CreateAllYouNeed(self):
        self.DecUrl()
        self.DataTOarticle()
        self.CreateCArticol()         



      


