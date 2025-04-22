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
    # TODO: Actividad 5
    raise NotImplementedError()


def is_relvar_in_bcnf(relvar: Relvar):
    # TODO: Actividad 6
    raise NotImplementedError()


def is_relvar_in_4nf(relvar: Relvar):
    # TODO: Actividad 7
    raise NotImplementedError()
