sistema= []

def cadastrar_cliente(usuario, senha):
  for cliente in sistema:
    if cliente["Usuario"] == usuario:
      print("Usuario já cadastrado!")
      return
      
  sistema.append({
        "Usuario": usuario,
        "Senha": senha
      })
  print("Usuario cadastrado com sucesso!")

def login_cliente(usuario_cadastrado, senha_cadastrada):
  for cliente in sistema:
    if cliente["Usuario"] == usuario_cadastrado:
      print("Usuario encontrado!")
      if cliente["Senha"] == senha_cadastrada:
        print("Seja Bem-Vindo!")
      else:
        print("Usuario ou senha incorretos!")
      return 
  print("Usuario não cadastrado!")

while True:
  print("=====Menu=====\n1- Cadastro\n2- Login\n3- Sair")
  try:
    opc= int(input("Escolha uma opção: "))
  except ValueError:
    print("Apenas numeros")
    continue

  match opc:
    case 1: 
      usuario= input("Crie seu nome: ")
      senha= input("Crie sua senha: ")
      cadastrar_cliente(usuario, senha)
    case 2:
      usuario_cadastrado= input("digite o seu Login: ")
      senha_cadastrada= input("Digite a sua Senha: ")
      login_cliente(usuario_cadastrado, senha_cadastrada)
    case 3:
      print("Você saiu do sistema!")
      break
    case _:
      print("Opção inválida!")