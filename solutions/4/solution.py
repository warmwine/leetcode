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


if __name__ == '__main__':
    print(find_median([1, 3], [2]))
    print(find_median([1, 2], [3, 4]))
