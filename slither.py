#!/usr/bin/python3
import argparse
import sys


class Board:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return self.numbers.rstrip('\n')

    @classmethod
    def from_string(cls, s):
        return cls(s)


def get_board():
    parser = argparse.ArgumentParser()
    parser.add_argument('board')
    args = parser.parse_args()
    with open(args.board) as f:
        data = f.read()
    return Board.from_string(data)


def solve(board):
    return board


if __name__ == '__main__':
    print(solve(get_board()))
