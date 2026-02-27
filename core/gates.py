class Gate:
    def __init__(self, name):
        self.name = name
        self.inputs = [False, False]
        self.output = False
    
    def update(self):
        raise NotImplementedError("This method must be implemented by subclasses.")

class AndGate(Gate):
    def update(self):
        self.output = all(self.inputs)
        return self.output

class OrGate(Gate):
    def update(self):
        self.output = any(self.inputs)
        return self.output

class NotGate(Gate):
    def __init__(self, name):
        super().__init__(name)
        self.inputs = [False]
    def update(self):
        self.output = not self.inputs[0]
        return self.output

class XorGate(Gate):
    def update(self):
        self.output = self.inputs[0] != self.inputs[1]
        return self.output

class NandGate(Gate):
    def update(self):
        self.output = not all(self.inputs)
        return self.output