from .components import Attribute, FunctionalDependency, MultivaluedDependency, Relvar
from .exceptions import InvalidDependency, InvalidExpression
from .algorithms import closure, is_superkey, is_key, is_relvar_in_bcnf, is_relvar_in_4nf


A = Attribute("A")
B = Attribute("B")
C = Attribute("C")
D = Attribute("D")
E = Attribute("E")

# PRUEBAS DE LAS FUNCIONES

print("=== PRUEBA IS_TRIVIAL (MULTIVALUADA) ===")
heading_set = {A, B, C}
mvd_trivial = MultivaluedDependency("{A,B}->->{A}")
mvd_non_trivial = MultivaluedDependency("{A}->->{C}")
print("¿{A,B}->->{A} es trivial?:", mvd_trivial.is_trivial(heading_set))  # Respuesta esperada: True
print("¿{A}->->{C} es trivial?:", mvd_non_trivial.is_trivial(heading_set))  # Respuesta esperada: False


print("=== PRUEBA IS_TRIVIAL (DF) ===")
fd_trivial = FunctionalDependency("{A}->{A}")
fd_non_trivial = FunctionalDependency("{A}->{B}")
print("¿{A}->{A} es trivial?:", fd_trivial.is_trivial())  # Respuesta esperada: True
print("¿{A}->{B} es trivial?:", fd_non_trivial.is_trivial())  # Respuesta esperada: False


print("=== PRUEBA CLOSURE ===")
fds = {
    FunctionalDependency("{A}->{B}"),
    FunctionalDependency("{B}->{C}"),
    FunctionalDependency("{C,D}->{E}")
}
print("Cierre de {A, D}:", {attr.name for attr in closure({A, D}, fds)})  # Respuesta esperada: {C,E,B,D,A}


print("=== PRUEBA IS_SUPERKEY ===")
fds = {
    FunctionalDependency("{A}->{B}"),
    FunctionalDependency("{B}->{C}"),
    FunctionalDependency("{C}->{D}")
}
heading = {A, B, C, D}
print("¿{A} es superllave?:", is_superkey({A}, heading, fds))  # Respuesta esperada: True


print("=== PRUEBA IS_KEY ===")
fds = {
    FunctionalDependency("{A}->{B}"),
    FunctionalDependency("{B}->{C}")
}
heading = {A, B, C}
print("¿{A} es llave?:", is_key({A}, heading, fds))  # Respuesta esperada: True


print("=== PRUEBA BCNF ===")
fds = {
    FunctionalDependency("{A}->{B}"),
    FunctionalDependency("{B}->{A}")
}
relvar = Relvar(["A", "B"], functional_dependencies=fds)
print("¿Relvar está en BCNF?:", is_relvar_in_bcnf(relvar))  # Respuesta esperada: True



print("=== PRUEBA 4NF ===")
fd = FunctionalDependency("{A}->{B}")
mvd = MultivaluedDependency("{A}->->{C}")
relvar = Relvar(["A", "B", "C"], functional_dependencies={fd}, multivalued_dependencies={mvd})
print("¿Relvar está en 4NF?:", is_relvar_in_4nf(relvar))  # Respuesta esperada: False

