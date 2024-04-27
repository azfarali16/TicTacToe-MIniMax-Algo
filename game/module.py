from enum import Enum
from dataclasses import dataclass


@dataclass
class Board:
    def __post_init__(self):
        self._board = [[' ' for _ in range(3)] for _ in range(3)]

    def get_cell(self, row, col):
        return self._board[row][col]

    def set_cell(self, row, col, value):
        self._board[row][col] = value
    
    def display(self):
        print(self._board)

    def __iter__(self):
        return iter(self._board)
    
    def get_possible_moves(self):
        moves = [(row, col) for row in range(3) for col in range(3) if self._board[row][col] == " "]
        return moves


@dataclass
class Mark(str,Enum):
    CROSS = "X"
    CIRCLE = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.CIRCLE else Mark.CIRCLE    



def main():
    mark = Mark.CIRCLE
    print(mark.value)
    print(mark.other.value)
    return 0


if __name__ == "__main__":
    main()
