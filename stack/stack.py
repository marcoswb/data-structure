class Stack:

    def __init__(self) :
        self.__max = 100
        self.__lenght = 0
        self.__structure = []


    def destroy(self):
        """
        limpa a Stack
        """
        del self.__structure[:]


    def is_full(self):
        """
        Verifica se a Stack está cheia
        """
        return self.__lenght == self.__max


    def is_empty(self):
        """
        Verifica se a Stack está vazia
        """
        return self.__lenght == 0
    

    def push(self, item):
        """
        Insere um item na Stack
        """
        if self.is_full():
            return 'Não é possível inserir pois a Stack está cheia!'
        else:
            self.__structure.append(item)
            self.__lenght += 1
            return 'Elemento inserido!'

    def pop(self):
        """
        Remover um item da Stack
        """
        if self.is_empty():
            return 'Não é possível excluir pois a pilha está vazia!'
        else:
            self.__lenght -= 1
            last_item = self.__structure[self.__lenght]
            self.__structure.pop()
            return last_item


    def print(self):
        """
        Imprime a Stack
        """
        for item in self.__structure:
            print(item)

    
    def lenght(self):
        """
        Retorna o tamanho da Stack
        """
        return self.__lenght