

class Estoque:
    def __init__(self):
        self.rolhas = 0
        self.garrafas = 0
        self.rotulos = 0
        self.caixas_6 = 0  
        self.caixas_12 = 0 
        self.total_frete = 0 

    def adicionar_rolha(self, quantidade):
        self.rolhas += quantidade
        print(f"{quantidade} rolhas adicionadas ao estoque.")

    def adicionar_garrafa(self, quantidade):
        self.garrafas += quantidade
        print(f"{quantidade} garrafas adicionadas ao estoque.")

    def adicionar_rotulo(self, quantidade):
        self.rotulos += quantidade
        print(f"{quantidade} rótulos adicionados ao estoque.")

    def adicionar_caixa_6(self, quantidade):
        self.caixas_6 += quantidade
        print(f"{quantidade} caixas de 6 garrafas adicionadas ao estoque.")

    def adicionar_caixa_12(self, quantidade):
        self.caixas_12 += quantidade
        print(f"{quantidade} caixas de 12 garrafas adicionadas ao estoque.")

    def sair_garrafa(self, quantidade):
        if self.garrafas >= quantidade:
            self.garrafas -= quantidade
            frete = quantidade * 10
            self.total_frete += frete
            print(f"{quantidade} garrafas foram retiradas do estoque. Custo de frete: R${frete}")
        else:
            print("Não há garrafas suficientes no estoque.")

    def sair_caixa_6(self, quantidade):
        if self.caixas_6 >= quantidade:
            self.caixas_6 -= quantidade
            frete = quantidade * 60
            self.total_frete += frete
            print(f"{quantidade} caixas de 6 garrafas foram retiradas do estoque. Custo de frete: R${frete}")
        else:
            print("Não há caixas de 6 garrafas suficientes no estoque.")

    def sair_caixa_12(self, quantidade):
        if self.caixas_12 >= quantidade:
            self.caixas_12 -= quantidade
            frete = quantidade * 120
            self.total_frete += frete
            print(f"{quantidade} caixas de 12 garrafas foram retiradas do estoque. Custo de frete: R${frete}")
        else:
            print("Não há caixas de 12 garrafas suficientes no estoque.")

    def mostrar_estoque(self):
        print("Estoque:")
        print(f"Rolhas: {self.rolhas}")
        print(f"Garrafas: {self.garrafas}")
        print(f"Rótulos: {self.rotulos}")
        print(f"Caixas de 6 Garrafas: {self.caixas_6}")
        print(f"Caixas de 12 Garrafas: {self.caixas_12}")

    def mostrar_custo_total_frete(self):
        print(f"Custo total de frete acumulado: R${self.total_frete}")

estoque = Estoque()

while True:
    print("\nOpções:")
    print("1 - Adicionar Rolhas")
    print("2 - Adicionar Garrafas")
    print("3 - Adicionar Rótulos")
    print("4 - Adicionar Caixas de 6 Garrafas")
    print("5 - Adicionar Caixas de 12 Garrafas")
    print("6 - Retirar Garrafas")
    print("7 - Retirar Caixas de 6 Garrafas")
    print("8 - Retirar Caixas de 12 Garrafas")
    print("9 - Mostrar Estoque")
    print("10 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantidade = int(input("Digite a quantidade de rolhas a ser adicionada: "))
        estoque.adicionar_rolha(quantidade)
    elif opcao == 2:
        quantidade = int(input("Digite a quantidade de garrafas a ser adicionada: "))
        estoque.adicionar_garrafa(quantidade)
    elif opcao == 3:
        quantidade = int(input("Digite a quantidade de rótulos a ser adicionada: "))
        estoque.adicionar_rotulo(quantidade)
    elif opcao == 4:
        quantidade = int(input("Digite a quantidade de caixas de 6 garrafas a ser adicionada: "))
        estoque.adicionar_caixa_6(quantidade)
    elif opcao == 5:
        quantidade = int(input("Digite a quantidade de caixas de 12 garrafas a ser adicionada: "))
        estoque.adicionar_caixa_12(quantidade)
    elif opcao == 6:
        quantidade = int(input("Digite a quantidade de garrafas a serem retiradas: "))
        estoque.sair_garrafa(quantidade)
    elif opcao == 7:
        quantidade = int(input("Digite a quantidade de caixas de 6 garrafas a serem retiradas: "))
        estoque.sair_caixa_6(quantidade)
    elif opcao == 8:
        quantidade = int(input("Digite a quantidade de caixas de 12 garrafas a serem retiradas: "))
        estoque.sair_caixa_12(quantidade)
    elif opcao == 9:
        estoque.mostrar_estoque()
    elif opcao == 10:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha novamente.")