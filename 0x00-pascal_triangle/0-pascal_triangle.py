#!/usr/bin/python3
"""Pascal Triangle Interview Challenge for Alx project written by Dennis"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # This code explained that  a row is  fill first and last idx with 1
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for p in range(1, i):
            if p > 0 and p < len(row):
                x = pascal_triangle[i - 1][p]
                y = pascal_triangle[i - 1][p - 1]
                row[p] = x + y

        pascal_triangle[i] = row

    return pascal_triangle
