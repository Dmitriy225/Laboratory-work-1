import parser
import fileCreater

if __name__ == '__main__':
    books = parser.parse()
    fileCreater.create_xlsx(books)