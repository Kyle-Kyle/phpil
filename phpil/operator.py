from enum import Enum

from .opcode import Opcode

attr_list = ["isPrimitive", "isLiteral", "isParametric", "isCall", "isBlockBegin", "isBlockEnd", "isLoopBegin", "isLoopEnd", "isInternal", "isJump", "isImmutable", "isVarargs"]
Attribute = Enum("Attribute", attr_list)

class Operator:
    opcode = None
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = []

    def __str__(self):
        #TODO: refactor this
        outstring = ""
        output = ""
        input = ""

        for i in range(self.num_output):
            output += "out" + str(i) + ", "

        if self.num_output > 0:
            output = ''.join(output.rsplit(',', 1)) + "= "

        for i in range(self.num_input):
            input += "inp" + str(i) + ", "

        if self.num_input > 0:
            input = ''.join(input.rsplit(',', 1)) + ""

        return output + self.opcode.name + " " + input

class Nop(Operator):
    opcode = Opcode.Nop
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isPrimitive]

class LoadInteger(Operator):
    opcode = Opcode.LoadInteger
    num_input = 0
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"out0 = {self.opcode.name} '{self.value}'"

class LoadFloat(Operator):
    opcode = Opcode.LoadFloat
    num_input = 0
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"out0 = {self.opcode.name} '{self.value}'"

class LoadString(Operator):
    opcode = Opcode.LoadString
    num_input = 0
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"out0 = {self.opcode.name} '{self.value}'"

class LoadBoolean(Operator):
    opcode = Opcode.LoadBoolean
    num_input = 0
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"out0 = {self.opcode.name} '{self.value}'"

class LoadNull(Operator):
    #FIXME: handle null separately maybe?
    opcode = Opcode.LoadNull
    num_input = 0
    num_output = 1
    num_temp_var = 0
    attributes = []

# class LoadObject (Operator):
    #TODO
#     def __init__(self, value):
#(LoadObject , self)         super.__init__(numInputs=0, numOutputs=1, numTempvars=0)
#         self.opcode = Opcode.LoadObject
#         self.value = value

class CreateObject(Operator):
    opcode = Opcode.CreateObject
    num_input = 1
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, obj, args):
        self.object = obj
        self.args = args

class CreateArray(Operator):
    opcode = Opcode.CreateArray
    num_input = None
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, num_init_vals):
        self.num_input = num_init_vals

class CallFunction(Operator):
    opcode = Opcode.CallFunction
    num_input = None
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, num_args):
        self.num_input = num_args+1 # function + func args

class BeginIf(Operator):
    opcode = Opcode.BeginIf
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin]

class BeginElse(Operator):
    opcode = Opcode.BeginElse
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin, Attribute.isBlockEnd]

class EndIf(Operator):
    opcode = Opcode.BeginIf
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd]

class BeginWhile(Operator):
    opcode = Opcode.BeginWhile
    num_input = 2
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin, Attribute.isLoopBegin]

    def __init__(self, comparater):
        self.comparater = comparater

    def __str__(self):
        return f"{self.opcode.name} inp0, {self.comparater}, inp1"

class EndWhile(Operator):
    opcode = Opcode.EndWhile
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd, Attribute.isLoopEnd]

class BeginFor(Operator):
    opcode = Opcode.BeginFor
    num_input = 3
    num_output = 0
    num_temp_var = 1
    attributes = [Attribute.isBlockBegin, Attribute.isLoopBegin]

    def __init__(self, comparater, op):
        self.op = op
        self.comparater = comparater

    def __str__(self):
        return f"{self.opcode.name} inp0, {self.op}, inp1, {self.comparater}, inp2"

class EndFor(Operator):
    opcode = Opcode.EndFor
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd, Attribute.isLoopEnd]

class BeginDoWhile(Operator):
    opcode = Opcode.BeginDoWhile
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin, Attribute.isLoopBegin]

class EndDoWhile(Operator):
    opcode = Opcode.EndDoWhile
    num_input = 2
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd, Attribute.isLoopEnd]

    def __init__(self, comparater):
        self.comparater = comparater

class EndForEach(Operator):
    opcode = Opcode.EndForEach
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = []

class Return(Operator):
    opcode = Opcode.Return
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = []

class Break(Operator):
    opcode = Opcode.Break
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = []

class Continue(Operator):
    opcode = Opcode.Continue
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = []

class UnaryOperator(Operator):
    opcode = Opcode.UnaryOperator
    num_input = 1
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, op):
        self.op = op

    def __str__(self):
        return f"out0 = {self.opcode.name} {self.op} inp0"

class BinaryOperator(Operator):
    opcode = Opcode.BinaryOperator
    num_input = 2
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, op):
        self.op = op

    def __str__(self):
        return f"out0 = {self.opcode.name} inp0, {self.op}, inp1"

class Include(Operator):
    opcode = Opcode.Include
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = []

class Eval(Operator):
    opcode = Opcode.Eval
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = []

    def __init__(self, value):
        self.value = value

class Phi(Operator):
    opcode = Opcode.Phi
    num_input = 1
    num_output = 1
    num_temp_var = 0
    attributes = []

class Copy(Operator):
    opcode = Opcode.Copy
    num_input = 2
    num_output = 0
    num_temp_var = 0
    attributes = []

class BeginFunction(Operator):
    opcode = Opcode.BeginFunction
    num_input = 0
    num_output = 1
    num_temp_var = None
    attributes = [Attribute.isBlockBegin]

    def __init__(self, signature):
        self.signature = signature
        self.num_temp_var = signature.num_args

class EndFunction(Operator):
    opcode = Opcode.EndFunction
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd]

class ThrowException(Operator):
    opcode = Opcode.ThrowException
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = []

class BeginTry(Operator):
    opcode = Opcode.BeginTry
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin]

class BeginCatch(Operator):
    opcode = Opcode.BeginCatch
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockBegin, Attribute.isBlockEnd]

class EndTryCatch(Operator):
    opcode = Opcode.EndTryCatch
    num_input = 0
    num_output = 0
    num_temp_var = 0
    attributes = [Attribute.isBlockEnd]

class CreateDict(Operator):
    opcode = Opcode.CreateDict
    num_input = None
    num_output = 1
    num_temp_var = 0
    attributes = []

    def __init__(self, num_init_vals):
        self.num_input = num_init_vals

class GetArrayElem(Operator):
    opcode = Opcode.GetArrayElem
    num_input = 2
    num_output = 1
    num_temp_var = 0
    attributes = []

class SetArrayElem(Operator):
    opcode = Opcode.SetArrayElem
    num_input = 3
    num_output = 0
    num_temp_var = 0
    attributes = []

#TODO: support class definition
class BeginClass(Operator):
    pass

class EndClass(Operator):
    pass

class BeginForEach(Operator):
    pass

class Print(Operator):
    opcode = Opcode.Print
    num_input = 1
    num_output = 0
    num_temp_var = 0
    attributes = []

################################ operator grouping ###########################
comparaters = ["==", "===", "!=", "<", "<=", ">", ">="]
unary_ops = ["++", "--", "!", "~"]
binary_ops = ["+", "-", "*", "/", "%", "&", "|", "&&", "||", "^", "<<", ">>"]

