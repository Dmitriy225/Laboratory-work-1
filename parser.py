from bs4 import BeautifulSoup
import requests
from book import book

def parse():
    url = 'https://www.chitai-gorod.ru/'
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('article', class_='product-card slider__item-card')
    books = list()
    for data in block:
        name = data.find('div', class_='product-card__text product-card__row').\
            find('a', class_='product-card__title').\
            find('div', class_='product-title').\
            find('div', class_='product-title__head').text

        author = data.find('div', class_='product-card__text product-card__row').\
            find('a', class_='product-card__title').\
            find('div', class_='product-title').\
            find('div', class_='product-title__author').text

        priceDiscountBlock = data.find('div', class_='product-card__price product-card__row').\
            find('div', class_='product-price').\
            find('div', class_='product-price__value product-price__value--discount')
        if priceDiscountBlock: # Если на книгу есть скидка
            price = priceDiscountBlock.text
        else: # Если на книгу скидки нет, то цена хранится в другом блоке
            price = data.find('div', class_='product-card__price product-card__row').\
                find('div', class_='product-price').\
                find('div', class_='product-price__value').text
        books.append(book(name, author, price))
    return books