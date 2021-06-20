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

    length_text_1 = len(text_1)
    length_text_2 = len(text_2)

    distance_matrix = [[0 for i in range(length_text_1)]
                       for j in range(length_text_2)]

    for i in range(length_text_1):
        distance_matrix[0][i] = i

    for i in range(length_text_2):
        distance_matrix[i][0] = i

    for i in range(length_text_1):
        for j in range(length_text_2):
            if text_1[i] == text_2[j]:
                cost = 0
                # TODO
