#import numpy as np
def solution(a, b):
    #return int(np.dot(np.array(a), np.array(b)))
    return sum([x*y for x, y in zip(a, b)])