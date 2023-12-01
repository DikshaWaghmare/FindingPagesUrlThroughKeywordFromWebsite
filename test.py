
# Python code with frontend to find all urls in given websites where given keywords found in anchor tag#

from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

app = Flask(__name__)

def find_urls_with_keyword(url, keyword):
    visited_links = set()
    matched_urls = []

    def search_in_page(url):
        nonlocal matched_urls
        if url in visited_links or len(matched_urls) >= 10:
            return
        visited_links.add(url)

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            anchor_tags = soup.find_all('a', href=True)
            
            for tag in anchor_tags:
                text = tag.get_text()
                if keyword.lower() in text.lower():
                    link = tag['href']
                    full_link = urljoin(url, link)
                    matched_urls.append(full_link)
                    if len(matched_urls) >= 10:
                        return
                    search_in_page(full_link)
            
        except requests.RequestException as e:
            pass

    search_in_page(url)
    return matched_urls

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    website_url = request.form['websiteUrl']
    keyword = request.form['keyword']

    matched_urls = find_urls_with_keyword(website_url, keyword)
    
    return render_template('index.html', urls=matched_urls, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)

