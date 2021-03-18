"""
declare all the opcodes
"""
from enum import Enum

opcode_list = [ "Nop", "LoadInteger", "LoadFloat", "LoadString", "LoadBoolean", "LoadNull", "CreateObject", "CreateArray", "CallFunction", "Print", "BeginFunction", "EndFunction", "BeginIf", "BeginElse", "EndIf", "BeginWhile", "EndWhile", "BeginFor", "EndFor", "BeginForEach", "EndForEach", "Return", "Break", "Continue", "BeginTry", "BeginCatch", "EndTryCatch", "BeginClass", "EndClass", "UnaryOperator", "BinaryOperator", "Include", "Eval", "Phi", "Copy", "BeginDoWhile", "EndDoWhile", "ThrowException","CreateDict","GetArrayElem","SetArrayElem"]

Opcode = Enum("Opcode", opcode_list)

if __name__ == '__main__':
    print(Opcode.Nop.name)
    print(Opcode.Nop.value)
