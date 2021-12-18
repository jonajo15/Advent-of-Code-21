from dataclasses import dataclass
from functools import reduce

filename = 'days/16/input.txt'


@dataclass
class Packet:
    binary: str
    length: int
    version: int
    type: int
    sub_packets: list

    def __init__(self, binary):
        self.binary = binary
        self.version = int(binary[:3], 2)
        self.type = int(binary[3:6], 2)
        self.length = 0

        if self.type == 4:
            self.sub_packets = []
            self.value = self.get_literal()
        else:
            self.sub_packets = self.get_sub_packets()
            self.value = self.calculate()

    def get_literal(self):
        binary = ''
        i = 6
        not_last_group = 1

        while not_last_group:
            not_last_group = int(self.binary[i], 2)
            binary += self.binary[i + 1: i + 5]

            i += 5

        self.length = i
        return int(binary, 2)

    def get_sub_packets(self):
        sub_packets = []
        length_type_id = int(self.binary[6], 2)
        l_length = 15 if length_type_id == 0 else 11
        detail = int(self.binary[7: 7 + l_length], 2)

        if length_type_id == 0:
            self.length = 7 + l_length + detail

            sub_packet = self.binary[7 + l_length: self.length]

            while sub_packet:
                packet = Packet(sub_packet)
                sub_packets.append(packet)
                sub_packet = sub_packet[packet.length:]
        else:
            sub_packet = self.binary[7 + l_length:]
            self.length = 7 + l_length

            for _ in range(detail):
                packet = Packet(sub_packet)
                sub_packets.append(packet)

                self.length += packet.length
                sub_packet = sub_packet[packet.length:]

        return sub_packets

    def sum_versions(self):
        version_sum = self.version

        if self.sub_packets:
            for sub in self.sub_packets:
                version_sum += sub.sum_versions()

        return version_sum

    def calculate(self):
        sub_values = list(map(lambda p: p.value, self.sub_packets))

        if self.type == 0:
            return sum(sub_values)
        elif self.type == 1:
            return reduce((lambda x, y: x * y), sub_values)
        elif self.type == 2:
            return min(sub_values)
        elif self.type == 3:
            return max(sub_values)
        elif self.type == 5:
            return 1 if sub_values[0] > sub_values[1] else 0
        elif self.type == 6:
            return 1 if sub_values[0] < sub_values[1] else 0
        elif self.type == 7:
            return 1 if sub_values[0] == sub_values[1] else 0

        return 0


def read_file_to_string():
    with open(filename) as file:
        return file.read().rstrip()


def task1():

    # hex to binary
    hexa = read_file_to_string()
    fill = len(hexa) * 4
    binary = (bin(int(hexa, 16))[2:]).zfill(fill)

    packet = Packet(binary)

    print("\tAnswer: ", packet.sum_versions())


def task2():

    # hex to binary
    hexa = read_file_to_string()
    fill = len(hexa) * 4
    binary = (bin(int(hexa, 16))[2:]).zfill(fill)

    packet = Packet(binary)

    print("\tAnswer: ", packet.value)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
