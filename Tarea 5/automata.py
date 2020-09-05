cadena = '__servidor1'
cadena2 = '4servidor'
def AFD(entrada):
    estado=0
    for letra in range(len(entrada)):
        if estado == 0:
            if entrada[letra]=='_':
                estado = 1
            elif (entrada[letra]== 'a' or entrada[letra]== 'b' or entrada[letra]== 'c'or entrada[letra]== 'd'or entrada[letra]== 'e'or entrada[letra]== 'f'or entrada[letra]== 'g'or entrada[letra]== 'h'or entrada[letra]== 'i'or entrada[letra]== 'j' or entrada[letra]== 'k' or entrada[letra]== 'l'or entrada[letra]== 'm'or entrada[letra]== 'n'or entrada[letra]== 'o'or entrada[letra]=='p'or entrada[letra]== 'q'or entrada[letra]== 'r' or entrada[letra]== 's'or entrada[letra]== 't'or entrada[letra]== 'u'or entrada[letra]== 'v'or entrada[letra]== 'w'or entrada[letra]== 'x'or entrada[letra]== 'y'or entrada[letra]== 'z'):
                estado = 2
            else:
                print('error cadena incorrecta :(')
                return
        elif estado == 1:
            if entrada[letra]=='_':
                estado =1
            elif (entrada[letra]== 'a' or entrada[letra]== 'b' or entrada[letra]== 'c'or entrada[letra]== 'd'or entrada[letra]== 'e'or entrada[letra]== 'f'or entrada[letra]== 'g'or entrada[letra]== 'h'or entrada[letra]== 'i'or entrada[letra]== 'j' or entrada[letra]== 'k' or entrada[letra]== 'l'or entrada[letra]== 'm'or entrada[letra]== 'n'or entrada[letra]== 'o'or entrada[letra]=='p'or entrada[letra]== 'q'or entrada[letra]== 'r' or entrada[letra]== 's'or entrada[letra]== 't'or entrada[letra]== 'u'or entrada[letra]== 'v'or entrada[letra]== 'w'or entrada[letra]== 'x'or entrada[letra]== 'y'or entrada[letra]== 'z'):
                estado=3
            else:
                print('error cadena incorrecta :(')
                return
        elif estado == 2:
            if (entrada[letra]== 'a' or entrada[letra]== 'b' or entrada[letra]== 'c'or entrada[letra]== 'd'or entrada[letra]== 'e'or entrada[letra]== 'f'or entrada[letra]== 'g'or entrada[letra]== 'h'or entrada[letra]== 'i'or entrada[letra]== 'j' or entrada[letra]== 'k' or entrada[letra]== 'l'or entrada[letra]== 'm'or entrada[letra]== 'n'or entrada[letra]== 'o'or entrada[letra]=='p'or entrada[letra]== 'q'or entrada[letra]== 'r' or entrada[letra]== 's'or entrada[letra]== 't'or entrada[letra]== 'u'or entrada[letra]== 'v'or entrada[letra]== 'w'or entrada[letra]== 'x'or entrada[letra]== 'y'or entrada[letra]== 'z'):
                estado = 2
            elif (entrada [letra]=='0'or entrada [letra]=='1'or entrada [letra]=='2'or entrada [letra]=='3'or entrada [letra]=='4'or entrada [letra]=='5'or entrada [letra]=='6'or entrada [letra]=='7'or entrada [letra]=='8'or entrada [letra]=='9'):
                estado=4 
            else:
                print('error cadena incorrecta :(')
                return
        elif estado == 3:
            if entrada[letra]== 'a' or entrada[letra]== 'b' or entrada[letra]== 'c'or entrada[letra]== 'd'or entrada[letra]== 'e'or entrada[letra]== 'f'or entrada[letra]== 'g'or entrada[letra]== 'h'or entrada[letra]== 'i'or entrada[letra]== 'j' or entrada[letra]== 'k' or entrada[letra]== 'l'or entrada[letra]== 'm'or entrada[letra]== 'n'or entrada[letra]== 'o'or entrada[letra]=='p'or entrada[letra]== 'q'or entrada[letra]== 'r' or entrada[letra]== 's'or entrada[letra]== 't'or entrada[letra]== 'u'or entrada[letra]== 'v'or entrada[letra]== 'w'or entrada[letra]== 'x'or entrada[letra]== 'y'or entrada[letra]== 'z':
                estado =3
            elif (entrada [letra]=='0'or entrada [letra]=='1'or entrada [letra]=='2'or entrada [letra]=='3'or entrada [letra]=='4'or entrada [letra]=='5'or entrada [letra]=='6'or entrada [letra]=='7'or entrada [letra]=='8'or entrada [letra]=='9'):
                estado=4
            else:
                print('error cadena incorrecta :(')
                break
    print('cadena correcta :D') 

AFD(cadena)
AFD(cadena2)


