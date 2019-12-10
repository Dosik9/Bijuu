#Task 5
import json
id_user=1
id_book=1
try:
    Books=list(json.load(opener))
except:
    Books=[]
try:
    Users=list(json.load(opener))
except:
    Users=[]

def addBook(id_book):
    id=id_book
    id_book=id_book+1
    Title=input("Title of book: ")
    Author=input("Author of book: ")
    Publisher=input("Publisher of book: ")
    Quantity=int(input("Quantity of books: "))
    book={"ID":id,"Title":Title,"Author":Author,"Publisher":Publisher,"Quantity":Quantity}
    opener=open("Library.json")
    Books.append(book)
    with open("Library.json", "w") as file_b:
        json.dump(Books,file_b)
        file_b.close();
def addUser(id_user):
    id=id_user
    id_user+=1
    name=input("Name of user: ")
    surname=input("Surname of user: ")
    login=input("Create login for user: ")
    password=input("Create password for user: ")
    user={"ID":id,"Name":name,"Surname":surname, "Login":login, "Password":password}
    opener=open("Users.json")
    Users.append(user)
    with open("Users.json","w") as file_u:
        json.dump(Users,file_u)
        file_u.close()

def allBooks():
    with open("Library.json") as file_b:
        all_books=file_b.read()
        print(all_books)
        file_b.close()

def allUsers():
    with open("Users.json") as file_b:
        all_users=file_b.read()
        print(all_users)
        file_b.close()

def removeBook():
    with open("Library.json") as file_b:
        all_books=list(json.load(file_b))
        for i in all_books:
            print(i)
        remove_book=int(input("Choose ID which book need removing: "))
        for i in range (len(all_books)):
            if all_books[i]['ID']==remove_book :
                del all_books[i]
        # del remove_book
def Search_Book():
    print("Search by:\n [1].ID\n [2].Title\n [3].Author")
    num=int(input("Choose one: "))
    with open("Library.json") as file_b:
        all_books=list(json.load(file_b))
        if num==1:
            serch_id=int(input("Enter 'ID' of book: "))
            for i in range (len(all_books)):
                if all_books[i]['ID']==serch_id :
                    print(all_books[i])
                else:
                    print("A book by that ID doesn`t exist")
        elif num==2:
            serch_Title=input("Enter 'Title' of book: ")
            for i in range (len(all_books)):
                if all_books[i]['Title']==serch_Title :
                    print(all_books[i])
                else:
                    print("A book by that Title doesn`t exist")
        elif num==3:
            serch_Author=input("Enter 'Author' of book: ")
            for i in range (len(all_books)):
                if all_books[i]['Author']==serch_Author :
                    print(all_books[i])
                else:
                    print("A book by that Author doesn`t exist")
while(True):
    print("[1].Admin")
    print("[2].User")
    print("[0].Exit")
    number=int(input("Choose one: "))
    if number==1:
        print("[1]. Add Book")
        print("[2]. Add User")
        print("[3]. All Books")
        print("[4]. Remove Book")
        print("[5]. All Users")
        print("[6]. Remove Users")
        print("[0]. Exit")
        num=int(input("Choose one: "))
        if num==1:
            addBook(id_book)
        elif num==2:
            addUser(id_user)
        elif num==3:
            allBooks()
        elif num==4:
            removeBook()
        elif num==5:
            allUsers()
        elif num==0:
            continue

    elif number==2:
        print("Hello User")
        login=input("Enter your login: ")
        password=input("Enter your password: ")
        with open("Users.json") as file_u:
            all_users=list(json.load(file_u))
            for i in range (len(all_users)):
                if all_users[i]['Login']==login and all_users[i]['Password']==password :
                    print("Wellcome!")
                    print("[1]. All book")
                    print("[2]. Give book")
                    print("[3]. Find book")
                    print("[0]. Back")
                    num=int(input("Choose one: "))
                    if num==1:
                        allBooks()
                    elif num==3:
                        Search_Book()
                    elif num==0:
                        continue
                else:
                    print("You entered incorrect login or password")
    elif number==0:
        break
    else:
        continue
