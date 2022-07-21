import csv
def readSaveBookInfo():
    bookList = []
    while True:
        bookNo = int(input("enter book number: "))
        bookTitle = input("Enter book title: ")
        bookAuthor = input("Enter book author: ")
        bookPrice = int(input("Enter book price: "))
        bookList.append([bookNo, bookTitle, bookAuthor, bookPrice])
        ch = input("Enter y/n to enter more.. ")
        if ch == 'N' or ch == 'n':
            with open("TW3.csv", "w") as f:
                writer  = csv.writer(f,lineterminator='\n')
                writer.writerows(bookList)
        break

def searchBookAuthor():
    author = input("Enter author name: ")
    with open("TW3.csv") as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            if row[2] == author:
                result.append(row)
        if result == []:
            print("no books with this author name :( ")
        else:
            print("books with this author name are: ")
        for line in result:
            print(line)

def searchBookPrice():
    price = int(input("enter your price: "))
    try:
        if price <= 0:
            raise ValueError("invalid input for price :) ")
        with open("TW3.csv") as f:
            reader = csv.reader(f)
            result = []
            for row in reader:
                if int(row[3] < price):
                    result.append(row)
            if result == []:
                print("no books within this price range :( ")
            else: 
                print("these books are within the price range: ")
            for line in result:
                print(line)
    except ValueError as VE:
        print(VE)

def searchBookTitle():
    title = input("Enter book title: ")
    with open("TW3.csv") as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            if row[1] == title:
                result.append(row)
        if result == []:
            print("no books with this title :( ")
        else:
            print("books with this title are: ")
        for line in result:
            print(line)

def main():
    readSaveBookInfo()
    menuDict = {
        "1": searchBookAuthor,
        "2": searchBookPrice,
        "3": searchBookTitle,
        "4": "exit"
    }
    while True:
        choice = input("enter your choice: ")
        if choice == "4":
            break
        menuDict[choice]()

if __name__ == "__main__":
    main()
