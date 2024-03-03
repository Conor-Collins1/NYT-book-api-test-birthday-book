import requests
import json

n_books = 0
dash = "-"

def main(book_input):
    book_n = int(book_input)
    book_n -= 1
    book_t = books_found[book_n]["title"]
    print ("\n", book_t.title(), "A book from",books_found[book_n]["author"] )
    print (books_found[book_n]["description"])
    print ("You can order this book and learn more at", books_found[book_n]['amazon_product_url'])
    again = input("\n Would you like to learn about another book?  ( Y/N )")
    if again == "Y":
        main(input("\n which book would you like to learn about?"))
    else :
        print("\n Goodbye!")


print("\n","\n")
print("Would you like to run", "\n", "(1)birthday top booklist - only works for dates after 2008")
choice=input("or (2)todays top booklist  ")





if choice == "2" :
    data_a = requests.get("https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=Jm0tzINVh3ShhoElcAc4P6N3IlHn7hz5")
    response_json = json.loads(data_a.text)
    books_found = response_json["results"]["books"]
    for n in books_found:
        n_books+=1
    books_found=str(n_books)

    print("\n \n The top 15 fiction books today according to NYT are:")
    books_found = response_json["results"]["books"]
    for n in books_found:
       name = n['title']
       rank = n['rank']
       print(rank,name.title())
    main(input("which book would you like to learn about (1-15)"))





if choice == "1" :
    year=input("\n what year were you born? (only data for greater than 2008)  e.g 2010  ")

    month=input("what month e.g 9  ")
    if int(month) < 10 :
        month = "0"+month
    
    day=input("what day? e.g 14  ")
    if int(day) < 10 :
        day = "0"+day

    data_a = requests.get("https://api.nytimes.com/svc/books/v3/lists/"+year+dash+month+dash+day+"/hardcover-fiction.json?api-key=Jm0tzINVh3ShhoElcAc4P6N3IlHn7hz5")
    response_json = json.loads(data_a.text)
    books_found = response_json["results"]["books"]
    for n in books_found:
        n_books+=1
    n_books=str(n_books)
    print("\n \n The top "+n_books+" fiction books on your birthday according to NYT are:")
    books_found = response_json["results"]["books"]
    for n in books_found:
       name = n['title']
       rank = n['rank']
       print(rank,name.title())
    main(input("which book would you like to learn about (1-"+n_books+")"))
