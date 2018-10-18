#Arquivo principal

from pessoa import pessoa

#Objeto da classe pessoa
p1 = pessoa ('João', '123', 20)

#Imprimir dados do objeto
print (p1.get_nome())
print (p1.get_cpf())
print (p1.get_idade())

#Objeto em versão texto
print(p1)

#Objeto funcionario
f1 = Funcionario ('José', '456', 40,)