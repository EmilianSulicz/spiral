def spiral(input_data):
    my_data = input_data
    result = []
    while my_data:
        for index, element in enumerate(my_data):
            if index == 0:
                result.extend(element)
            elif index != len(my_data) - 1:
                result.append(element[-1])
                del my_data[index][-1]
            else:
                result.extend(element[::-1])
                del my_data[-1]
        del my_data[0]

        my_data.reverse()
        for index, element in enumerate(my_data):
            if not element:
                del my_data[index]
            else:
                result.append(element[0])
                del my_data[index][0]
        my_data.reverse()

    return result
