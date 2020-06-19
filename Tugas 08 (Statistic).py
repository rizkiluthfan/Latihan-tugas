# TUGAS 

list_angka = [1,3,3,3,4,4,2,4,10]

print(list_angka)

# Mean 

def mean(list_angka):
    n = len(list_angka)
    mean = sum(list_angka)/n
    return mean

mean(list_angka)

# Median

def median(list_angka):
    n = len(list_angka)
    list_angka.sort()
    if n % 2 == 0: 
        median1 = list_angka[n//2] 
        median2 = list_angka[n//2 - 1] 
        median = int((median1 + median2)/2)
        return median
    else: 
        median = list_angka[n//2] 
        return median

median(list_angka)

# Mode

import collections

def mode(list_angka):
    data = collections.Counter(list_angka)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode) != len(list_angka):
        return mode
    else:
        print ('no mode')   
       
mode(list_angka)

# Variance

def variance(list_angka):
    n = len(list_angka)
    m = sum(list_angka) / n
    var = sum((xi - m) ** 2 for xi in list_angka) / n
    return var
    
variance(list_angka)

# Stdev

import math

def stdev(list_angka):
    
    stdev = math.sqrt(variance(list_angka))
    return stdev

stdev(list_angka)

# Skewness

def skewness(list_angka):
    n = len(list_angka)
    m = sum(list_angka) / n
    skew1 = sum((xi - m) ** 3 for xi in list_angka) / n
    skew2 = (stdev(list_angka) **3)
    skew = skew1/skew2
    return skew

skewness(list_angka)

# Excess Kurtosis

def excesskurtorsis(list_angka):
    n = len(list_angka)
    m = sum(list_angka) / n
    exckur1 = sum((xi - m) ** 4 for xi in list_angka) / n
    exckur2 = (stdev(list_angka)) ** 4
    exckur = exckur1/exckur2 - 3
    return exckur
    
excesskurtorsis(list_angka)

# Statistic Sample

stat = []

def statistic_sample(list_angka, stat):
    
    if stat == 'mean':
        return(mean(list_angka))

    elif stat == 'median':
        return(median(list_angka))
    
    elif stat == 'mode':
        return(mode(list_angka))
    
    elif stat == 'variance':
        return(variance(list_angka))
    
    elif stat == 'stdev':
        return(stdev(list_angka))
    
    elif stat == 'skewness':
        return(skewness(list_angka))

    elif stat == 'excesskurtorsis':
        return excesskurtorsis(list_angka)
    
    else : 
        return 'error'

print(statistic_sample(list_angka, 'excesskurtorsis'))
