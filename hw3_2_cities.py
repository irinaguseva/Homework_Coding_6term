from random import choice
from time import sleep

class Cities_Game():
    
    def prepare_file(self):
        
        with open('hw3_2_cities_list.txt', 'r', encoding='utf8') as f:
            file = f.readlines()
            
        for i in range(len(file)):
            file[i] = file[i].rstrip('\n')
            file[i] = file[i].lower()

        dic = {}
        for i in range(97, 123):
            dic[chr(i)] = []
        for city in file:
            if city[0] in dic:
                dic[city[0]].append(city)

        self.dic = dic
        
        
    def hello_func(self):
        
        print('Name the City!')
        city = input().lower()
        self.city = city
        

    def game_cycle(self):
        
        city = self.city
        
        while True:

            letter = city[-1]
            try:
                random_city = choice(self.dic[letter])
            except IndexError:
                print("Sorry, I've run out of cities.")
                break
                
            i = self.dic[letter].index(random_city)
            del self.dic[letter][i]
            print('Here you are: ', random_city)
            last_letter = random_city[-1]
            
            sleep(1)
            city = input('Your city: ').lower()

            if not city:
                print('Goodbye!')
                break

            while city[0] != last_letter:
                city = input(f'Hey, give me the city starting with {last_letter}! ') 

game = Cities_Game()
game.prepare_file()
game.hello_func()
game.game_cycle()

