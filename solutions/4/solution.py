def find_median(numsa, numsb):
    count = len(numsa) + len(numsb)
    ret = 0
    if count == 0:
        return 0
    else:
        median_pos = int((count+1)/2)
        a_pos = 0
        b_pos = 0
        result = []
        while a_pos < len(numsa) and b_pos < len(numsb):
            numa = numsa[a_pos]
            numb = numsb[b_pos]
            if numa < numb:
                result.append(numa)
                a_pos += 1
            else:
                result.append(numb)
                b_pos += 1

        if a_pos == len(numsa):
            result += numsb[b_pos:]
        elif b_pos == len(numsb):
            result += numsa[a_pos:]

        if count % 2 == 0:
            ret = (result[median_pos-1]+result[median_pos])/2
        else:
            ret = result[median_pos-1]
    return ret


def find_median_optimized(lista, listb):
    lena, lenb = len(lista), len(listb)
    if lena > lenb:
        lista, listb, lena, lenb = listb, lista, lenb, lena

    if lenb == 0:
        raise ValueError

    cut_a_min = 0
    cut_a_max = lena
    half_len = int((lena+lenb+1)/2)
    while cut_a_min <= cut_a_max:
        cut_a_try = int((cut_a_min + cut_a_max)/2)
        cut_b_try = half_len - cut_a_try

        if cut_a_try < cut_a_max and listb[cut_b_try-1] > lista[cut_a_try]:
            cut_a_min = cut_a_try + 1
        elif cut_a_try > 0 and lista[cut_a_try-1] > listb[cut_b_try]:
            cut_a_max = cut_a_try - 1
        else:
            max_of_left = 0
            min_of_right = 0
            if cut_a_try == 0:
                max_of_left = listb[cut_b_try-1]
            elif cut_b_try == 0:
                max_of_left = lista[cut_a_try-1]
            else:
                max_of_left = max(lista[cut_a_try-1], listb[cut_b_try-1])

            if (lena + lenb) % 2 == 1:
                return max_of_left

            if cut_a_try == lena:
                min_of_right = listb[cut_b_try]
            elif cut_b_try == lenb:
                min_of_right = lista[cut_a_try]
            else:
                min_of_right = min(lista[cut_a_try], listb[cut_b_try])

            return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':
    print(find_median_optimized([1, 3], [2]))
    print('-------------')
    print(find_median_optimized([1, 2], [3, 4]))
