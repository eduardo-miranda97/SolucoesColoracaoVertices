from graph import generate_graph
from grasp import grasp


def test_grasp():
    _, graph = generate_graph(100, 0.5)

    solution = grasp(graph, use_path_relinking=False)
    print(solution.colors_count, solution.node_order)

    solution = grasp(graph, use_path_relinking=True)
    print(solution.colors_count, solution.node_order)


if __name__ == '__main__':
    test_grasp()
