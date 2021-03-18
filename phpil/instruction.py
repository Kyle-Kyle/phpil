from .opcode import Opcode
from .operator import Attribute

class Instruction:

    def __init__(self, operator, inputs=None, outputs=None, temps=None):
        self.operator = operator
        self.inputs = inputs if inputs else []
        self.outputs = outputs if outputs else []
        self.temps = temps if temps else []

    def __str__(self):

        string = str(self.operator)

        inps = ""
        for i, val in enumerate(self.inputs):
            string = string.replace("inp"+str(i), str(val))

        for i, val in enumerate(self.outputs):
            string = string.replace("out"+str(i), str(val))

        return string


    """getter for the ith input/output variable"""
    def getOutput(self, idx=0):
        return self.outputs[idx]

    def getInput(self, idx=0):
        return self.inputs[idx]

    def getTemp(self, idx=0):
        return self.temps[idx]


    """getter for all output variable"""
    def getAllOutputs(self):
        return self.outputs

    def getAllInputs(self):
        return self.inputs

    def getAllTemps(self):
        return self.temps


    """misc functions"""
    def isBeginFunction(self):
        return self.operator.opcode == Opcode.BeginFunction

    def isEndFunction(self):
        return self.operator.opcode == Opcode.EndFunction

    def isBeginElse(self):
        return self.operator.opcode == Opcode.BeginElse

    def hasOutputs(self):
        return self.operator.num_output != 0

    def hasInputs(self):
        return self.operator.num_input != 0

    def getOpcode(self):
        return self.operator.opcode


    """Flag manipulations"""
    def isBlockBegin(self):
        return Attribute.isBlockBegin in self.operator.attributes

    def isBlockEnd(self):
        return Attribute.isBlockEnd in self.operator.attributes

    def isLoopBegin(self):
        return Attribute.isLoopBegin in self.operator.attributes

    def isLoopEnd(self):
        return Attribute.isLoopEnd in self.operator.attributes

