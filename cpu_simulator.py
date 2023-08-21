opcode_dict = {
    "add": 0,
    "subtract": 1,
    "lw": 2,
    "sw": 3
}

class CPU:
    def __init__(self, control_unit, ALU, register, memory_bus) -> None:
        self.control_unit =  control_unit
        self.ALU = ALU
        self.register = register
        self.memory_bus =  memory_bus

# Interprets assembly language instruction (opcode, register_1, register_2, destination_register) and converts it to binary.
    def instruction(self, instruction:str):
        
        instruction_array = instruction.split(' ')
        
        # We'll deal properly with the opcode later.
        opcode = instruction_array.pop(0)
        binary_instructions = []
        for item in instruction_array:
            item_int = int(item)
            binary_instructions.append(bin(item_int))

        # Handles conversion of opcode
        opcode_bin = bin(opcode_dict[opcode])

        return opcode_bin, binary_instructions
        

class Control_Unit:
    def __init__(self) -> None:
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
        self.memory = [0 for _ in range(0, size)]
    
    def insert(address, value):
        pass

    def retrieve(address):
        pass

test = CPU(None, None, None, None)
test_1 = "add 1 4 8"
test.instruction(test_1)
