# malongyu 2300930
import numpy as np

def seita_k(s,K,y,fai):
    result = s + K*(y-(fai.T)@s)
    return result

def K_k(P,fai):
    result = P@fai/(1+ (fai.T)@P@fai)
    return result

def P_k(K,fai,P):
    result = (np.eye(4)- K@(fai.T) )@P

    return result
