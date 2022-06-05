import itertools as it


def generate_graphs(n):
    """
    Generates the sub-graphs according the the provided input
    :param n: The size of the graph
    :return: graphs: The sub graphs
    """
    graphs = []
    count = []
    output = ""
    file = open("file_n_" + str(n) + ".txt", "w")
    nodes = list(range(1, n + 1))
    all_edges = list(it.product(nodes, nodes))
    edges = [pair for pair in all_edges if pair[0] != pair[1]]
    for all_edges in range(n - 1, n ** 2 - n + 1):
        all_graphs = list(it.combinations(edges, all_edges))
        for graph in all_graphs:
            graph = list(graph)
            if is_graph_exists(graph, graphs, n) and is_graph_valid(graph, nodes):
                graphs.append(graph)
    output = output + f"n= {str(n)}\ncount={str(len(graphs))}\n"
    for graph in graphs:
        motif = len(graph)
        if motif not in count:
            output = output + f"#{str(motif)}\n"
            count.append(len(graph))
        output = output + f"{str(graph)}\n"
    file.write(output)
    file.close()
    return graphs


def is_graph_exists(graph, sub_graphs, n):
    """
    Check if the graph exists in the sub_graphs
    :param graph:The graph to test is exists in list
    :param sub_graphs: The list of sub-graphs
    :param n:The size provided by the user
    :return:True | False
    """
    nodes = range(1, n + 1)
    permutation_list = it.permutations(nodes)
    for edge in permutation_list:
        switched = {i: j for i, j in zip(nodes, edge)}
        sub_graph = tuple((switched[edge[0]], switched[edge[1]]) for edge in graph)
        if sorted(list(sub_graph)) in sub_graphs:
            return False
    return True


def is_graph_valid(graph, nodes):
    """
    The method checks the validity of the graph provided in terms of containing all the nodes provided
    :param graph: a graph object
    :param nodes: a list of nodes
    :return:True | False
    """
    graph_nodes = []
    for i in range(0, len(graph)):
        edge = graph[i]
        for j in range(0, 2):
            node = edge[j]
            if node not in graph_nodes:
                graph_nodes.append(node)
    if nodes == graph_nodes:
        if is_connected(graph, nodes):
            return True
        else:
            return False
    else:
        return False


def is_connected(graph, nodes):
    """
    The method checks the validity of the graph provided in terms of connectivity
    :param graph: a graph object
    :param nodes: a list of nodes
    :return: True | False
    """
    connected_nodes = [nodes[0]]
    for j in range(len(nodes)):
        for i in range(0, len(graph)):
            edge = graph[i]
            node1 = edge[0]
            node2 = edge[1]
            if node1 in connected_nodes and node2 not in connected_nodes:
                connected_nodes.append(node2)
            elif node1 not in connected_nodes and node2 in connected_nodes:
                connected_nodes.append(node1)
    if len(connected_nodes) == len(nodes):
        return True
    else:
        return False


def run_question_1():
    print("The following is a dynamic code\n "
          "Option 1: enter value of n by the user - Press 1\n"
          "Option 2: Run the the code with n=4 - Press 2\n")
    try:
        mode = int(input())
    except Exception:
        mode = 2
        print("Wrong input, none digit value was entered.\n Mode = Option 2")
    if mode == 1:
        print("Please a positive integer representing n\n")
        n = int(input())
    else:
        n = 4
    for graph_size in range(1, n + 1):
        generate_graphs(graph_size)



def run_question_2():
    print("Please insert the number of nodes")
    n = int(input())
    graph = []
    is_running = True
    print("Please enter the directed edges in the format required\n For example:\n1 2\n1 3\n2 3\ndone")
    while is_running:
        try:
            row = input().split(" ")
        except Exception:
            print("Bad Value inserted - re-setting program\n")
            quit()
        if row[0] == "done":
            is_running = False
        else:
            edge = [row[0], row[1]]
            graph.append(edge)

    # Generate graph
    graphs = generate_graphs(int(n))
    good_graphs = []
    for test_graph in graphs:
        is_graph_good = True
        for edge_1 in test_graph:
            is_edge_good = False
            node1 = edge_1[1]
            node2 = edge_1[0]
            for edge_2 in graph:
                node1_valid = edge_2[0]
                node2_valid = edge_2[1]
                if node1 == int(node1_valid) and node2 == int(node2_valid):
                    is_edge_good = True
            if not is_edge_good:
                is_graph_good = False
        if is_graph_good:
            good_graphs.append(test_graph)

    # Parse answer
    edges = len(graph[0])
    new_motif = True
    output = f"count={str(len(good_graphs))}\n"
    for graph in good_graphs:
        if len(graph) != edges:
            new_motif = True
        if new_motif:
            edges = len(graph)
            output = output + f"#{str(edges)}\n"
            new_motif = False
        for edge in graph:
            output = output + f"{str(edge[1])} {str(edge[0])}\n"
    print(output)


def main():
    print("Exercise 1\n")
    is_running = True

    while is_running:
        print("Please insert the digits 1 or 2 to pick which question you wish to run\n"
              "To terminate please enter the digit 9\n")
        try:
            question = int(input())
            if question == 9:
                is_running = False
        except Exception:
            print("Wrong input, question 1 is the default value\n")
            question = 1
        if question == 1:
            run_question_1()
        elif question == 2:
            run_question_2()
        else:
            is_running = False

    print("Terminating program...")


main()
