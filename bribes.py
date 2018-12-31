queue = [1, 2, 5, 3, 4, 7, 8, 6]


def is_ahead(member, index):
    return member > index + 1


def minimumBribes(q):

    r = 0
    for i in range(len(q)):
        number = i + 1
        index = q.index(number)
        if any([p < number for p in q[index + 1:]]):

            distance = i - index
            if distance > 2:
                print ('Too chaotic')
                return

            r += sum([1 for k in q[index + 1:] if k < number])
            
    print (r)
    return


minimumBribes(queue)
