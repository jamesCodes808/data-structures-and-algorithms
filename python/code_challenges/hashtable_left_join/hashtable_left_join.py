from data_structures.hashtable import Hashtable

def left_join(hashmap_syn, hashmap_ant):
    # Takes in 2 hashmaps
    # Both have strings as keys
    # 1 has synonym of string key as value
    # 1 has antonym of string key as value
    results = list()

    for left_key,left_value in hashmap_syn.items():
        joined_list = [left_key, left_value]
        if left_key in hashmap_ant.keys():
            right_value = hashmap_ant.get(left_key)
            if right_value is not None:
                joined_list.append(right_value)
        else:
            joined_list.append('NONE')

        results.append(joined_list)

    return results
