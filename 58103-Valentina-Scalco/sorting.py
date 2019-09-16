class sort:
    def bubbleSort(self, lista):
        n = len(lista)
        i = 0
        j = 0
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
