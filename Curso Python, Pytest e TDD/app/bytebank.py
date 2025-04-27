from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._name = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._name

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nasciemnto_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nasciemnto_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._name.strip()
        nome_quebrado = nome_completo.split(" ")
        return nome_quebrado[-1]

    def _eh_socio(self):
        sobre_names = ['Bragança', 'Cordeiro', 'Silva']
        return self._salario >= 100000 and (self.sobrenome() in sobre_names)

    def decrescimo_salario(self):
        if self._eh_socio:
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Salario é muito alto para receber um bonus")
        return valor

    def __str__(self):
        return f'Funcionario({self._name}, {self._data_nascimento}, {self._salario})'
