# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def get_graph():
    body = request.get_json()
    return jsonify(body)

@server.route('/degrees-of-separation/<origin>/<destination>', methods=['GET'])
def find_path(origin, destination, graph='', paths=[]):
        
    graph = request.get_json()
    
    paths = paths + [origin]
    
    if origin == destination:
        return jsonify(len(paths)-1)
    
    if origin not in graph:
        return jsonify("no origin in the graph")
    
    for node in graph[origin]:
        if node not in path:
            newpath = find_path(node, destination, graph, paths)
            if newpath is not None:
                return newpath
  
    return jsonify(None)
                
server.run()