---

## 3) validador-cpf  
*Descrição sugerida:* Validador de CPF em Python.

*Arquivo:* validador_cpf.py  
```python
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma2 * 10 % 11) % 10

    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])

if _name_ == "_main_":
    cpf_input = input("Digite um CPF para validar (somente números ou com pontos/traço): ")
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido!")
