from app.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = "13/03/2000"
        esperado = 25

        funcionario_teste = Funcionario("teste", entrada, 1111)

        # When - Ação
        resultado = funcionario_teste.idade()

        # Then - Resultado
        assert resultado == esperado

    def test_quando_name_recebe_lucas_carvalho_deve_retornar_apenas_carvalho(self):
        # Given
        entrada = " Lucas Carvalho "
        esperado = "Carvalho"
        sobre_name_teste = Funcionario(entrada, "11/11/2000", 1111)

        # When
        resultado = sobre_name_teste.sobrenome()

        # Then
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # given
        entrada_salario = 100000
        esperado = 90000
        entrada_name = "Paulo Bragança"
        funcionario_teste = Funcionario(entrada_name, "11/11/2000", entrada_salario)

        # When
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # given
        entrada = 1000
        esperado = 100
        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)

        # When
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert resultado == esperado
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        # given
        entrada = 10000000
        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)

        # When / Then
        with pytest.raises(Exception):
            funcionario_teste.calcular_bonus()

    def test_quando_idade_for_13_03_1999_deve_retornar_24(self):
        # Given - Contexto
        entrada = "13/03/1999" 
        esperado = 24

        funcionario_teste = Funcionario("teste", entrada, 1111)

        # When - Ação
        resultado = funcionario_teste.idade()

        # Then - Resultado
        assert resultado == esperado

    def test_retorno_str(self):
        # Given
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'
        funcionario_teste = Funcionario(nome, data_nascimento, salario)

        # When
        resultado = funcionario_teste.__str__()

        # Then
        assert resultado == esperado
