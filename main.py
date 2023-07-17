from split_audio import * 
from export_mir_2 import *
from load_data import *
import pandas as pd
import os

dir_db = '../../db/dataset/'
dir_data = str( os.getcwd() ) + '/'
print( dir_data )

stat = 'mean'
splits = [ 'complete', 'begin', 'end', 'middle', 'middle_1', 'middle_2' ] 
genres = [ 'andino', 'brega', 'carimbo', 'cumbia', 'merengue', 'pasillo', 'salsa', 'vaqueirada' ]

dim = 125

seconds = 10
for rth in genres:
    for sp in splits:
        archive = 'db_' + str(seconds) + '_' + rth + '_' + stat + '_' + sp
        print( archive, sp )
        db_aux1 = load_variable( dir_data + dir_db , archive  )
#        print( rth, db_aux1.shape )
        if db_aux1.shape[0] >= dim:
            db_aux1 = db_aux1.iloc[0:dim,:]
 #       else:
  #          print( rth, sp,' has data lower than permited!' )

        if rth == genres[0] and sp == splits[0]:
            db_all_genre = db_aux1                
        else:
            db_all_genre = db_all_genre.append( db_aux1, ignore_index=False, verify_integrity=False, sort= None ) 
        print( rth, db_aux1.shape, db_all_genre.shape )

print( 'Dataset of musical genres', genres, 'with splits', splits, 'has the total of:', db_all_genre.shape )
print( db_all_genre.head() )
