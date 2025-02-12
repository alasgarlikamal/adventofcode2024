from collections.abc import Callable


class Part1:
    registers: dict[str, int]
    program: list[int]
    operations: dict[int, Callable]
    pointer: int = 0
    output: list[int] = []

    def __init__(self, input: str):

        registers, program = self.parse(input)
        self.registers = registers
        self.program = program
        self.operations = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def parse(self, input: str):
        with open(input, "r") as file:
            registers: dict[str, int] = {}
            program: list[int]
            (registers_text, program_text) = file.read().split("\n\n")
            for line in registers_text.split("\n"):
                _, register, value = line.split(" ")
                registers[register[0]] = int(value)

            program = list(map(int, program_text.split(" ")[1].split(",")))
            return registers, program

    def run(self):
        while self.pointer < len(self.program) - 1:
            self.operations[self.program[self.pointer]](self.program[self.pointer + 1])
        return ",".join((map(str, self.output)))

    def combo_operand(self, operand: int):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.registers["A"]
        elif operand == 5:
            return self.registers["B"]

        return self.registers["C"]

    def adv(self, operand: int):
        self.registers["A"] //= 2 ** self.combo_operand(operand)
        self.pointer += 2

    def bxl(self, operand: int):
        self.registers["B"] ^= operand
        self.pointer += 2

    def bst(self, operand: int):
        self.registers["B"] = self.combo_operand(operand) % 8
        self.pointer += 2

    def jnz(self, operand: int):
        if self.registers["A"] == 0:
            self.pointer += 2
        else:
            self.pointer = operand

    def bxc(self, operand: int):
        self.registers["B"] ^= self.registers["C"]
        self.pointer += 2

    def out(self, operand: int):
        self.output.append(self.combo_operand(operand) % 8)
        self.pointer += 2

    def bdv(self, operand: int):
        self.registers["B"] = self.registers["A"] // 2 ** self.combo_operand(operand)
        self.pointer += 2

    def cdv(self, operand: int):
        self.registers["C"] = self.registers["A"] // 2 ** self.combo_operand(operand)
        self.pointer += 2


solution = Part1("input.txt")
answer = solution.run()
print(answer)
