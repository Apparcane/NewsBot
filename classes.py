class message:

    # def write(self, isource, ititle, iauthor, idescript, iurl):
    #     self.source = isource
    #     self.title = ititle
    #     self.author = iauthor
    #     self.descript = idescript
    #     self.url = iurl
        
    def display(self, source, title, author, descript, url):
        if author == None:
            author = 'Не указан'
        return source + '\n' + title + '\n' + author + '\n' + descript + '\n' + url 