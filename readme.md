# CPU Simulator

This project was created as part of the Codecademy [Computer Science Career Path](https://www.codecademy.com/career-journey/computer-science)

## What is it?
This is a CPU simulator, that simulates the way in which a CPU's control unit and ALU (Arithmetic Logic Unit) interpret instructions in binary. This is a fairly basic implementation, with only basic mathematical operations supported. Users can also save values to either cache or memory.
The CPU reads instructions from a separate text file containing instructions. This simulates machine language being converted into binary.

## How was it developed?
This is my most complex project to date, it relies on a lot of classes, representing the flow of data through the CPU. The CPU class has a control unit as a child, which sends instructions to the ALU. From there, the ALU performs any number of mathematical functions or saving and loading operations. The ALU has access to both the cache and memory data. 
The initial instruction is converted from machine language to binary, but I found it much easier to convert the values back to integers when working on them in the ALU. This is a little messy, but was much simpler and saved me a lot of trouble! This does make the conversion to binary a little redundant, but it illustrates what a real CPU would do.
The program is quite verbose, giving details about what it is doing at each step of the way. This helps to illustrate the process of a CPU being instruction being carried out.

Guidance on how to format instructions for the CPU are contained within the instructions.txt. As this is a plain text file, I had to include a way for the interpreter to ignore lines that were commented out, which was quite fun.

## Further Expansions
This project is far from perfect, but it performs enough to illustrate the main points. If I were to invest more time into it I would like to expand the available instruction set. I would also need to improve error and input checking as this is quite limited at present. It would also be nice to flesh out the machine language interpreter.

This project was quite complex, and I worry that it might not be particularly readable. This is something I'm trying to work on as I get my code out there more and more. I found it useful to use the [black formatter](https://black.readthedocs.io/en/stable/) for Python to help with formatting and readability.
