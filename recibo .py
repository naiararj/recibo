#Crie um sistema que imprima um recibo de compras para o usuário. O sistema vai perguntar a quantidade de itens diferentes e depois vai perguntar qual o nome do item e a quantidade deste item. No final o programa exibe o recibo juntamente com o valor final da compra. Veja um exemplo de como o sistema deve funcionar: 


itensQuantidade = int(input("Digite a quantidade de itens diferentes: "))

itens=[]

i=0
while i<itensQuantidade:
    nomeItem=input("Nome do produto {}: ".format(i+1) )
    quantidade=float(input("Quantidade do produto: "))
    valorUnitario=float(input("Valor unitário do produto: "))
    
    item={
    "nomeItem":nomeItem,
    "quantidade":quantidade,
    "valorUnitario":valorUnitario
    }
    
    itens.append(item)
    i+=1

total=0
print("==========================")
print("Recibo")
print("Quantidade   |   Nome  | Valor")
for item in itens:
    print("{}  |   {}   |  R${}".format(item["quantidade"],item["nomeItem"],item["valorUnitario"]))
    total+=item["valorUnitario"] * item["quantidade"]
print("Total: R$"+str(total))
print("======================")
