"""Hosting the same flipkart review using web scrapping by flask"""

from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
import requests
import logging

base_url = "https://www.flipkart.com/search?q="

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

url_client = uReq(flipkart_url)
flipkart_page = url_client.read()
bs("flipkart_page","html.parser")
