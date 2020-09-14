class catagory:
    def showAll(self):
        import sqlite3
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM category")
        Catagories= cursor.fetchall()
        print("ID Name")
        for single in Catagories:
            print(single[0]," ",single[1])
            pass

class books:
    def allBooks(self):
        import sqlite3
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        cursor.execute("SELECT  book.bid, book.bname, book.bauthor, category.cname FROM book INNER JOIN category ON book.cId = category.cId ")
        Catagories= cursor.fetchall()
        print("ID Name Author catagory")
        for single in Catagories:
            print(single[0]," ",single[1]," ",single[2]," ",single[3])
            pass

    def searchByCata(self, ID):
        import sqlite3
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        query = "SELECT * FROM book WHERE cid= '"+str(ID)+"'"
        cursor.execute(query)
        Catagories= cursor.fetchall()
        print("ID Name Author")
        for single in Catagories:
            print(single[0]," ",single[1]," ",single[2])
            pass

    def searchByAuthor(self, name):
        import sqlite3
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        query = "SELECT * FROM book WHERE bauthor= '"+name+"'"
        cursor.execute(query)
        Catagories= cursor.fetchall()
        print("ID Name Author")
        for single in Catagories:
            print(single[0]," ",single[1]," ",single[2])
            pass

class orderBook:
    
    def __init__(self, bId,cusName):
        import datetime
        self.bId= bId
        self.cusName = cusName
        self.BuyDate = datetime.datetime.now()
        self.returnDate = self.BuyDate + datetime.timedelta(days=10)

    def show(self):
        import sqlite3
        connection = sqlite3.connect("sqlite.db")
        cursor = connection.cursor()
        cursor.execute("SELECT  book.bid, book.bname, book.bauthor, category.cname FROM book INNER JOIN category ON book.cId = category.cId WHERE book.bid='"+str(self.bId)+"'")
        Catagories= cursor.fetchall()
        print("ID Name Author catagory buydate returndate Customer Name")
        for single in Catagories:
            print(single[0]," ",single[1]," ",single[2]," ",single[3]," ",self.BuyDate," ",self.returnDate," ",self.cusName)
            pass
       

class manager: 
    order = []
   
    def addOrder(self, bId,cusName):
        temp = orderBook(bId,cusName)
        self.order.append(temp)

    def showAll(self):
        for x in self.order:
            x.show()
            pass

def Manu():
    print("1> show all books")
    print("2> show all catagory")
    print("3> show all books")
    print("4> Borrow Boo")
    print("5> Recept")
    print("Press any key to exit")

def Main():
   
    m = manager()
    book = books()
    cata = catagory()

    while True:
        Manu()
        key = int(input("Enter Your Choice"))
        if key == 1:
            print("**********************************")
            book.allBooks()
        elif key == 2:
            print("**********************************")
            cata.showAll()
            id = int(input("Please enter catagory id: "))
            book.searchByCata(id)
        elif key == 3: 
            print("**********************************")
            book.allBooks()
            id = input("Please enter Book author name: ")
            book.searchByAuthor(id)
        elif key == 4:
            print("**********************************")
            book.allBooks()
            id = int(input("Enter Book Id you want to borrow:"))
            name = input("Enter Customer Name: ")
            m.addOrder(id,name)
        elif key == 5:
            print("**********************************")
            m.showAll()
        else:
            print("**********************************")
            print("Thanks for using my system")
            break

try:
    Main()
    pass
except :
    pass