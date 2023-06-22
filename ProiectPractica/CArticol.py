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
        print("id "+self.id+"\n")
        print("name "+self.name+"\n")
        print("author "+self.author+"\n")
        print("title "+self.title+"\n")
        print("description "+self.description+"\n")
        print("url "+self.url+"\n")
        print("urlToImage "+self.urlToImage+"\n")
        print("publishedAt "+self.publishedAt+"\n")
        print("content "+self.content+"\n")
        print("\n\n");



        
        