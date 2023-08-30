# TO-DO:
# - Implement a way for instructions to be read from an external file.
# - Implement error and input checking.



class CPU:
    def __init__(self, control_unit) -> None:
        self.control_unit =  control_unit

# Interprets assembly language instruction (opcode, register_1, register_2, destination_register) and converts it to binary.
    def instruction(self, instruction:str):
        opcode_dict = {
            "add": 0,
            "sub": 1,
            "mult": 2,
            "div": 3,
            "sw": 4,
            "lw": 5
        }

        print("Converting instruction from machine language to binary...\n")
        instruction_array = instruction.split(' ')

        # We'll deal properly with the opcode later.
        opcode = instruction_array.pop(0)
        binary_instructions = []
        for item in instruction_array:
            # The below logic handles the removal of brackets, and gives the operand a preceding number to determine if this is a register address, a memory address, or a directly inserted number.
            item_list = [*item]            
            # Brackets are used to determine a cache address.
            if item_list[0] and item_list[-1] in ('(', ')'):
                operand = [1, int(item.strip('()'))]
            # Curly brackets are used to signify a memory address.
            elif item_list[0] and item_list[-1] in ('{', '}'):
                operand = [2, int(item.strip('{}'))]
            else:
                operand = [0, int(item)]

            binary_instructions.append([bin(item) for item in operand])

        # Handles conversion of opcode
        opcode_bin = bin(opcode_dict[opcode])

        print(opcode_bin, binary_instructions, '\n')
        self.control_unit.send_instructions(opcode_bin, binary_instructions)
        # return opcode_bin, binary_instructions
    
    # Function to read a file containing instructions and pass them to the CPU line-by-line.
    def read_instructions_from_file(self, path_to_file):
        with open(path_to_file) as file:
            for line in file.readlines():
                instruction = line.rstrip('\n')
                print("performing operation {}".format(instruction))
                self.instruction(instruction)


        

class Control_Unit:
    def __init__(self, ALU) -> None:
        self.ALU = ALU


    def send_instructions(self, opcode:int, bin_operands:list):
        print("Sending instructions to the ALU...\n")
        
        # Save word / load word operations need to be handled differently
        if int(opcode, 2) in (4, 5):
            if int(opcode, 2) == 4:
                print("This is a save word operation.\n")
                if int(bin_operands[1][0], 2) == 1:
                    self.ALU.sw(int(bin_operands[0][1], 2), int(bin_operands[1][1], 2), False)
                elif int(bin_operands[1][0], 2) == 2: 
                    self.ALU.sw(int(bin_operands[0][1], 2), int(bin_operands[1][1], 2), True)
            elif int(opcode, 2) == 5:
                print("This is a load word operation.\n")
                if int(bin_operands[0][0], 2) == 1:
                    self.ALU.lw(int(bin_operands[0][1], 2), False)
                else: 
                    self.ALU.lw(int(bin_operands[0][1], 2), True)

        # If the operation is mathematical, values may need to be retrieved from cache / memory.
        else:
            print("Fetching any required values from cache / memory")
            register_1, register_2 = self.fetch(bin_operands[0]), self.fetch(bin_operands[1])
            destination_register = [int(num, 2) for num in bin_operands[2]]
            print(register_1, register_2, destination_register)

            if opcode == bin(0):
                print("This is an add operation.\n")
                self.ALU.add(register_1, register_2, destination_register)
            elif opcode == bin(1):
                print("This is a subtraction operation.\n")
                self.ALU.subtract(register_1, register_2, destination_register)
            elif opcode == bin(2):
                print("This is a multiplication operation.\n")
                self.ALU.multiply(register_1, register_2, destination_register)
            elif opcode == bin(3):
                print("This is a divison operation.\n")
                self.ALU.divide(register_1, register_2, destination_register)

        # When operation is complete, display state of register and memory.
        self.ALU.register.print_register()
        self.ALU.memory_bus.print_memory()
    
    # This function is used to retrieve values from the cache / memory.
    def fetch(self, operand):
        # If the operand is a directly inserted value, the function can end.
        if int(operand[0], 2) == 0:
            return int(operand[1], 2)
        elif int(operand[0], 2) == 1:
            return self.ALU.lw(int(operand[1], 2), False)
        elif int(operand[0], 2) == 2:
            return self.ALU.lw(int(operand[1], 2), True)


class ALU:
    def __init__(self, register, memory_bus) -> None:
        self.register = register
        self.memory_bus =  memory_bus

    # Function for various operations below.
    def add(self, register_1, register_2, destination_register):
        print(f"Adding {register_1} and {register_2}")
        value = register_1 + register_2
        if destination_register[0] == 1:
            print("Passing {} to cache register {}".format(value, destination_register[1]))
            self.register.insert(destination_register[1], value)
        elif destination_register[0] == 2:
            print("Passing {} to memory register {}".format(value, destination_register[1]))
            self.memory_bus.insert(destination_register[1], value)
        

    def subtract(self, register_1, register_2, destination_register):
        print(f"Subtracting {register_2} from {register_1}")
        value = register_1 - register_2
        if destination_register[0] == 1:
            print("Passing {} to cache register {}".format(value, destination_register[1]))
            self.register.insert(destination_register[1], value)
        elif destination_register[0] == 2:
            print("Passing {} to memory register {}".format(value, destination_register[1]))
            self.memory_bus.insert(destination_register[1], value)

    def multiply(self, register_1, register_2, destination_register):
        print(f"Multiplying {register_2} and {register_1}")
        value = register_1 * register_2
        if destination_register[0] == 1:
            print("Passing {} to cache register {}".format(value, destination_register[1]))
            self.register.insert(destination_register[1], value)
        elif destination_register[0] == 2:
            print("Passing {} to memory register {}".format(value, destination_register[1]))
            self.memory_bus.insert(destination_register[1], value)

    def divide(self, register_1, register_2, destination_register):
        print(f"Dividing {register_1} by {register_2}")
        value = register_1 / register_2
        if destination_register[0] == 1:
            print("Passing {} to cache register {}".format(value, destination_register[1]))
            self.register.insert(destination_register[1], value)
        elif destination_register[0] == 2:
            print("Passing {} to memory register {}".format(value, destination_register[1]))
            self.memory_bus.insert(destination_register[1], value)

    def sw(self, value, destination_register, to_memory):
        if to_memory:
            self.memory_bus.insert(destination_register, value)
        else:
            self.register.insert(destination_register, value)

    def lw(self, target_register, from_memory):
        if from_memory:
            value = self.memory_bus.retrieve(target_register)
        else:
            value = self.register.retrieve(target_register)
        return value


class Register:
    def __init__(self, register_size) -> None:
        self.register = [0 for i in range(0, register_size)]

    def insert(self, address, value):
        print("Saving {} to register at address: {}.".format(value, address))
        self.register[address] = value

    def retrieve(self, address):
        print("Retrieving value from register at address: {}".format(address))
        value = self.register[address]
        print(value)
        return int(value)
    
    def print_register(self):
        print("State of register: \n")
        print(self.register)
        print('\n')

class Memory_Bus:
    def __init__(self, size) -> None:
        self.memory = [0 for _ in range(0, size)]
    
    def insert(self, address, value):
        print("Saving {} to memory at address: {}.".format(value, address))
        self.memory[address] = value

    def retrieve(self, address):
        print("Retrieving value from memory at address: {}".format(address))
        value = self.memory[address]
        print(value)
        return int(value)
    
    def print_memory(self):
        print("State of Memory: \n")
        print(self.memory)
        print('\n')

test_cpu = CPU(Control_Unit(ALU(Register(32), Memory_Bus(32))))
test_cpu.read_instructions_from_file('instructions.txt')

