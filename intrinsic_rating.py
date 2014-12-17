import numpy as np
import scipy as sp
import math
import re
import random
import matplotlib.pyplot as plt

#turn_deltas = ((deltas, player_choice),...,(deltas, player_choice))



#(q, 0-1, 0.05)
#(s, 0-0.7, 0.02)
#(c, 1-5, 0.2)

qs = np.arange(0.0, 1.0,   0.05)
ss = np.arange(0.0, 0.7, 0.02)
cs = np.arange(1.0, 2,   0.20)

#print [(round(x,3),round(y,3),round(z,2)) for x in qs for y in ss for z in cs]
grid = [(s,c) for s in ss for c in cs]

# tm = moves for one turn 
# pt = grid_pt
# up = 1
# down = 0
# straddle = 2

# calculate % of up for a given turn
def turn_probabilities(turn_delta,pt,q):
    tm = turn_delta[0]
    pmove = turn_delta[1]
    gs = map(g,tm,grid_pt = pt)
    s_sum = sum(gs)
    gs = np.array(gs)
    ps = gs/s_sum
    pminus = sum(ps[:pmove])
    pplus = pminus + ps[pmove]
    
    if (pplus <= q):
        updown = 1
    elif (pminus >= q):
        updown = 0
    elif ((pminus < q) & (q < pplus)):
        updown = abs(q-pminus)/ps[pmove]

    return updown

# calculate score for a given q
def game_probabilities(q, turn_deltas, pt):
    updowns = map(turn_probabilities, turn_deltas, pt=pt,q=q)
    R = sum(updowns)/len(updowns)
    mu = (R-q)^2
    return mu

# calculate score for all qs
def percentile_score(pt,turn_deltas,qs):
    percentile_mus = map(game_probabilities,qs,turn_deltas=turn_deltas,pt=pt)
    return sum(percentile_mus)

# minimize score over all s and c vals
def score_minimization(grid, turn_deltas, qs):
    scores = map(percentile_score,grid,turn_deltas=turn_deltas, qs=qs)
    return argmin(scores)


    
        
        
    
def g(delta,pt):
    return numpy.exp(-1 * (delta/pt[0])^(pt[1]))

