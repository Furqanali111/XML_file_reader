from lxml import etree
import pandas as pd

tree = etree.parse("compiler.xml")
root = tree.getroot()

data=[]

for book in root.findall("book"):
    book_dict = {}
    book_dict['Book ID'] = book.get('id')
    book_dict['Author'] = book.find('author').text
    book_dict['Title'] = book.find('title').text
    book_dict['Genre'] = book.find('genre').text
    book_dict['Price'] = book.find('price').text
    book_dict['Publish Date'] = book.find('publish_date').text
    book_dict['Description'] = book.find('description').text
    data.append(book_dict)

#creeating a data frame to write it on excel
df = pd.DataFrame(data)
print(df)
#writing to excel
df.to_excel('Books.xlsx', index=False)
