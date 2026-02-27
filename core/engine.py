class Wire:
    def __init__(self, start_gate, end_gate, input_index):
        self.start_gate = start_gate   # The object from which the signal originates (InputSwitch or DraggableGate)
        self.end_gate = end_gate       # The object where the signal is received (DraggableGate)
        self.input_index = input_index # Which input of the target gate?

    def transmit(self):
        # Carry the signal: Inject it from the output to the input
        val = self.start_gate.logic_gate.output
        self.end_gate.logic_gate.inputs[self.input_index] = val