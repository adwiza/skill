def bubble_sort(slist):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(slist) - 1):
            if slist[i] > slist[i + 1]:
                slist[i], slist[i + 1] = slist[i + 1], slist[i]
                was_swap = True
    return slist


def quick_sort(slist):
    if len(slist) <= 1:
        return slist
    pivot = slist[0]
    less_then = []
    more_then = []
    # equal = []
    for elem in slist:
        if elem > pivot:
            more_then.append(elem)
        elif elem < pivot:
            less_then.append(elem)
        # else:
        #     equal.append(elem)

    # return quick_sort(less_then) + equal + quick_sort(more_then)
    return quick_sort(less_then) + [pivot, ] + quick_sort(more_then)


def embedded_sort(slist):
    return list(set(sorted(slist)))
