
pwd = input("Digite uma senha: ")

if len(pwd) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
elif not any(char.isdigit() for char in pwd):
    print("A senha deve conter pelo menos um dígito.")
elif not any(char.isupper() for char in pwd):
    print("A senha deve conter pelo menos uma letra maiúscula.")
elif not any(char.islower() for char in pwd):
    print("A senha deve conter pelo menos uma letra minúscula.")
elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in pwd):
    print("A senha deve conter pelo menos um caractere especial.")
else:
    print("Senha válida!")
    with open("senha.txt", "w") as file:
        file.write(pwd)
    print("Senha salva com sucesso!")