importar  cadena 
alfa  =  cadena . ascii_lowercase

n  =  int ( input ()) 
L  =  [] 
para  i  en el  rango ( n ): 
    s  =  "-" . unirse a ( alfa [ i : n ]) 
    L . agregar (( s [:: - 1 ] + s [ 1 :]) . center ( 4 * n - 3 ,  "-" )) 
print ( ' \ n' . unirse ( L [: 0 : - 1 ] + L ))