## @brief: funcao que retorna recorte de audio mono a partir de uma posicao especifica
## data - audio file
## sr - sample rate
## split - posicao de recorte ['begin', 'middle', 'middle_1', 'middle_2', 'end' ]
##    begin    - a partir do inicio
##    middle   - valor central da musica
##    middle_1 - a partir de um ponto para o centro musica
##    middle_2 - do centro para o final da musica
## sec - segundos de recorte
def split_audio( data, sr, split, sec ):
  dim_audio = len(data)  #dim do arquivo em segundos
  frame_new = int(sec*sr)  # dimensao do novo arquivo 10, 20, 30s ...

  if split == 'begin':  # a partir do inicio, cria um arquivo de sec    
    pos_0 = 0
    pos_n = frame_new
    if frame_new > dim_audio:     
      pos_n = int( dim_audio )    
    
  if split == 'middle':     # da posicao central
    p_central = dim_audio/2
    pos_0 = int( p_central - frame_new/2 )
    pos_n = int( p_central + frame_new/2 )
    if pos_n > dim_audio: pos_n = int( dim_audio ) # informar o valor medio
  
  if split == 'middle_1':     # da posicao central para o inicio
    p_central = dim_audio/2
    pos_0 = int( p_central - frame_new )
    pos_n = int( p_central )
    if pos_0 < 0 : pos_0 = int(0) # informar o valor medio

  if split == 'middle_2':     # da posicao central para o final
    p_central = dim_audio/2
    pos_0 = int( p_central )
    pos_n = int( p_central + frame_new )
    if pos_n > dim_audio: pos_n = int( dim_audio ) # informar o valor medio
  
  if split == 'end':
    pos_0 = int( dim_audio - frame_new )
    pos_n = int( dim_audio )
    if pos_0 < 0 : pos_0 = int(0)   # informar um novo frame maior que o audio

  return data[pos_0 : pos_n]

### example
#audio2 = split_audio( audio, sr, 'middle', 10 )
