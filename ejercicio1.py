#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
# lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.


f = open('datos.txt','w')

datos = "datos de prueba\n"
f.write(datos)
f.close()

f = open('datos.txt', 'a')
datos = 'mas datos\n'
f.writelines(datos)
f.close()
