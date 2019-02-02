# Class Utility
# Gabriel R Santos (@chr0m1ng)


class ClassUtils():
    ''' Do a safe cast of a obj to a given type.'''
    def SafeCast(val, to_type, default=None):
        try:
            return to_type(val)
        except (ValueError, TypeError):
            return default
