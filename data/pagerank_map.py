#!/usr/bin/env python

import sys
import numpy

#
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# parses the raw input
for line in sys.stdin:
    res = line.split('\t')
    node = res[0]
    lst = res[1].split(',')
    which_iter = 1
    if isInt(lst[0]):
        which_iter = int(lst[0]) + 1
        curr_rank = lst[1]
        prev_rank = lst[2]
        adj_nodes = lst[3:]
    else:
        curr_rank = lst[0]
        prev_rank = lst[1]
        adj_nodes = lst[2:]



    for link in adj_nodes:
        new_rank = float(curr_rank)/len(adj_nodes)
        # emit the amount of rank a node contributes to a neighbor,
        # the current iteration,
        # and remember this node
        result = str(link).rstrip() + "\t" + str(which_iter) + "," \
            + str(new_rank) + ","\
            + str(node[7:]) + "\n"
        sys.stdout.write(result)

        # its to-be previous rank
    result2 = str(node[7:]).rstrip() + "\t" + str(curr_rank) + "\n"
    # sys.stdout.write(result2)


# dict = {}
# for line in sys.stdin:
#     res = line.split('\t')
#     node = res[0][7:]
#     adj = res[1].split(',')
#     dict[str(node)] = adj
#
# # construct a matrix
# num_nodes = len(dict)
# mat = [[0.0] * num_nodes for _ in range(num_nodes)]
# for key, value in dict.iteritems():
#     num_adj = (len(value)) - 2
#     print key
#     for val in value[2:]:
#         mat[int(key)][int(val)] = float(value[0])/num_adj
#
#
# numpy.dot(











