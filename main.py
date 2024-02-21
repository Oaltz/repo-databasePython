# Imporatação e conexão com o database / tables

from database import db, Usuario, Anuncio

db.connect()

db.create_tables((Usuario, Anuncio))

# Create
usuario = Usuario.create(nome="Henrique", email="henrique@gmail.com", senha="123")

Usuario.create(nome="Pedro", email="pedro@gmail.com", senha="123!")
Usuario.create(nome="Davi", email="davi@gmail.com", senha="123@")
Usuario.create(nome="Maria", email="maria@gmail.com", senha="123#")

# print ("Novo usuário: ", usuario.id, usuario.nome, usuario.email)

# Read
lista_usuarios = Usuario.select()
# print("Listando usuários:")

for u in lista_usuarios:
    # print("-", u.id, u.nome, u.email)

usuario1 = Usuario.get(Usuario.id ==1)
# print("Usuário pelo id:", usuario1.id, usuario1.nome)

# Update
maria = Usuario.get(Usuario.email == "maria@gmail.com")
maria.nome = "Maria Joaquina"
maria.save()

# print("Nome atualizado da Maria:", maria.nome)

try:
    usuario_duplicado = Usuario.create(nome= "Duplicado", email="teste@teste.com", senha="123")
except:
    # print("E-mail existente!")

# Delete
usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
usuario_deletado.delete_instance()

try:
    Usuario.get(Usuario.email == "teste@teste.com")
except:
    # print("Usuário deletado!")

# Tabel Anuncio
maria = Usuario.get(Usuario.email == "maria@gmail.com")
anuncio = Anuncio.create(
    usuario = maria,
    titulo = "Teste do banco de Dados",
    descricao = "Teste para criação de um anuncio vinculado a um usuário",
    valor = 500.0
)

# print("Novo anuncio: ", anuncio.id, anuncio.titulo)

# Create
Anuncio.create(usuario = maria, titulo= "Anuncio 1", descricao= "Descrição 1", valor= 100.0)
Anuncio.create(usuario = maria, titulo= "Anuncio 2", descricao= "Descrição 2", valor= 150.0)
Anuncio.create(usuario = maria, titulo= "Anuncio 3", descricao= "Descrição 3", valor= 200.0)

# Read
# print("Anuncios da maria: ")

anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@gmail.com")
for a in anuncios_maria:
    # print("-", a.id, a.titulo, a.valor)

# Update
maria_anuncio = Anuncio.get(Anuncio.titulo == "Anuncio 1")
maria_anuncio.titulo = "Anuncio 1 Atualizado"
maria_anuncio.save()
# print("Anuncio atualizado da Maria:", maria_anuncio.titulo)

# Delete
Anuncio.delete().execute()

# print("Qtd de anuncios: ", Anuncio.select().count())