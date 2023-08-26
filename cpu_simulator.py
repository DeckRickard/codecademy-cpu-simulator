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
        
        print("Converting instruction from machine language to binary...")
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
        print("Sending instructions to the ALU...")
        register_1, register_2, destination_register = operands[0], operands[1], operands[2]
        if opcode == 0:
            print("This is an add operation.")
            self.ALU.add(register_1, register_2, destination_register)

        # When operation is complete, display state of register and memory.
        self.ALU.register.print_register()
        self.ALU.memory_bus.print_memory()


class ALU:
    def __init__(self, register, memory_bus) -> None:
        self.register = register
        self.memory_bus =  memory_bus

    # Function for various operations below.
    def add(self, register_1, register_2, destination_register):
        print(f"Adding {int(register_1)} and {int(register_2)}")
        value = register_1 + register_2
        print("Passing value to destination register...")
        self.register.insert(destination_register, value)


class Register:
    def __init__(self, register_size) -> None:
        self.register = [0 for i in range(0, register_size)]

    def insert(self, address, value):
        print("Saving value to register at address: {}.".format(address))
        self.register[address] = value

    def retrieve(self, address):
        print("Retrieving value from register at address: {}".format(address))
        return self.register[address]
    
    def print_register(self):
        print("State of register: \n")
        print(self.register)

class Memory_Bus:
    def __init__(self, size) -> None:
        self.memory = [0 for _ in range(0, size)]
    
    def insert(self, address, value):
        print("Saving value to memory at address: {}.".format(address))
        self.memory[address] = value

    def retrieve(self, address):
        print("Retrieving value from memory at address: {}".format(address))
        return self.memory[address]
    
    def print_memory(self):
        print("State of Memory: \n")
        print(self.memory)

test_cpu = CPU(Control_Unit(ALU(Register(32), Memory_Bus(32))))
test_cpu.control_unit.send_instructions(0, [3, 4, 2])
