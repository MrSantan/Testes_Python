from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual

# programa
# conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)
#
# cartao_Lira = CartaoCredito('Lira', conta_Lira)
#
#
# conta_Lira.nome = "João Lira"
# print(conta_Lira.nome)
#
#
# cartao_Lira.senha = '2345'
# print(cartao_Lira.senha)
#
# print(conta_Lira.__dict__)
# print(cartao_Lira.__dict__)

agencia_premium_especial = AgenciaPremium(22221111, 15888888888888)
print(agencia_premium_especial.caixa)


