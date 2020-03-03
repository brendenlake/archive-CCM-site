# -*- coding: utf-8 -*-
# The typical imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # delete ablater
import random
import math
from copy import deepcopy
from IPython.display import display, Markdown, Latex, HTML
from tabulate import tabulate


class GridWorld():
    
    def __init__(self, gridmap):
        display(Markdown("## Welcome to your new Grid World!"))
        self.gridmap = gridmap
        self.gridmap_flat = [item for sublist in gridmap for item in sublist]
        self.nrows = len(self.gridmap)
        self.ncols = len(self.gridmap[0])
        self.all_states = [] # includes all states, indexed by (i,j) location
        self.all_states_rev = {} # reverse lookup from coordinates to index
        self.valid_states = {} # don't include impossible start states
        self.valid_states_rev = {} # reverse mapping for valid states
        self.transitions = {} # a nested tree of possible transitions
        self.actions = ['up','right','down','left']
        self.actions_num = [0, 1, 2, 3]
        self.start_state_idx = None
        self.start_state_coord = None
        self.goal_state_idx = None
        self.goal_state_coord = None
    
        idx = 0
        for i in range(self.nrows):
            for j in range(self.ncols):
                self.all_states.append((i,j))
                self.all_states_rev[(i,j)]=idx
                if self.gridmap[i][j] == 's':
                    self.start_state_idx = idx
                    self.start_state_coord = (i,j)
                if self.gridmap[i][j] == 'g':
                    self.goal_state_idx = idx
                    self.goal_state_coord = (i,j)                   
                if self.gridmap[i][j] != 'x':
                    self.valid_states[idx]=(i,j)
                    self.valid_states_rev[(i,j)] = idx
                idx += 1
        self.build_transitions()
    
    def coord_to_index(self, coord):
        return self.all_states_rev[coord]
    
    def index_to_coord(self, index):
        return self.all_states[index]
    
    def raw_print(self):
        raw_print_table = []
        for i in range(self.nrows):
            raw_print_row = []
            for j in range(self.ncols):
                raw_print_row.append("%s"%self.gridmap[i][j])
            raw_print_table.append(raw_print_row)
        display(Markdown("**Raw World Layout**"))
        self.pretty_print_table(raw_print_table)
        
    def enumerate_states(self):
        return [i for i in range(len(self.all_states))]
    
    def enumerate_valid_states(self):
        return list(self.valid_states.keys())
    
    def coord_print(self):
        index_printer_table = []
        for i in range(self.nrows):
            index_printer_row = []
            for j in range(self.ncols):
                index_printer_row.append("(%s,%s)"%(i,j))
            index_printer_table.append(index_printer_row)
        display(Markdown("**Indexes of each grid location as a tuple**"))
        self.pretty_print_table(index_printer_table)

    def index_print(self):
        coord_printer_table = np.zeros((self.nrows, self.ncols))
        for i in range(self.nrows):
            for j in range(self.ncols):
                coord_printer_table[i][j] = self.coord_to_index((i,j))
        display(Markdown("**Indexes of each grid location as an id number**"))
        self.pretty_print_table(coord_printer_table)

    def up(self, state):
        i,j = self.index_to_coord(state)
        # if you are goal state or a wall do nothing
        if self.gridmap[i][j]=='x' or self.gridmap[i][j]=='g':
            return state 
        elif (i==0): # if walking of top, return to start state
            return self.start_state_idx
        elif self.gridmap[i-1][j]=='x': # OR if you'll hit a wall do nothing
            return self.coord_to_index((i,j))
        else:
            return self.coord_to_index((i-1,j))

    def down(self, state):
        i,j = self.index_to_coord(state)
        if self.gridmap[i][j]=='x' or self.gridmap[i][j]=='g': #if you are a wall or goal state(do nothing)
            return state
        elif (i==self.nrows-1): # if in bottom row return to start state
            return self.start_state_idx
        elif self.gridmap[i+1][j]=='x': # OR if you'll hit a wall
            return state
        else:
            return self.coord_to_index((i+1,j))
    
    def left(self, state):
        i,j = self.index_to_coord(state)
        if self.gridmap[i][j]=='x' or self.gridmap[i][j]=='g': #if you are a wall or goal state(do nothing)
            return state
        elif (j==0): # if in left-most column return to start state
            return self.start_state_idx
        elif self.gridmap[i][j-1]=='x': #if you'll hit a wall
            return state
        else:
            return self.coord_to_index((i,j-1))

    def right(self, state):
        i,j = self.index_to_coord(state)
        if self.gridmap[i][j]=='x' or self.gridmap[i][j]=='g': #if you are a wall or goal state(do nothing)
            return state
        elif (j==self.ncols-1): # if in right-most column return to start state
            return self.start_state_idx
        elif self.gridmap[i][j+1]=='x': #if you'll hit a wall
            return state
        else:
            return self.coord_to_index((i,j+1))

    def build_transitions(self):
        for i in self.enumerate_valid_states():
            x,y = self.index_to_coord(i)
            if self.gridmap[x][y] != 'x' and self.gridmap[x][y] != 'g': # no transitions for goal or barriers
                self.transitions[i] = {"up": self.up(i), "right": self.right(i), "down": self.down(i), "left": self.left(i)}
            else:
                self.transitions[i] = {}
                
    def pretty_print_table(self, table):
        display(HTML(tabulate(table, tablefmt="html")))
    
    def pretty_print_policy_table(self, policy_table):
        pretty_policy = deepcopy(self.gridmap)
        for i in range(len(self.gridmap)):
            for j in range(len(self.gridmap[i])):
                if self.gridmap[i][j]=='x':
                    pretty_policy[i][j]='▉'
                else:
                    if policy_table[i][j] == {"up": 1.0, "right": 0.0, "down": 0.0, "left": 0.0}:
                        pretty_policy[i][j]='↑'
                    elif policy_table[i][j] == {"up": 0.0, "right": 1.0, "down": 0.0, "left": 0.0}:
                        pretty_policy[i][j]='→'
                    elif policy_table[i][j] == {"up": 0.0, "right": 0.0, "down": 1.0, "left": 0.0}:
                        pretty_policy[i][j]='↓'
                    elif policy_table[i][j] == {"up": 0.0, "right": 0.0, "down": 0.0, "left": 1.0}:
                        pretty_policy[i][j]='←'
        self.pretty_print_table(pretty_policy)

def random_policy():
    policy = {"up": 0.0, "right": 0.0, "down": 0.0, "left": 0.0}
    idx = random.choice(["up","right","down","left"])
    policy[idx]=1.0
    return policy

def zero_q_values():
    qvals = {"up": 0.0, "right": 0.0, "down": 0.0, "left": 0.0}
    return qvals
