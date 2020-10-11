'''First assigments: Char cunt
'''

import os
import argparse
import logging
import time
from matplotlib import pylab
import tkinter


def count(filename):
    logging.getLogger().setLevel(logging.INFO)
    file = os.path.abspath(filename)
    logging.info('Full path to your file: %s', file)
    with open(file) as input_file:
        file = input_file.read() #put the book into a string, the with method close the file after the cycle or if there is a problem. No open files wondering in the RAM.
    '''Now I must count the character in this string'''
    alph = dict()
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    for ch in letters: #initialize every character as zero
        alph[ch] = 0
    for keys in alph:
        alph[keys] = file.count(keys)
    '''This block makes an awfull GUI for the graph choice'''
    root = tkinter.Tk() #create the object
    var_y = tkinter.IntVar() #create varuiables
    var_n = tkinter.IntVar()
    tkinter.Label(root, text = "Do you want a graph?").grid(row=0)
    tkinter.Checkbutton(root, text = "yes", variable = var_y).grid(row=1) #this assign a 1 to the variable if the box is checked 0 otherwise
    tkinter.Checkbutton(root, text = "no", variable = var_n).grid(row=2)
    tkinter.Button(root, text='Quit', command = root.destroy).grid(row=3)
    root.mainloop()
    if (var_y.get()==1 and var_n.get()==0):
        ''' This functon makes the histogram of a dictionary if possible'''
        for item in list(alph.values()):
            try:
                item +=1
                item -=1
            except TypeError:
                return 'Not a number-dictionary thing'
        pylab.bar(list(alph.keys()), list(alph.values())/pylab.sum(list(alph.values())))
        pylab.show()
        choice = 'That is a really interesting graph!'
    elif (var_y.get()==1 and var_n.get()==1):
        choice = 'You are a little bit confuse' #just a little bit of practice, useless code
    else:
        choice = 'Hope you liked my program :)'

    print('{}'.format(choice))


if __name__ == "__main__":
    parser = argparse.ArgumentParser( description = 'This program counts character, any problem?')#Parser = "Analyzer"
    parser.add_argument('book', type = str, help = 'Your book') #Create a new argument that is a new "type" of variable with an "help" as a description.
    args = parser.parse_args()
    count(args.book)
    print('Elapsed time: {} sec.'.format(time.process_time())) #Time of run