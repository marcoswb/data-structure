from queue import Queue


class Main():

    def __init__(self):
        queue = Queue()
        self.__item = 0
        self.__option = -1
        
        print('Iniciando algoritmo de Queue...')

        while self.__option != 0:
            self.menu()
            self.__option = int(input('Digite sua opção: '))
            if self.__option == 1:
                self.__item = input('Digite o item a ser inserido: ')
                print(queue.push(self.__item))
            elif self.__option == 2:
                print(f'item {queue.pop()} apagado.')
            elif self.__option == 3:
                queue.print()


    
    def menu(self):
        print('Digite 0 para sair do loop!')
        print('Digite 1 para inserir um elemento!')
        print('Digite 2 para remover um elemento!')
        print('Digite 3 para imprimir a fila!')


if __name__ == '__main__':
    Main()