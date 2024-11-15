from flask import render_template, request, redirect, flash, jsonify
from bs4 import BeautifulSoup

URL_FILE = "urls.txt"

class Scraper:

    def load_urls():
        try:
            with open(URL_FILE, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []
        
    def save_urls(urls):
            with open(URL_FILE, 'w') as file:
                file.write('\n'.join(urls))

    def add_url(new_url):
        urls = Scraper.load_urls()

        if new_url not in urls:
            urls.append(new_url)
            Scraper.save_urls(urls)
            return ({'msg': new_url + " added"})
        else:
            return ({'msg': "URL already exists or invalid"})
        

    def remove_url(url):
        urls = Scraper.load_urls()

        if url in urls:
            url.remove(url)
            Scraper.save_urls(urls)
            return ({'msg': url + " removed"})
        else:
            return ({'msg': "URL does not exist"})
    


