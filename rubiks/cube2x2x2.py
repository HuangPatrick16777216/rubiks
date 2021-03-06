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

from typing import List


W: int = 0
Y: int = 1
B: int = 2
G: int = 3
R: int = 4
O: int = 5

MOVE_R: int = 6
MOVE_L: int = 7
MOVE_F: int = 8
MOVE_B: int = 9
MOVE_U: int = 10
MOVE_D: int = 11


class Move:
    """
    Class for a single move on a cube.
    """

    type: int
    prime: bool

    def __init__(self, type: int, prime: bool = False) -> None:
        """
        Initializes move.
        :param type: cube2x2x2.MOVE_R, cube2x2x2.MOVE_T, etc
        :param prime: Whether the move is prime (rotated ccw instead of cw)
        """
        self.type = type
        self.prime = prime

    def __repr__(self) -> str:
        string = Move.type_to_symbol(self.type)
        if self.prime:
            string += "'"
        return f"<2x2x2.Move.from_string(\"{string}\")>"

    def __str__(self) -> str:
        string = Move.type_to_symbol(self.type)
        if self.prime:
            string += "'"
        return string

    def __eq__(self, move) -> bool:
        return (self.type==move.type) and (self.prime==move.prime)

    @staticmethod
    def type_to_symbol(type: int) -> str:
        if type == MOVE_R:
            return "R"
        elif type == MOVE_L:
            return "L"
        elif type == MOVE_F:
            return "F"
        elif type == MOVE_B:
            return "B"
        elif type == MOVE_U:
            return "T"
        elif type == MOVE_D:
            return "B"
        raise ValueError(f"Move type {type} not allowed.")

    @staticmethod
    def symbol_to_type(symbol: str) -> int:
        if symbol == "R":
            return MOVE_R
        elif symbol == "L":
            return MOVE_L
        elif symbol == "F":
            return MOVE_F
        elif symbol == "B":
            return MOVE_B
        elif symbol == "T":
            return MOVE_U
        elif symbol == "B":
            return MOVE_D

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


class MoveSequence:
    """
    A sequence of moves.
    """

    moves: List[Move]

    def __init__(self, moves: List[Move] = []) -> None:
        """
        Initializes move sequence.
        :param moves: List of initial moves.
        """
        self.moves = list(moves)

    def __repr__(self) -> str:
        string = ", ".join([move.__str__() for move in self.moves])
        return f"<2x2x2.MoveSequence({string})>"

    def __getitem__(self, index: int) -> Move:
        return self.moves[index]

    def __contains__(self, move: Move) -> bool:
        return move in self.moves

    def append(self, move: Move) -> None:
        """
        Appends move to internal list.
        :param move: Move to append.
        """
        self.moves.append(move)

    def pop(self, index: int = -1) -> None:
        """
        Removes a move from the internal list.
        :param index: Index to pop.
        """
        self.moves.pop(index)

    def count(self, move: Move) -> int:
        return self.moves.count(move)
