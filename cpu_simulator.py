opcode_dict = {
    "add": 0,
    "subtract": 1,
    "lw": 2,
    "sw": 3
}

class CPU:
    def __init__(self, control_unit) -> None:
        self.control_unit =  control_unit

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
    def __init__(self, ALU) -> None:
        self.ALU = ALU


    def send_instructions(self, opcode:int, operands:list):
        register_1, register_2 = operands[0], operands[1]
        if opcode == 0:
            self.ALU.add(register_1, register_2)


class ALU:
    def __init__(self, register, memory_bus) -> None:
        self.register = register
        self.memory_bus =  memory_bus

    # Function for various operations below.
    def add(self, register_1, register_2):
        print(f"Adding {int(register_1)} and {int(register_2)}")

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

test_cpu = CPU(Control_Unit(ALU(Register(32), Memory_Bus(32))))
test_cpu.control_unit.send_instructions(0, [0, 0])
