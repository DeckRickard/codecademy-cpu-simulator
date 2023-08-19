class CPU:
    def __init__(self, control_unit, ALU, register, memory_bus) -> None:
        self.control_unit =  control_unit
        self.ALU = ALU
        self.register = register
        self.memory_bus =  memory_bus

    def instruction(instruction):
        pass

class Control_Unit:
    def __init__(self) -> None:
        pass

    def split_values(instruction):
        pass

    def send_instructions(opcode, operands):
        pass


class ALU:
    def __init__(self) -> None:
        pass

    # Function for various operations below.

class Register:
    def __init__(self, register_size) -> None:
        self.register = [0 for i in range(0, register_size)]

    def insert(address, value):
        pass

    def retrieve(address):
        pass

class Memory_Bus:
    def __init__(self, size) -> None:
        self.memory = [0 for i in range(0, size)]
    
    def insert(address, value):
        pass

    def retrieve(address):
        pass