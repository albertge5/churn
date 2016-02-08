#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

alpha = 0.85
# this reducer's particular key, since 
# keys are grouped into contiguous blocks
key = ""
rank = 0.0
old_rank = 0.0
adj_list = []

for line in sys.stdin:

    res = line.split('\t')
    node = res[0]
    value = res[1].split(',')
    if len(value) > 1:
        contrib = float(value[0])
        contrib_by = (value[1]).rstrip()

        if node != key:
            if key == "":
                pass
            else:
                # moved onto a new block
                # emit the rank of the previous block
                # here we're using the matrix G = alpha*P + (1-alpha)/n * 1_(n*n)
                # and this is where we finalize the computation pi = piG
                # the second term contributes 1-alpha to every element in the vector
                # of pi, and the first term just multiplies the sum
                # of each node's contribution to an element by alpha
                rank = alpha * (rank) + (1 - alpha)
                sys.stdout.write("NodeId:" + key +\
                        "\t" + str(rank) + "," + str(old_rank) + "," +\
                        ",".join(adj_list) + "\n")
                # reset rank, adj_list
                rank = 0.0
                adj_list = []
            key = node
        rank += float(contrib)
        adj_list.append(contrib_by)
    else:
        old_rank = float(value[0])


