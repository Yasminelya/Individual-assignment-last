# -*- coding: utf-8 -*-

import requests

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": []
}

def get_graph(graph): 
    data = graph
    request = requests.post("http://127.0.0.1:5000/upload-graph", json=data)
    return request.json()

def degrees_of_separation(origin, destination): 
    data = graph
    request = requests.get('http://127.0.0.1:5000/degrees-of-separation/{}/{}'.format(origin, destination), json=data)
    return request.json()
