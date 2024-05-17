import mysql.connector

class Usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password
    
def iniciar_sesion(mycursor, correo, password):
    sql = "SELECT nombre, correo, password FROM usuarios WHERE correo = %s AND password = %s"
    mycursor.execute(sql, (correo, password))
    usuario_data = mycursor.fetchone()
    if usuario_data:
        usuario = Usuario(*usuario_data)
        print(f"bienvenido, {usuario.nombre}!")
    else:
        print("datos incorrectos.")

def registrar_usuario(mycursor, nombre, correo, password):
    sql = "INSERT INTO usuarios (nombre, correo, password) VALUES (%s, %s, %s)"
    mycursor.execute(sql, (nombre, correo, password))
    print("usuario registrado exitosamente.")

def main():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="mydatabase"
        )
        mycursor = mydb.cursor()

        opcion = input("elige una opcion (1: Registrar, 2: Iniciar sesion): ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            password = input("password: ")
            registrar_usuario(mycursor, nombre, correo, password)
        elif opcion == "2":
            correo = input("Correo: ")
            password = input("password: ")
            iniciar_sesion(mycursor, correo, password)
        else:
            print("opcion no valida.")

        mydb.commit()
        mycursor.close()
        mydb.close()
    except mysql.connector.Error as error:
        print("error al conectar a la base de datos:", error)

if __name__ == "__main__":
    main()













