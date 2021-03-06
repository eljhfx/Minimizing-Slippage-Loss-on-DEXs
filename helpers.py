import networkx as nx
from Classes import Path, Order, Orderbook
from NetIntegratedClasses import loss_function
import numpy as np, numpy.random

#helper function that randomly allocates liquidity for edges 
def random_allocation_sampler(support_edges, total_liquidity):
    sample = []
    #normalizes random numbers to sum to total liquidity
    a = np.random.random(len(support_edges))
    a /= a.sum()
    a *= total_liquidity

    for i in range(len(support_edges)):
        #appends liquidity for edge[i] in the support
        sample += [support_edges[i] + [a[i]]]

    return sample

def create_samples(support_edges, total_liquidity, num_samples):
    #list of sample liquidity allocations
    samples = []
    for i in range(num_samples):
        samples += [random_allocation_sampler(support_edges, total_liquidity)]

    return samples

def equiv_order_generator(num_tokens):
    orders = []
    for i in range(1, num_tokens + 1):
        j = i + 1
        while (j < num_tokens + 1):
            orders.append(Order(100, str(i), str(j)))
            j += 1

def dense_edge_generator(num_edges):
    edges = []
    for i in range(1, num_edges):
        j = i + 1
        while (j <= num_edges):
            edges.append([str(i), str(j)])
            j += 1
    return edges

def dense_order_book_generator(edges):
    order_book = []
    for e in edges:
        order_book.append(Order(100, e[0], e[1]))

    return order_book


#def get_nodes(order_book): for o in order_book:




    




