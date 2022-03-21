import random
if __name__ == '__main__':
    def dec():
        list = ['Sim', 'Não']
        list2 = random.choice(list)
        return(list2)
    print (dec())