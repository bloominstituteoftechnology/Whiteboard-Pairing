def time_planner(first_array, second_array, duration):
    # loop through first array
    for i_array in first_array:
        # loop through second array
        for j_array in second_array:
            # end = to the max both first array and the second
            end = max(i_array[1], j_array[1])
            # start = to the min of the first part of the data point
            start = max(i_array[0], j_array[0])
            # if end minus start is bigger than the duration for both first and second array.
            if end - start > duration:
                return (start, start+duration)
            # return array
    return []


print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
