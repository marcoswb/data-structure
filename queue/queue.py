class Queue:

    def __init__(self) :
        self.__max = 10
        self.__first = 0
        self.__last = 0
        self.__structure = {}


    def is_full(self):
        """
        Verifica se a Queue está cheia
        """
        result = (self.__last - self.__first) == self.__max
        return result


    def is_empty(self):
        """
        Verifica se a Queue está vazia
        """
        result = self.__first == self.__last
        return result
    

    def push(self, item):
        """
        Insere um item na Queue
        """
        if self.is_full():
            return 'Não é possível inserir pois a Queue está cheia!'
        else:
            last_position = self.__last % self.__max
            self.__structure[last_position] = item
            self.__last += 1
            return 'Elemento inserido!'

    def pop(self):
        """
        Remover um item da Queue
        """
        if self.is_empty():
            return 'Não é possível excluir pois a Queue está vazia!'
        else:
            first_position = self.__first % self.__max
            print(self.__first, first_position)
            first_item = self.__structure[first_position]
            del self.__structure[first_position]
            self.__first += 1
            return first_item


    def print(self):
        """
        Imprime a Queue
        """
        for key in self.__structure.keys():
            print(self.__structure[key])
