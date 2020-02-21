import numpy as np
def maxdropknee(values):  

    # every value gets a score, 
    # if it goes up: nextvalue-v
    # if it goes down: nextminimum - value
    # return minimum of scores
    
    scores = []
    for i,v in enumerate(values[:-1]):
        if values[i+1] > v:
            scores.append(values[i+1]-v)
        else:
            rest = values[i+1:]
            if rest:
                cur  =  v
                for e in rest:
                    if e < cur: # next value is smaler. continue
                        cur = e
                    else: # next value is larger, break
                        break 
                scores.append(cur-v)

    '''
    from matplotlib import pyplot as plt
    res=[0]*len(values)
    res[np.argmin(scores)]= -2000
    plt.plot(values)
    plt.plot(scores)
    plt.plot(res)
    plt.show()
    '''
    return np.argmin(scores)
   
