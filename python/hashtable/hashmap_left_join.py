from hashtable.hashtable import Hashtable

def hashmap_left_join(hmap1, hmap2):
    result = Hashtable()
    keys = hmap1.keys()
    for key in keys:
        if hmap2.contains(key):
            result.add(key, [hmap1.get(key), hmap2.get(key)])
        else:
            result.add(key, [hmap1.get(key), None])
    return result

#