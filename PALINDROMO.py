def is_palindromo(palavra):
    if len(palavra)>1:
        for x in range(0,int(len(palavra)/2)):
            if palavra[x]!=palavra[(len(palavra)-1)-x]:
                return False

    return True
def is_palindromo_recursivo(palavra):
    if len (palavra)<2:
        return True
    elif palavra[0]!= palavra [-1]:
        return False
    else:
        return is_palindromo_recursivo(palavra[1:len(palavra)-1])
print(is_palindromo_recursivo('motor'))
print(is_palindromo_recursivo('rotor'))
print(is_palindromo_recursivo('osso'))
print(is_palindromo_recursivo('ospo'))
print(is_palindromo_recursivo('r'))
