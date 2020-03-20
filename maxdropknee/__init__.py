import numpy as np
import math


def angle(b,c):
    tan = math.degrees(math.atan(abs(c-b)))
    if c>b: return 90+tan
    return 90-tan

def angles(a,b,c):
    r1=angle(b,a)
    r2=angle(b,c)
    return r1+r2

def maxdropknee(values, smooth=3):  
    """ 
       avg left+right -> minumize angle 
    """
    valz = [ np.mean(values[i:i+smooth]) for i in range(len(values)-smooth)]
    
    scores = []
    for i,v in enumerate(values[smooth:-smooth-1]):
        i+=smooth
        x= valz[i-smooth]
        z=valz[i+1]
        ang = angles(x,v,z)
        scores.append(ang) 
        
    return np.argmin(scores+smooth)



def paper_angle_based(values):
    # INITIALIZE
    cur,pre,aft = [values[0]]*3

    # GET DIFFs
    diffs = []
    for i,m in enumerate(range(cmin, cmax)):
        cur = values[i]
        aft = values[i+1]
        diffs.append((i, m, pre+aft-2*cur ))
        pre = cur

    # find local minima in diff function
    locmin = [ v for i,v in enumerate(diffs[:-1])
            if diffs[i][2] < diffs[i-1][2] and diffs[i][2] < diffs[i+1][2] ]


    # for each n with decreasing order of localmin value ( is this bic or diff?)
    locmin.sort(key= lambda x: x[2], reverse=True) # decreasing order of locmin

    cur = -999999999
    lastm = -1
    their_angle = lambda a,b,c: math.atan(1/abs(b-a)) + math.atan(1/abs(c-b))
    for i,m,v in locmin:
        a = their_angle(*values[i-1:i+2])

        if a < cur:
            break
        else:
            cur = a
            lastm = m
    else:
        print("something went wrong")
    
    return lastm


   
