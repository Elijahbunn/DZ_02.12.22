from random import randint

#list_test = ['Elijah', 'Bunin', 'slime']

def number_charactristic (list1):
    if list1[2] == 'human' or list1[2] == 'pangolin':
        list1.extend([randint(0, 20), randint(20, 50), randint(10, 30), randint(10, 20),
                        randint(20, 40), randint(0, 20)])
    elif list1[2] == 'orc' or list1[2] == 'werewolf' or list1[2] ==  'giant':
        list1.extend([randint(40, 80), randint(0, 30), randint(20, 30), randint(0, 15),
                        randint(0, 15), randint(0, 10)])
    elif list1[2] == 'dwarf' or list1[2] == 'goblin':
        list1.extend([randint(30, 60), randint(30, 60), randint(30, 70), randint(0, 15),
                        randint(20, 40), randint(0, 10)])
    elif list1[2] == 'elf' or list1[2] == 'technocrat' or list1[2] == 'essence':
        list1.extend([randint(10, 30), randint(40, 80), randint(30, 70), randint(30, 70),
                        randint(30, 60), randint(30, 60)])
    elif list1[2] == 'slime' or list1[2] == 'spirit' or list1[2] == 'deity':
        list1.extend([randint(10, 30), randint(30, 60), randint(10, 70), randint(20, 50),
                        randint(2, 50), randint(40, 80)])
    
#number_charactristic (list_test)

#print(list_test)