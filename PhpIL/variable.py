"""
An abstraction for variables in PHPIL
"""
class Variable:

    class_id = 0

    def __init__(self):
        self.id = self.__class__.class_id
        self.__class__.class_id += 1

    def __eq__(self, other):
        if not isinstance(other, Variable):
            return False
        return self.id == other.id

    def __str__(self):
        return "$v" + str(self.id)

    def __repr__(self):
        return "v" + str(self.id)

    @staticmethod
    def new_session():
        Variable.class_id = 0

if __name__ == '__main__':
    print(Variable())
    print(Variable())
    Variable.new_session()
    print(Variable())
    print(Variable())
