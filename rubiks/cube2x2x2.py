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
MOVE_RP: int = 7
MOVE_L:  int = 8
MOVE_LP: int = 9

MOVE_F:  int = 10
MOVE_FP: int = 11
MOVE_B:  int = 12
MOVE_BP: int = 13

MOVE_T:  int = 14
MOVE_TP: int = 15
MOVE_B:  int = 16
MOVE_BP: int = 17


class Move:
    """
    Class for a single move on a cube.
    """

    _type: int
    _prime: bool

    def __init__(self, move_type: int, prime: bool = False):
        """
        Initializes move.
        :param move_type: cube2x2x2.MOVE_R, cube2x2x2.MOVE_T, etc
        :param prime: Whether the move is prime (rotated ccw instead of cw)
        """
        self._type = move_type
        self._prime = prime
