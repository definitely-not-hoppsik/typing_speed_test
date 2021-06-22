import numpy
"""
module contains methods for calculating distance between two strings

"""


def hamming_distance(text_1: str, text_2: str) -> int:
    """
    definition_1: number of positions, at which corresponding characters in two given strings
    of equal length are different
    definition_2: minimum number of single character operations (substituions) required to change
    one string into another; applies only to strings of the same length

    it is assumed, that the string are of equal lenght, however
    this function will strip the longer string to the lenght
    of the shorter one

    """
    if len(text_1) != len(text_2):
        raise ValueError("undefined for strings of different length")

    distance = 0

    for text_1_symbol, text_2_symbol in zip(text_1, text_2):
        if text_1_symbol != text_2_symbol:
            distance += 1

    return distance


def levenshtein_distance(text_1: str, text_2: str) -> int:
    """
    definition: minimum number of single character operations (insertions, deletions,substitutions)
    required to change one string into another

    """
    try:
        isinstance(text_1, str)
        isinstance(text_2, str)
    except:
        # TODO
        pass

    text_1_length = len(text_1)
    text_2_length = len(text_2)

    distance_matrix = [[0 for i in range(text_2_length+1)]
                       for j in range(text_1_length+1)]

    for i in range(text_1_length+1):
        distance_matrix[i][0] = i

    for j in range(text_2_length+1):
        distance_matrix[0][j] = j

    for i in range(1, text_1_length+1):
        for j in range(1, text_2_length+1):
            if text_1[i-1] == text_2[j-1]:
                cost = 0
            else:
                cost = 1

            above = distance_matrix[i-1][j]+1
            above_left = distance_matrix[i][j-1]+1
            above_diagonal = distance_matrix[i-1][j-1] + cost

            distance_matrix[i][j] = min(above, above_left, above_diagonal)

    return distance_matrix[text_1_length][text_2_length]
