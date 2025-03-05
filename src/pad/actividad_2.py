import numpy as np
import pandas as pd
from numpy.random import randn

class Matrices():
    def __init__(self):
        np.random.seed(101)
    
    def serie(self): # una sola dimencion
        etiquetas= ["a","b","c"]
        valores = [10,20,30]
        arr = np.array(valores)
        directorios={"amiiboSeries": "Mario Sports Superstars", "character": "Metal Mario","numero":121}
        #print(pd.__version__)
        mi_serie= pd.Series(data=valores,index=etiquetas)
        print(etiquetas)
        print(valores)
        print(arr)
        print(directorios)
    
    def matrices(self,filas=0,columnas=0):
        #data= pd.DataFrame() # vacio
        #data= pd.DataFrame(randn(6,4),index="A B C D E F".split(" "), columns="W X Y Z".split(" "))
        data= pd.DataFrame(randn(6,4), columns="W X Y Z".split(" ")) # ((w*y)-z)+y  
        print(data)
        data["udigital"]= "pad"
        data["funcion"]= ((data["W"]*data["Y"])-data["Z"])+data["Y"]
        data.to_excel("datos_generados.xlsx")

matr =  Matrices()
matr.matrices()
#matr.serie()