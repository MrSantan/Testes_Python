with open("lista.txt") as lista:
    for i in lista:
        print(f"- {i.strip()}")

print("----------------------------")

with open("lista.txt", "a") as lista:
    novo_item = input("Digite um novo item para adicionar à lista: ")
    if novo_item != "": # Check if the input is not just whitespace
        lista.write(f"{novo_item}\n")
    else:
        print("Nenhum item foi adicionado, pois o input estava vazio.")