# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)

import copy

state = {'json': None, 'value': None}

def start(default_values):
    nodes = state['json']
    result = []
    iterable = iter(default_values)

    for value in iterable:
        result.append([int(value), next(iterable), next(iterable)])

    if default_values:
        del default_values[0]

    if nodes:
        default_values = _setDefaultValues(nodes, default_values)
        result = _algorithm(nodes, default_values, result)
        total_cost = sum(path[0] for path in result)
        print(result)
        print('total cost: ' + str(total_cost))
    else:
        print('open a JSON file first.')

def _algorithm(nodes, values, result):

    while _valuesAreNotInSet(values, nodes.keys()):
        min_weight_path = _minWeight(nodes, values)

        if min_weight_path[1] not in values:
            values.append(min_weight_path[1])

        result.append([min_weight_path[0]] + min_weight_path[2])

    return result

def _minWeight(nodes, values):
    min_weight_path =  _defineFirstMinWeight(nodes, values)

    for key in values:
        for k in nodes[key]:
            weight = nodes[key][k]

            if weight < min_weight_path[0] and (k not in values):
                min_weight_path[0] = weight
                min_weight_path[1] = k
                min_weight_path[2] = [key,k]
    
    return min_weight_path

def _valuesAreNotInSet(values, node_keys):
    return bool(set(node_keys) - set(values))

def _setDefaultValues(nodes, default_values):
    if not default_values:
        default_values = [list(nodes.keys())[0]]

    return default_values

def _defineFirstMinWeight(nodes, values):
    node_values = []
    
    for key in values:
        node_values += list(nodes[key].values())
        maximum = max(node_values)

    max_node = None

    for key in values:
        node = nodes[key]

        for weight in node.values():
            if weight == maximum:
                max_node = key
        
            if max_node:
                break

    return [maximum, max_node, None]