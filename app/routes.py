from flask import Blueprint, jsonify, request

from .scraper import Scraper

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    urls = Scraper.load_urls()
    return jsonify(urls)

@main.route("/add", methods=["POST"])
def add():
    url_added = Scraper.add_url(request.json.get('url'))
    return jsonify(url_added)

@main.route("/scrape")
def scrape():
    return "Welcome to scrape!"