# Declaracion Boolean
boolean_1 = True
boolean_2 = False

# Ver
print("Contenido boolean #1: ", boolean_1)
print("Contenido boolean #2: ", boolean_2)

# Ver tipo
print("Tipo: ", type(boolean_1))

# Ver stributos y funciones
print("Composicion boolean #1: ", dir(boolean_1))

# Operadores
# Igual
print("\nTrue = False:  ", boolean_1 == boolean_2)
print("True = True:   ", boolean_1 == boolean_1)
print("False = False: ", boolean_2 == boolean_2)
print("False = True:  ", boolean_2 == boolean_1)
# Diferente
print("\nTrue != False:  ", boolean_1 != boolean_2)
print("True != True:   ", boolean_1 != boolean_1)
print("False != False: ", boolean_2 != boolean_2)
print("False != True:  ", boolean_2 != boolean_1)
# Y (AND)
print("\nTrue & False:  ", boolean_1 & boolean_2)
print("True & True:   ", boolean_1 & boolean_1)
print("False & False: ", boolean_2 & boolean_2)
print("False & True:  ", boolean_2 & boolean_1)
# O (OR)
print("\nTrue | False:  ", boolean_1 | boolean_2)
print("True | True:   ", boolean_1 | boolean_1)
print("False | False: ", boolean_2 | boolean_2)
print("False | True:  ", boolean_2 | boolean_1)
# XOR
print("\nTrue ^ False:  ", boolean_1 ^ boolean_2)
print("True ^ True:   ", boolean_1 ^ boolean_1)
print("False ^ False: ", boolean_2 ^ boolean_2)
print("False ^ True:  ", boolean_2 ^ boolean_1)
# <<
print("\nTrue << False:  ", boolean_1 << boolean_2)
print("True << True:   ", boolean_1 << boolean_1)
print("False << False: ", boolean_2 << boolean_2)
print("False << True:  ", boolean_2 << boolean_1)
# >>
print("\nTrue >> False:  ", boolean_1 >> boolean_2)
print("True >> True:   ", boolean_1 >> boolean_1)
print("False >> False: ", boolean_2 >> boolean_2)
print("False >> True:  ", boolean_2 >> boolean_1)
