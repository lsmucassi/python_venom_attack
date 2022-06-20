# ************************************************************ #
#                                                              #
#    ░██████╗░██╗██╗░░░██╗░█████╗░███╗░░██╗████████╗           #
#   ██╔════╝░██║╚██╗░██╔╝██╔══██╗████╗░██║╚══██╔══╝            #
#   ██║░░██╗░██║░╚████╔╝░███████║██╔██╗██║░░░██║░░░            #
#   ██║░░╚██╗██║░░╚██╔╝░░██╔══██║██║╚████║░░░██║░░░            #
#   ╚██████╔╝██║░░░██║░░░██║░░██║██║░╚███║░░░██║░░░            #
#   ░╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░            #
#                                                              #
#   club_namegen.py                                            #
#   By: r3b31 <lindasmucassi@gmail.com>                        #
#   Created: 2022/06/20 16:30:11 by r3b31                      #
#   Updated: 2022/06/20 16:30:11 by r3b31                      #
#                                                              #
# ************************************************************ #

'''
DAY 1:
    Create an application that will generate a club name based on the users input
        - Ask the user to enter the town, township, village or city they are from
        - ask the user to choose between entering a Hobby, Fruit, Vegetable, Plant, Animal or Natuaral landscape 
        - Ask the user to enter their Pet name
        - Generate a club name using a random combination of the three
'''
import random

def main():
    club_name = []

    # - Ask the user to enter the town, township, village or city they are from
    city_name = input("Enter the name of the City/Township/Town/Village you stay in: \n")

    # - ask the user to choose between entering a Hobby, Fruit, Vegetable, Plant, Animal or Natuaral landscape 
    fun_name = input("Enter your Hobby or favourite Animal/Fruit/Veg/Plant/Natual Landscape: \n")

    # - Ask the user to enter their Pet name
    pet_name = input("Enter the name of your pet: \n")

    # - Generate a club name using a random combination of the three
    # firstly save all the inputs inside one list and print the list randomly, that will be the results
    club_name = [city_name, fun_name, pet_name]
    random.shuffle(club_name)
    # print results
    print("Your club name: ", " ".join(club_name))

if __name__ == "__main__":
    main()