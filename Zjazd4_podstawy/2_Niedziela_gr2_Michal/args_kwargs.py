from matplotlib import pyplot as plt


def basic_args_example():
    def multiply(x, y):
        return x * y

    numbers = [6, 5]
    print(multiply(*numbers))


def plot_based_on_x_y_arrays():
    a = (0, 0)
    b = (0, 3)
    c = (2, 3)
    d = (2, 4)
    points = [a, b, c, d]

    print(list(zip(*points)))

    plt.scatter(*zip(*points))
    plt.plot(*zip(*points))
    plt.show()


def basic_kwargs_example():
    def summarize_person(name: str = "Noname", pesel: str = "00000000000", age: int = 18):
        print(f"{name=}, {pesel=}, {age=}")
    summarize_person(name="Herbert", pesel="92021231245", age=44)

    person = {
        "name": "Halibut",
        "age": 69,
        "pesel": "979343999923"
    }
    summarize_person(**person)
