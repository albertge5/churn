import os


MAX_ITER = 1

for i in range(MAX_ITER):
    os.system("python pagerank_map.py < email_input.txt | sort | python "
            "pagerank_reduce.py | python process_map.py | sort | python "
            "process_reduce.py > email_output.txt")
    os.system("python pagerank_map.py < email_output.txt | sort | python "
            "pagerank_reduce.py | python process_map.py | sort | python "
            "process_reduce.py > test3.txt")

