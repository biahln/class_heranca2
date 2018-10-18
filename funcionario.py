#Classe funcionario
#Importando a classe Pessoa
from pessoa import pessoa
class Funcionario (pessoa):
    #Metodo construtor
def __init__ (self, nome, cpf, idade, matricula, salario, setor)
    super().__init__(nome, cpf, idade)
    self.matricula=matricula
    self.salario=salario
    self.setor=setor
    