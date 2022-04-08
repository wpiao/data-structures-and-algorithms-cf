import enum


def business_trip(g, cities):
    is_connected = False
    cost = 0
    city_node_list = g.get_node()
    city_list = []
    for city_node in city_node_list:
        city_list.append(city_node.value.lower())
    for idx, city in enumerate(cities):
        if idx == 0:
            continue
        if city in city_list:
            pass
