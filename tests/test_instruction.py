from phpil.operator import *
from phpil.variable import Variable
from phpil.instruction import Instruction

print(Instruction(Nop()))
print(Instruction(LoadInteger(1),False,[Variable(12)]))
print(Instruction(LoadFloat(1.1),False,[Variable(11)]))
print(Instruction(LoadString('aaaa'),False,[Variable(12)]))
print(Instruction(LoadBoolean(True),False,[Variable(12)]))
print(Instruction(LoadNull(),False,[Variable(12)]))
print(Instruction(CreateArray(3),[Variable(2),Variable(3),Variable(4)],[Variable(12)]))
print(Instruction(CallFunction(2),[Variable(1), Variable(2), Variable(3)], [Variable(4)]))
#print(Instruction(CreateObject('blag', 3),[Variable(1),Variable(3),Variable(2) ],[Variable(12)])) //Error
#print(Instruction(BeginFunction(),False,[Variable(12)])) //NotCompleted
#print(Instruction(EndFunction(),False,False)) //NotCompleted
print(Instruction(BeginIf(),[Variable(1)],False))
print(Instruction(BeginElse(),False,False))
print(Instruction(EndIf(),False,False))
print(Instruction(BeginWhile(">"),[Variable(5), Variable(0)],False)) # Error
print(Instruction(EndWhile(),False,False))
print(Instruction(BeginFor("++", "<"),[Variable(1), Variable(4), Variable(10)],False))
print(Instruction(EndFor(),False,False))
#print(Instruction(BeginForEach(),False,False)) //NotCompleted
#print(Instruction(EndForEach(),False,False)) //NotCompleted
print(Instruction(Return(),False,[Variable(12)]))
print(Instruction(Break(),False,False))
print(Instruction(Continue(),False,False))
#print(Instruction(BeginTry(),False,False)) //NotCompleted
#print(Instruction(BeginCatch(),False,False)) //NotCompleted
#print(Instruction(EndTryCatch(),False,False)) //NotCompleted
#print(Instruction(BeginClass(),False,False)) //NotMade
#print(Instruction(EndClass(),False,False)) //NotMade
print(Instruction(UnaryOperator("++"),[Variable(11)],[Variable(10)]))
print(Instruction(BinaryOperator("+"),[Variable(10), Variable(11)],[Variable(10)]))
print(Instruction(Include(),[Variable("module")],False))
print(Instruction(Eval('1'),[Variable(11)],False))
print(Instruction(Phi(), [Variable(10)], [Variable(12)]))
print(Instruction(Copy(), [Variable(10), Variable(20)], False))
print(Instruction(ThrowException(), [Variable(10)], False))
print(Instruction(BeginTry(), False, False))
print(Instruction(Copy(),False, [Variable(20)]))
print(Instruction(Print(), [Variable(10)], False))
print(Instruction(BeginDoWhile(), False, False))
print(Instruction(EndDoWhile(">"), [Variable(1), Variable(2)], False))
