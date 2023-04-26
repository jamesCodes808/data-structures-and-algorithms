def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        # sort the left side
        merge_sort(left)

        # sort the right side
        merge_sort(right)

        # merge the sorted left and right sides together
        merge(left, right, lst)


def merge(left, right, lst):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    # set remaining entries in lst to remaining values in left or right
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    lst = [5, 2, 9, 1, 7, 4]
    merge_sort(lst)
    print(lst)
