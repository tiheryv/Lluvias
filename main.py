import xlrd
from Array3D import Array3D

def main():
    data = []
    lluvias = Array3D(33,13,35)
    for anio in range(1985,2019):
        anio_lista=[]
        archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
        hoja=archivo.sheet_by_index(0)
        for estado in range(2,34):
            mes_lista=[]
            for mes in range(1,13):
                mes_lista.append("%.2f" % hoja.cell_value(estado,mes))
            anio_lista.append(mes_lista)
        data.append(anio_lista)
    for depth in range(34):
        for rows in range(32):
            for cols in range(12):
                lluvias.set_item(rows,cols,depth,data[depth][rows][cols])
    anio=int(input("año(1985-2018)?:"))
    estado=int(input('Que estado(1-32)?:'))
    mes=int(input("mes(1-12)?:"))

    print(f"el promedio mensual es:{lluvias.get_item(estado-1,mes-1,anio-1985)}")

main()
