#sudoku solver

import numpy as np
import time

def findParentBox(index):

    if index[0] < 3:
        if index[1] < 3:
            parent_box = 1
        elif index[1] < 6:
            parent_box = 2
        elif index[1] < 9:
            parent_box = 3

    elif index[0] < 6:
        if index[1] < 3:
            parent_box = 4
        elif index[1] < 6:
            parent_box = 5
        elif index[1] < 9:
            parent_box = 6

    elif index[0] < 9:
        if index[1] < 3:
            parent_box = 7
        elif index[1] < 6:
            parent_box = 8
        elif index[1] < 9:
            parent_box = 9

    return parent_box

def boxValues(board, parent_box):

    if parent_box == 1:
        box_values = board[0:3,0:3]
    elif parent_box == 2:
        box_values = board[0:3,3:6]
    elif parent_box == 3:
        box_values = board[0:3,6:9]
    elif parent_box == 4:
        box_values = board[3:6,0:3]
    elif parent_box == 5:
        box_values = board[3:6,3:6]
    elif parent_box == 6:
        box_values = board[3:6,6:9]
    elif parent_box == 7:
        box_values = board[6:9,0:3]
    elif parent_box == 8:
        box_values = board[6:9,3:6]
    elif parent_box == 9:
        box_values = board[6:9,6:9]

    return box_values

def boxRule(board, trial, index):

    parent_box = findParentBox(index)
    box_values = boxValues(board, parent_box)

    box_values = np.reshape(box_values, (1,9))[0]
    match = np.where(box_values == trial)

    if len(match[0]) > 0:
        match = True
    else:
        match = False

    return match

def rowRule(board, trial, index):

    row_values = board[index[0],:]
    match = np.where(row_values == trial)

    if len(match[0]) > 0:
        match = True
    else:
        match = False

    return match

def columnRule(board, trial, index):

    column_values = board[:,index[1]]
    match = np.where(column_values == trial)

    if len(match[0]) > 0:
        match = True
    else:
        match = False

    return match

def combinedRule(board, trial, index):

    match = boxRule(board, trial, index) or rowRule(board, trial, index) or columnRule(board, trial, index)

    return match

initial =  [[0, 4, 0, 0, 0, 0, 0, 1, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 1, 0, 0, 0, 0, 0, 9, 0]]

initial = np.array(initial, dtype = int)
empty_cells = np.array(np.where(initial == 0))
empty_cells = empty_cells.transpose()
# initialise variables
current_empties = len(empty_cells)
current_index = 0
board = initial
trial = 1

while current_empties > 0:

    index = tuple(empty_cells[current_index])
    match = combinedRule(board,trial,index)

    while trial > 9:

        board[index] = 0
        current_index -= 1
        current_empties += 1
        index = tuple(empty_cells[current_index])

        trial = board[index] + 1
        match = combinedRule(board,trial,index)

    if match == False:  # acceptable value

        board[index] = trial
        current_index += 1
        current_empties -= 1
        trial = 1
        #time.sleep(0.5)

    elif match == True:

        board[index] = trial
        trial +=1

print(board)
