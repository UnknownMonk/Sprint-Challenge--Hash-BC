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

    available_ticket = None
    # for every ticket in tickets
    # add it to the hash table key = starting_airport, value = next_airport
    for i in range(length):
        starting_airport = tickets[i].source
        next_airport = tickets[i].destination

        hash_table_insert(ht, starting_airport, next_airport)

        # The ticket for your first flight has a destination with a starting_airport of "NONE"
        if starting_airport == "NONE":
             # find the next destination
            available_ticket = next_airport
            # set as starting location
            route[0] = available_ticket

    for i in range(1, length):
        next_destination = hash_table_retrieve(ht, available_ticket)
        route[i] = next_destination
        # set as next destination
        available_ticket = next_destination

    return route
