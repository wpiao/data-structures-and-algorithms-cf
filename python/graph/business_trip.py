def business_trip(g, input_cities):
    cost = 0
    normalized_input_cities = [city.lower() for city in input_cities]
    city_node_list = g.get_node()
    cities_in_graph = {}
    for city_node in city_node_list:
        cities_in_graph[city_node.value.lower()] = city_node
    for idx, city in enumerate(normalized_input_cities):
        if idx + 1 < len(normalized_input_cities):
            if city in cities_in_graph:
                next_city = normalized_input_cities[idx + 1]
                neighbor_city_nodes_list = g.adjacency_list[cities_in_graph[city]]['nodes']
                is_input_cities_connected = False
                for neighbor_city_node in neighbor_city_nodes_list:
                    if neighbor_city_node[0].value.lower() == next_city:
                        cost += neighbor_city_node[1]
                        is_input_cities_connected = True
                        break
                if is_input_cities_connected:
                    is_input_cities_connected = False
                else:
                    cost = 0
                    break
            else:
                cost = 0
                break

    if cost == 0:
        return False, f'${cost}'
    else:
        return True, f'${cost}'
