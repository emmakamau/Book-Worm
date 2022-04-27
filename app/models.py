'''
Define and initialize classes for our objects
'''

class Books:

    books_list = []

    def __init__(self,id,title,authors,publishedDate,description,language):
        self.id = id
        self.title = title
        self.authors = authors
        self.publishedDate=publishedDate
        self.description = description
        self.language = language


    pass