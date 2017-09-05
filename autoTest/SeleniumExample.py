#coding=utf-8
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.yahoo.com")
assert "Yahoo!" in browser.title
browser.close()
