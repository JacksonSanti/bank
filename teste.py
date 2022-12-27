from models.cliente import Cliente
from models.conta import Conta


jackson: Cliente = Cliente("Jackson", "124.004.446-17", "santi7728@gmail.com", "02/08/1996")

c: Conta = Conta(jackson)

print(c)