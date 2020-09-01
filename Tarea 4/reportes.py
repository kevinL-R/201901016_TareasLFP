import webbrowser

def reportar(lista_nombre, lista_edades, lista_activo, lista_saldo):
    with open('reporte.html', 'w') as myFile:
        myFile.write('<!DOCTYPE html>')
        myFile.write('<html>')
        myFile.write('<head>')
        myFile.write('<meta charset="utf-8">')
        myFile.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
        myFile.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
        myFile.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
        myFile.write('<link href="https://fonts.googleapis.com/css?family=Kaushan+Script" rel="stylesheet" type="text/css">')
        myFile.write('<link href="estilo.css" type="text/css" rel="stylesheet" media="">')
        myFile.write('</head>')
        myFile.write('<body>')
        myFile.write('<center>')
        myFile.write('<header>')
        myFile.write('Reporte')
        myFile.write('</header>')
        myFile.write('<div>')
        myFile.write('<table border="1" class="table table-dark">')
        myFile.write('<tr align="center">')
        myFile.write('<th scope="col">Nombre</th>')
        for nom in lista_nombre:
            myFile.write('<td>')
            myFile.write(nom)
            myFile.write('</td>')
        myFile.write('</tr>')
        myFile.write('<tr align="center">')
        myFile.write('<th scope="col">Edad</th>')
        for eda in lista_edades:
            myFile.write('<td>')
            myFile.write(eda)
            myFile.write('</td>')
        myFile.write('</tr>')
        myFile.write('<tr align="center">')
        myFile.write('<th scope="col">Activo</th>')
        for act in lista_activo:
            myFile.write('<td>')
            myFile.write(act)
            myFile.write('</td>')
        myFile.write('</tr>')
        myFile.write('<tr align="center">')
        myFile.write('<th scope="col">Saldo Q.</th>')
        for saldo in lista_saldo:
            myFile.write('<td>')
            myFile.write(saldo)
            myFile.write('</td>')
        myFile.write('</tr>')
        myFile.write('</table>')
        myFile.write('</div>')
        myFile.write('</center>')
        myFile.write('</body>')
        myFile.write('</html>')
    webbrowser.open('reporte.html', new=2, autoraise=True)

lista_nombre= ['Kevin','Carlos','Juan','Pedro','Samuel','Daniel','Lester','Mario','Luis','Fernando']
lista_edades=['19','20','30','25','23','20','18','29','36','31']
lista_activo=['true','False','true','False','true','False','true','False','true','False']
lista_saldo= ['0.0','200.25','1000.43','500.0','250.45','100.0','784.0','654.32','900.87','543.45']

reportar(lista_nombre, lista_edades, lista_activo, lista_saldo)
