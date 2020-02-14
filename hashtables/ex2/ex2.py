#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        try:
            hash_table_insert(ht, str(ticket.source), str(ticket.destination))
        except:
            head = ticket
    

    route[0] = head
    counter = 1
    prev = head.destination
    while prev != None:
        prev = route[counter-1]
        route[counter] = hash_table_retrieve(ht, str(prev))
        counter += 1

    return route
