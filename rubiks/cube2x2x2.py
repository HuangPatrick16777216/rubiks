#
#  Rubiks
#  Python Rubik's Cube module.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

WHITE:   int = 0
YELLOW:  int = 1
BLUE:    int = 2
GREEN:   int = 3
RED:     int = 4
ORANGE:  int = 5

MOVE_R:  int = 6
MOVE_L:  int = 7
MOVE_F:  int = 8
MOVE_B:  int = 9
MOVE_T:  int = 10
MOVE_B:  int = 11


class Move:
    """
    Class for a single move on a cube.
    """

    type: int
    prime: bool

    def __init__(self, type: int, prime: bool = False):
        """
        Initializes move.
        :param type: cube2x2x2.MOVE_R, cube2x2x2.MOVE_T, etc
        :param prime: Whether the move is prime (rotated ccw instead of cw)
        """
        self.type = type
        self.prime = prime

    def __repr__(self):
        string = Move.type_to_symbol(self.type)
        if self.prime:
            string += "'"
        return f"<2x2x2.Move.from_string(\"{string}\")>"

    @staticmethod
    def type_to_symbol(type: int):
        if type == MOVE_R:
            return "R"
        elif type == MOVE_L:
            return "L"
        elif type == MOVE_F:
            return "F"
        elif type == MOVE_B:
            return "B"
        elif type == MOVE_T:
            return "T"
        elif type == MOVE_B:
            return "B"
        raise ValueError(f"Move type {type} not allowed.")

    @staticmethod
    def symbol_to_type(symbol: str):
        if symbol == "R":
            return MOVE_R
        elif symbol == "L":
            return MOVE_L
        elif symbol == "F":
            return MOVE_F
        elif symbol == "B":
            return MOVE_B
        elif symbol == "T":
            return MOVE_T
        elif symbol == "B":
            return MOVE_B

    @classmethod
    def from_string(cls, string: str):
        string = string.strip()
        if len(string) not in (1, 2):
            raise ValueError("String must have length 1 or 2.")
        if len(string) > 1 and string[1] != "'":
            raise ValueError("Second character must be apostrophe (')")

        type = Move.symbol_to_type(string[0])
        prime = len(string) > 1
        return cls(type, prime)
