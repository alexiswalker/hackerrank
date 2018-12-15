def elements_in_even_positions(c):
    return [number for i, number in enumerate(c) if i % 2 == 0]


def jumpingOnClouds(c):
    elements = len(c)
    if elements % 2 == 0:
        return elements / 2
    else:
        positions = elements_in_even_positions(c)
        print positions
        if 1 in positions:
            return elements // 2
        else:
            return elements // 2 + 1


print jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
