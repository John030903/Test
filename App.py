import streamlit as st
import requests
import json

def use_api(url):
    """
    It takes a URL as an argument, makes a request to that URL, and returns the response as a JSON
    object
    
    :param url: The URL of the API you want to use
    :return: A dictionary
    """
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',}
    response = requests.get(url, headers=headers)
    # print(response.content)
    data = response.content
    return data

data  = use_api("http://127.0.0.1:5500")
st.write(data)