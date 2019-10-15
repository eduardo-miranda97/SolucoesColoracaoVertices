from graph import generate_graph, uni_to_bi
from grasp import grasp


def test_grasp():
    _, graph = generate_graph(10, 0.5)
    graph = uni_to_bi(graph)
    grasp(graph)


if __name__ == '__main__':
    test_grasp()
