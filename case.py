class MinhaClasse:
    def __enter__(self):
        print("Entrei!!!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sai!!")

with MinhaClasse() as mc:
    print("estou aqui dentro")