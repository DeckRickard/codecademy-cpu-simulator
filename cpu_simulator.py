# TO-DO:
# - Implement the remaining opcodes
# - Create logic for dealing with register/memory addresses in instructions



opcode_dict = {
    "add": 0,
    "sub": 1,
    "mult": 2,
    "div": 3
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

        print(opcode_bin, binary_instructions)
        return opcode_bin, binary_instructions
        

class Control_Unit:
    def __init__(self, ALU) -> None:
        self.ALU = ALU


    def send_instructions(self, opcode:int, operands:list):
        print("Sending instructions to the ALU...")
        register_1, register_2, destination_register = operands[0], operands[1], operands[2]
        if opcode == bin(0):
            print("This is an add operation.")
            self.ALU.add(int(register_1, 2), int(register_2, 2), int(destination_register, 2))
        elif opcode == bin(1):
            print("This is a subtraction operation.")
            self.ALU.subtract(int(register_1, 2), int(register_2, 2), int(destination_register, 2))
        elif opcode == bin(2):
            print("This is a multiplication operation.")
            self.ALU.multiply(int(register_1, 2), int(register_2, 2), int(destination_register, 2))
        elif opcode == bin(3):
            print("This is a divison operation.")
            self.ALU.divide(int(register_1, 2), int(register_2, 2), int(destination_register, 2))

        # When operation is complete, display state of register and memory.
        self.ALU.register.print_register()
        self.ALU.memory_bus.print_memory()


class ALU:
    def __init__(self, register, memory_bus) -> None:
        self.register = register
        self.memory_bus =  memory_bus

    # Function for various operations below.
    def add(self, register_1, register_2, destination_register):
        print(f"Adding {register_1} and {register_2}")
        value = register_1 + register_2
        print("Passing {} to destination register {}".format(value, destination_register))
        self.register.insert(destination_register, value)

    def subtract(self, register_1, register_2, destination_register):
        print(f"Subtracting {register_2} from {register_1}")
        value = register_1 - register_2
        print("Passing {} to destination register {}".format(value, destination_register))
        self.register.insert(destination_register, value)

    def multiply(self, register_1, register_2, destination_register):
        print(f"Multiplying {register_2} and {register_1}")
        value = register_1 * register_2
        print("Passing {} to destination register {}".format(value, destination_register))
        self.register.insert(destination_register, value)

    def divide(self, register_1, register_2, destination_register):
        print(f"Dividing {register_1} by {register_2}")
        value = register_1 / register_2
        print("Passing {} to destination register {}".format(value, destination_register))
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
instructions = test_cpu.instruction('div 100 10 7')
# print(instructions)
test_cpu.control_unit.send_instructions(instructions[0], instructions[1])
