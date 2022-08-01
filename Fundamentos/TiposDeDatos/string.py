# Declaracion de strings
string_1 = "Hello World! 1"
string_2 = 'Hello World! 2'
string_3 = """Hello World! é"""
string_4 = '''Hello World! å'''
print("Contenido strin #1: ", string_1)
print("Contenido strin #2: ", string_2)
print("Contenido strin #3: ", string_3)
print("Contenido strin #4: ", string_4)

# Concatenar
string_concatenado = string_1 + " " + string_2 + " " + string_3 + " " + string_4

print("Contenido string concatenado: ", string_concatenado)

# Ver tipo
print("Tipo string #1: ", type(string_1))
print("Tipo string #2: ", type(string_2))
print("Tipo string #3: ", type(string_3))
print("Tipo string #4: ", type(string_4))
print("Tipo string concatenado", type(string_concatenado))

# Ver stributos y funciones
print("Composicion string #1: ",dir(string_1))

# Capitalize, primera letra en mayuscula, las demas en minusclas
print("Capitalize: ",string_1.capitalize())

# Casefold, toda la cadena en minusculas
print("Casefold: ",string_2.casefold())

# Center, centra el texto en un espacio indicado de caracteres
print("Center: |",string_3.center(40),"|")

# Count, cuenta el nuveo de veces que un elemento est{a dentro de la cadena
print("Count: ",string_4.count("o"))

# Encode,
print("Encode: ",string_concatenado.encode())
print("Encode: ",string_concatenado.encode(encoding="ascii",errors="backslashreplace"))
print("Encode: ",string_concatenado.encode(encoding="ascii",errors="ignore"))
print("Encode: ",string_concatenado.encode(encoding="ascii",errors="namereplace"))
print("Encode: ",string_concatenado.encode(encoding="ascii",errors="replace"))
print("Encode: ",string_concatenado.encode(encoding="ascii",errors="xmlcharrefreplace"))

# Endswith, verifica si el texto termina en
print("Endswith: ",string_1.endswith("1"))
print("Endswith: ",string_1.endswith("2"))

# Expandtabs, expesifica el tamaño de espacions de \t (tabulacion)
string_1 = 'H\tE\tL\tL\tO' 
print("Expandtabs: ",string_1.expandtabs(1))
print("Expandtabs: ",string_1.expandtabs(2))
print("Expandtabs: ",string_1.expandtabs(3))
print("Expandtabs: ",string_1.expandtabs(4))

# Ejemplo
for i in range(10):
    print("Expandtabs: ",string_1.expandtabs(i))

# Find, indica en que posicion dle texto se encuentra un caracter o caracteres especificos, retorna la posicion dela primera vez que lo encuentra
print("Find: ",string_concatenado.find("1"))
print("Find: ",string_concatenado.find("2"))
print("Find: ",string_concatenado.find("3"))
print("Find: ",string_concatenado.find("Hello"))

