
def insert(sorted_list, value):
    i = 0
    while i < len(sorted_list) and value > sorted_list[i]:
        i += 1
    sorted_list.insert(i, value)

def insertion_sort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list



if __name__ == '__main__':
    # Example usage
    input_list = [5, 2, 8, 4, 7]
    print('Input list: '+ str(input_list))
    sorted_list = insertion_sort(input_list)
    print('Sorted list: '+ str(sorted_list))


