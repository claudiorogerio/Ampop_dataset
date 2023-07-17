'''
ler lista de arquivos wav's
'''
def read_fold( folder ):
    import os
    return os.listdir( folder )

def save_variable( directory, name_out, variable ):
    import pickle
    f = open( directory + name_out, 'wb' )
    pickle.dump( variable, f )
    f.close()

def load_variable( directory, name_in ):
    try:
      import pickle
      f = open( directory + name_in, 'rb' )
      aux = pickle.load(f)
      f.close()
      return aux
    except:
      return False

## retorna valores estatisticos para um vetor de entrada
# types - mean, median, min, max, std, mode
def statistics_values( data, types ):
    import numpy as np
    if types == 'mean':
        return np.mean( data )
    if types == 'median':
        return np.median( data )
    if types == 'min':
        return np.min( data )
    if types == 'max':
        return np.max( data )
    if types == 'std':
        return np.std( data )
    if types == 'mode':
        from scipy import stats
        return stats.mode( data )[0][0] # retorna apenas o valor

#print( statistics_values( [1,2,2,3,4,1,1], 'sd') )

