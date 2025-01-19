"""Hosting the same flipkart review using web scrapping by flask"""
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uOpen
import requests
import logging