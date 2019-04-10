print("[1]HUMBURGUES..........R$ 3,00\n[2]CHEESEBURGUER.............[R$2,50\n[3]Fritas...........R$2,50\n[4]Refrigerante.............R$1,00\nMILKSHAKE..........R$3,00")
try:
    iten=int(input("Digite o que deseja"))
    quantidade=int(input("Quantidade de itens q vc quer"))
except:
    print("Valor invalido")

if iten == 1:
    soma = quantidade * 3, 00
elif iten == 2:
    soma = quantidade * 2, 50
elif iten == 3:
    soma = quantidade * 2, 50
elif iten == 4:
    soma = quantidade * 1, 00
elif iten == 5:
    soma = quantidade * 3, 00

print("O VALOR A PAGAR :",soma)
