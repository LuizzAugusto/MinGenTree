#! /usr/bin/env python3
from sys import argv as arguments
import SimpleFile
import re
import json
import csv



def execute(arguments):
    filename1 = arguments[1]
    filename2 = arguments[2]
    vtx1 = arguments[3]
    vtx2 = arguments[4]

    text = _loadFile(filename1)

    if text:
        text = _preProcessing(text)
        positions = _convertion(text)
        json_dict = _structuringConnections(filename2, positions, vtx1, vtx2)
        json_dict = _addRedundance(json_dict)
        SimpleFile.write(f"{filename1[:-3]}json", json.dumps(json_dict))


def _loadFile(filename):
    text = SimpleFile.read(filename)

    if text != None:
        return text
    else:
        print('Error, file not found!')
        return None

def _preProcessing(text):
    new_text = ''

    while text[-1] == '\n' or text[-1] == ' ':
        text = text[:-1]

    for line in text.split('\n'):
        line = re.sub('[^(0-9)]*', '', line, count=1)
        
        while line[-1] == ' ':
            line = line[:-1]
        
        new_text += line + '\n'

    new_text = new_text[:-1]
    
    return new_text

def _structuringConnections(filename, positions, vtx1, vtx2):
    json_dict = {}
    
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            vertex1, vertex2 = row[vtx1], row[vtx2]
            distance = _getDistance(positions, vertex1, vertex2)

            if vertex1 not in json_dict:
                json_dict[vertex1] = {}
            
            json_dict[vertex1][vertex2] = distance
    return json_dict

def _convertion(text):
    positions = {}
    
    for line in text.split('\n'):
        vertex, x, y = line.split(' ')

        positions[vertex] = {'x':float(x),'y':float(y)}

    return positions

def _addRedundance(json_dict):
    for vertex in json_dict:
        for next_vertex in json_dict[vertex].keys():
            
            if vertex not in json_dict[next_vertex]:
                json_dict[next_vertex][vertex] = float(json_dict[vertex][next_vertex])

    return json_dict

def _getDistance(positions, vertex1, vertex2):
    x1 = positions[vertex1]['x']
    x2 = positions[vertex2]['x']
    y1 = positions[vertex1]['y']
    y2 = positions[vertex2]['y']

    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

if __name__ == '__main__' and len(arguments) > 4:
    execute(arguments)