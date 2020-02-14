#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    # loop through weights adding complements (key), and indices (value)
    # to hash table, also check if pair exists while looping
    for i, weight in enumerate(weights):
        # print('i: ',i)
        # print('weight: ', weight)
        # check if item to be paired with exists
        if hash_table_retrieve(ht, weight) != None:
            i2 = hash_table_retrieve(ht, weight)
            return(i, i2)
            
        complement = limit - weight
        hash_table_insert(ht, complement, i)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
