def uladniacz(func):
    def nowa_funkcja_ktora_podmienimy_pod_dekorowana():
        print("Odpalam funkcje add")
        func()
        print("Funkcja add odpalona")
    return nowa_funkcja_ktora_podmienimy_pod_dekorowana


@uladniacz
def add():
    for i in range(50):
        print(i)


add()
