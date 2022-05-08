def export_mir_2( dir, rithm, statistic, split, seconds, min_seconds, max_seconds, output ):
    #salsa, cumbia, carimbo, merengue, vaqueirada
    #rithm = 'marabaixo' # prox

    #dir_audio = dir_data + 'musics/' + rithm + '/'
    dir_audio = dir + rithm + '/'
    
    files = read_fold( dir_audio )
    print( "[Files] ", len(files), files )

    files_out = 0
    err_count_load = 0
    for row, file in enumerate( files ):
        
        ######### importar audio #########
        if file.find(".") != -1 :         # retira diretorios
        #if file.find(".") != -1 and file.find(".wav") != -1 : # apenas wav
          print( "[Extrac]", rithm, row, len(files), file, split )   

          try:
            #audio, sr = librosa.load( dir_fma + '001/' +'001483.mp3', mono = True )
            x, sr = librosa.load( dir_audio + file, sr=None, mono=True )              
          except:             
            err_count_load += 1
            print( Fore.RED + '[Err]' + Fore.BLACK, 'File on Unknow format:', file, '\t partial error:', err_count_load )
            #if type('texto') == type(audio):
            #  err_count_load += 1
            #  print( 'Not loaded', err_count_load )
            continue
          

          audio_size = get_duration( x, sr )
          if audio_size < min_seconds or audio_size > max_seconds: 
            print( Fore.RED + '[Out]    ', file, audio_size, '-----', Fore.BLACK )
            files_out += 1
            continue 
          
          
          if split != 'complete':
            x = split_audio( x, sr, split, seconds )
          sample = x   
          #print( '[Duract]', rithm, row, len(files), file, round(audio_size,3), round(get_duration(x,sr), 3) )
          print( '[Durati]', round(audio_size,3), ' extracting features by:', round(get_duration(x,sr), 3), ' seconds' )
          
          name = []                    
          colunas = []
          media = []
              
          #if row == 0:
              ## classe arquivo
          name.append( "classe" )
          name.append( "arquivo" )
          colunas.append( "classe" )
          colunas.append( "arquivo" )    
          media.append( rithm )
          media.append( file[:-4] )
          #media.append( files[row][:-4] )

          #name.append( "divisao" )
          #colunas.append( "divisao" )   

          name.append( 'divisao' )
          colunas.append( 'divisao')          
          media.append( split )
          #df[name] = 'teste'                 

          ###################### fourier tempogram #####
          colunas.append( "fourier_tempogram" )    
          four_tempog = librosa.feature.fourier_tempogram( y=sample, sr=sr )

          for i in range (four_tempog.shape[0]):    
              ###if row == 0:
              name.append( 'fourier_tempogram-' + statistic + str(i) )
              #media.append( np.mean(four_tempg[i,:] ) )    
              media.append( statistics_values( four_tempog[i,:], statistic ) )    


          df = pd.DataFrame( media )
          df = df.transpose()
          ##if row == 0:
          df.columns = name
           

          #################### tempogram ###############
          colunas.append("tempogram")
          tempog = librosa.feature.tempogram( y=sample, sr=sr )
          #print( tempog.shape )
          for i in range ( tempog.shape[0] ):                            
              value = statistics_values( tempog[i,:], statistic ) 
              name = 'tempogram-'+ statistic + str(i)  
              df[name] = value               
              

          ############ chroma bandwidth ######    
          colunas.append("chroma_stft")
          chrom_stft = librosa.feature.chroma_stft(y = sample, sr = sr, n_fft=2048, hop_length=512 )
          for i in range ( chrom_stft.shape[0] ):                  
              value = statistics_values( chrom_stft[i,:], statistic ) 
              name = 'chroma_stft-'+ statistic + str(i)
              df[name] = value            
              

          ######### chroma cens  ###########
          colunas.append("chroma_cens")
          chrom_cens = librosa.feature.chroma_cens(y = sample, sr = sr, hop_length=512 )
          for i in range ( chrom_cens.shape[0] ):                      
              value = statistics_values( chrom_cens[i,:], statistic ) 
              name = 'chroma_cens-' + statistic + str(i)
              df[name] = value            
              

          ######## chroma cqt #############
          colunas.append("chroma_cqt")
          chrom_cqt = librosa.feature.chroma_cqt(y = sample, sr = sr, hop_length=512 )
          for i in range ( chrom_cqt.shape[0] ):               
              value = statistics_values( chrom_cqt[i,:], statistic ) 
              name = 'chroma_cqt-' + statistic + str(i)
              df[name] = value            
              

          ###### mel spectgram #######  128 dados
          colunas.append("mel")    
          mel = librosa.feature.melspectrogram( y = sample, sr=sr, n_mels=128 )
          for i in range ( mel.shape[0] ):                   
              value = statistics_values( mel[i,:], statistic ) 
              name = 'mel-' + statistic + str(i)
              df[name] = value
              

          ########## mfcc ######## mel frequency 20 conteudos
          colunas.append("mfcc")  
          mfcc = librosa.feature.mfcc( y=sample, sr=sr, n_mfcc=20 )
          for i in range ( mfcc.shape[0] ):                             
              value = statistics_values( mfcc[i,:], statistic ) 
              name = 'mfcc-' + statistic + str(i)
              df[name] = value
              

          ######## tonez ######## 6 conteudos
          colunas.append("tonnetz")  
          tonnetz = librosa.feature.tonnetz( y=sample, sr=sr)
          for i in range ( tonnetz.shape[0] ):                
              value = statistics_values( tonnetz[i,:], statistic ) 
              name = 'tonnetz-' + statistic + str(i)
              df[name] = value            
              

          ########## rms ########## 1 conteudo
          colunas.append( "rms" )
          rms = librosa.feature.rms( y=sample )
          for i in range ( rms.shape[0] ):                  
              value = statistics_values( rms[i,:], statistic ) 
              name = 'rms-' + statistic + str(i)
              df[name] = value                 
              

          ########## zcr #########  1 conteudo
          colunas.append("zcr")  
          zcr = librosa.feature.zero_crossing_rate( y = sample )
          for i in range ( zcr.shape[0] ):                   
              value = statistics_values( zcr[i,:], statistic ) 
              name = 'zcr-' + statistic + str(i)
              df[name] = value            
          ############ zcr sum ###########
          value = np.sum( zcr, axis= 1 )[0]
          name = 'zcr-' + 'sum' + str(i)
          df[name] = value


          ############# roll ###########
          colunas.append("roll_off")
          porcent = [0.01, 0.85, 0.99]
          for p in porcent:
              roll = librosa.feature.spectral_rolloff( y= sample, sr= sr, n_fft= 2048, roll_percent = p )  
              value = statistics_values( roll[0,:], statistic ) 
              name = 'roll_off-' + statistic + str(p)
              df[name] = value          
              
          ############# spectral bandwidth 2--12 ###########
          colunas.append("spectral_centroid")
          centroid = librosa.feature.spectral_centroid( y=sample, sr= sr )
          value = statistics_values( centroid[0, :], statistic ) 
          name = 'spectral_centroid-' + statistic + str(0)
          df[name] = value 

          colunas.append("spectral_bandwidth")
          for i in range ( 2, 12 + 1 ):   
              band = librosa.feature.spectral_bandwidth( y= sample, sr= sr, p= i )            
              value = statistics_values( band[0, :], statistic ) 
              name = 'spectral_bandwidth-' + statistic + str(i)
              df[name] = value 
                  
          if row == 0:
              df_out = df
          else:
              df_out = df_out.append( df, ignore_index=True ).copy()
              #pd.concat( [df_out, df], ignore_index=True )

    print( Fore.GREEN + "[Atributos]", colunas )
    print( Fore.RED + '[Excluidos]' + Fore.BLACK, files_out, '\t total:', len(files)-files_out )
    print( Fore.RED + '[Not loaded]', Fore.BLACK, err_count_load )
    #df_out.head() 
    save_variable( dir +'../db/', output , df_out )
    return df_out
