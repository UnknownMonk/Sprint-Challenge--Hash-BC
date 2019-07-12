#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    if length <= 1:
        return None

    ht = HashTable(length)

    for i in range(length):
        # check if a key (element from weights arr) is already in hash table
        key_exist = hash_table_retrieve(ht, weights[i])
        if (key_exist == 0 or key_exist) and (limit - weights[i] == weights[i]):
            # 2 same elements, each equal to limit/2 => element + element = limit
            return (i, key_exist)
        hash_table_insert(ht, weights[i], i)

    # placeholder for keys that sum to limit
    keys = []

    # search for key, which adds to limit with another key => limit-key = another key
    for i in range(length):
        key_value = hash_table_retrieve(ht, limit-weights[i])
        if key_value:
            keys.append(weights[i])
            keys.append(limit-weights[i])
            break

    indexes = [weights.index(keys[0]), weights.index(keys[1])]
    indexes.sort(reverse=True)

    return (indexes[0], indexes[1])


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
