
''' forma no legal
import sys.os
sys.path.insert(0,os.path.abspath('...')
import paquete.funciones as fun
fun.Luisa()
'''
import paquete.funciones as fun 
print(fun.Luisa())


def test_():
    assert fun.multiplicacion(5,5)==25
    assert fun.sumar(5,4)==9 
    assert print('hola')== None 
