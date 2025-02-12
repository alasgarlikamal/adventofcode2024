from collections.abc import Callable


class Part2:
    registers: dict[str, int]
    program: list[int]
    operations: dict[int, Callable]
    pointer: int = 0
    output: list[int] = []

    def __init__(self, input: str):

        self.program = self.parse(input)
        self.registers = {
            "A": 0,
            "B": 0,
            "C": 0,
        }

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
            program_text = file.read().split("\n\n")[1]
            return list(map(int, program_text.split(" ")[1].split(",")))

    def run_part1(self):
        while self.pointer < len(self.program) - 1:
            self.operations[self.program[self.pointer]](self.program[self.pointer + 1])
        return self.output

    def run(self):
        a = 0
        j = 1
        istart = 0
        while j <= len(self.program) and j >= 0:
            a <<= 3
            for i in range(istart, 8):
                self.registers["A"] = a + i
                self.registers["B"] = 0
                self.registers["C"] = 0
                self.pointer = 0
                self.output = []
                out = self.run_part1()
                if self.program[-j:] == out:
                    break
            else:
                j -= 1
                a >>= 3
                istart = a % 8 + 1
                a >>= 3
                continue
            j += 1
            a += i
            istart = 0
        return a

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


solution = Part2("input.txt")
answer = solution.run()
print(answer)
