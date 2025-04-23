from .components import FunctionalDependency, Attribute, Relvar


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
            if fd.left.issubset(closure_set) and not fd.right.issubset(closure_set):
                # Agregamos los atributos del lado derecho al cierre y seguimos iterando
                closure_set.update(fd.right)
                changed=True
    return closure_set


def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # TODO: Actividad 4
    raise closure(attributes, functional_dependencies).issuperset(heading)


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    # Verificar si el conjunto de atributos es un superclave
    if not is_superkey(attributes, heading, functional_dependencies):
        return False
    
    # Verificar si cualquier subconjunto propio es también superclave
    for attr in attributes:
        subset = attributes - {attr}
        if is_superkey(subset, heading, functional_dependencies):
            return False
    
    return True


def is_relvar_in_bcnf(relvar: Relvar) -> bool:
      for fd in relvar.fds:
        if not is_superkey(fd.lhs, relvar.header, relvar.fds):
            return False
       return True



def is_relvar_in_4nf(relvar: Relvar) -> bool:
      for mvd in relvar.mvds:
        if not is_superkey(mvd.lhs, relvar.header, relvar.fds):
            return False
       return True

