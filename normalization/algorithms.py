from .components import FunctionalDependency, Attribute, Relvar, MultivaluedDependency


def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    # TODO: Actividad 3
    """
    debemos regresar el cierre del conjunto de atributos i.e. conjunto de todos los atributos que pueden ser determinados funcionalmente
    """
    closure_set=set(attributes)  #hacemos copia del conjunto inicial
    changed=True #variable para saber si el cierre cambió 

    while changed: 
        changed=False
        for fd in functional_dependencies: #iteramos sobre las dependencias funcionales
            #si el lado izquierdo está contenido en el cierre actual y hay atributos en el lado derecho que no están en el cierre
            if fd.determinant.issubset(closure_set) and not fd.dependant.issubset(closure_set):
                # Agregamos los atributos del lado derecho al cierre y seguimos iterando
                closure_set.update(fd.dependant)
                changed=True
    return closure_set


def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 4
    return closure(attributes, functional_dependencies).issuperset(heading)


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # Verificar si el conjunto de atributos es un superllave
    if not is_superkey(attributes, heading, functional_dependencies):
        return False
    # Verificar si cualquier subconjunto propio es también superllave
    for attr in attributes:
        subset = attributes - {attr}
        if is_superkey(subset, heading, functional_dependencies):
            return False
    return True


def is_relvar_in_bcnf(relvar: Relvar) -> bool:
    for fd in relvar.functional_dependencies:
         if not fd.is_trivial() and not is_superkey(fd.determinant, relvar.heading, relvar.functional_dependencies): 
            return False
    return True 


def is_relvar_in_4nf(relvar: Relvar) -> bool: 
    #verificar que este en BCNF 
    if not is_relvar_in_bcnf(relvar):
        return False
    # verificar MVDs 
    for mvd in relvar.multivalued_dependencies:
        if not mvd.is_trivial(relvar.heading) and not is_superkey(mvd.determinant, relvar.heading, relvar.functional_dependencies):
            return False
    return True


# Ejemplo 1: BCNF y 4NF
heading = {"A", "B"}
fd = FunctionalDependency("{A}->{B}")  # A es superllave
mvd = MultivaluedDependency("{A}->->{B}")  # Trivial (B ⊆ A)
relvar = Relvar(heading, [fd], [mvd])
print(is_relvar_in_bcnf(relvar))  # True
print(is_relvar_in_4nf(relvar))   # True

# Ejemplo 2: No está en BCNF
heading = {"A", "B"}
fd = FunctionalDependency("{B}->{A}")  # B no es superllave
relvar = Relvar(heading, [fd], [])
print(is_relvar_in_bcnf(relvar))  # False