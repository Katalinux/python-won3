def media(lst_note):
    """
    Average of values in the list.

    :param lst_note: List of int
    :type lst_note: list[int]
    :return: Average
    :rtype: float

    >>> media([1, 2, 3])
    2.0
    >>> media([1, 0, 2])
    1.0
    >>> media([])
    0.0
    """
    if len(lst_note) > 0:
        return sum(lst_note) / len(lst_note)
    return 0.0


def find_len(lst):
    """
    Find the longest string in tuple.
    :param lst: List of tuples
    :type lst: list
    :return:
    :rtype: int
    >>> find_len([('aaaa',), ('bb',), ('ccccc',)])
    5
    """
    ln = 4
    for tp in lst:
        if len(tp[0]) > ln:
            ln = len(tp[0])
    return ln


if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
