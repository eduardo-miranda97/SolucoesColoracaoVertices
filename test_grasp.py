from graph import generate_graph
from grasp import grasp


def test_grasp():
    _, graph = generate_graph(10, 0.5)
    grasp(graph)


if __name__ == '__main__':
    test_grasp()
