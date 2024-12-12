import streamlit as st
import requests

steam_html = requests.get("https://store.steampowered.com")
print(steam_html.text.split("<!-- Special offers block -->")
      [1].split("<!-- Carousel linking to various category content hubs. -->")[0])
