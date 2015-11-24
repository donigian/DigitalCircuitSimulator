class CircuitBoard: #TO-DO
    #The purpose of this class is to have a place
    #where we can put all the gates and connectors
    #so we can follow the logic of an entire circuit
    #rather than just the logic of one gate.
    #(Just outputs the "final" gate's output...)
    #(Makes assumption that a circuit only has one
    #exit point?)
    pass


class LogicGate:
    #This is the parent class to all logic gates.
    #Its members are
    #   _label, which can be used to give a gate a name,
    #   _output, which represents the output of the gate
    #            after performing its operation.

    def __init__(self, label):
        self._label = label
        self._output = None

    def getLabel(self):
        return self._label

    def getOutput(self):
        self._output = self.constructGateLogic()
        return self._output


class BinaryGate(LogicGate):
    #This is a LogicGate that takes more than one input.
    #Right now it only takes two inputs, hence the name
    #"BinaryGate".
    #TO-DO: In the future, the gate should be able to take
    #a number of inputs where the number is greater than 1.
    #(AndGate is an example of a LogicGate where it can make
    #sense to have more than 2 inputs.)

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self._pinA = None
        self._pinB = None

    def getPinA(self):
        if self._pinA == None:
            return 1 if int(input("Enter Pin A input for gate "+self.getLabel()+": ")) != 0 else 0
        else:
            return self._pinA.getFrom().getOutput()

    def getPinB(self):
        if self._pinB == None:
            return 1 if int(input("Enter Pin B input for gate "+self.getLabel()+": ")) != 0 else 0
        else:
            return self._pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self._pinA == None:
            self._pinA = source
        else:
            if self._pinB == None:
                self._pinB = source
            else:
                print("Can't Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return self.getPinA() & self.getPinB()
    

class OrGate(BinaryGate):
    
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return self.getPinA() | self.getPinB()
    

#While {AND, OR, NOT} is functionally complete,
#additional logic gates are provided for the sake
#of convenience.
class XorGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return self.getPinA() ^ self.getPinB()
    

class NandGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return 1 ^ (self.getPinA() & self.getPinB())
    

class NorGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return 1 ^ (self.getPinA() | self.getPinB())
    

class XnorGate(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def constructGateLogic(self):
        return 1 ^ (self.getPinA() ^ self.getPinB())
    

class UnaryGate(LogicGate):
    #UnaryGate is a LogicGate that only takes one input.

    def __init__(self, label):
        LogicGate.__init__(self, label)

        self._pin = None

    def getPin(self):
        if self._pin == None:
            return 1 if int(input("Enter Pin input for gate "+self.getLabel()+"-->")) != 0 else 0
        else:
            return self._pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self._pin == None:
            self._pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def constructGateLogic(self):
        return 1 ^ self.getPin()
        

class NopGate(UnaryGate):

    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def constructGateLogic(self):
        return self.getPin()


class Connector:

    def __init__(self, fgate, tgate):
        self._fromgate = fgate
        self._togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self._fromgate

    def getTo(self):
        return self._togate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())

main()
