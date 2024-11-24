# LISTS


# MAXIMUM OF A LIST

def find_max(my_list):
    maximum_number = max(my_list)
    return maximum_number


# SUM OF A LIST 

def list_sum(list_sum):
    sum = 0
    for element in list_sum:
        sum += element

    return sum


# APPENDING ELEMENTS

def append_element(list_append, element):
    list_append.append(element)
    return list_append
# AVERAGE OF A LIST

def average(list_average):
    sum = 0
    for element in list_average:
        sum += element

    average = sum / len(list_average)
    return average


# REMOVING ELEMENT

def remove_element(original_list, element):
    original_list.remove(element)
    return original_list


# REVERSING A LIST

def reverse_list(unreversed_list):
    reversed_list = unreversed_list[::-1]
    return reversed_list


# SORTING A LIST

def sort_list(unsorted_list):
    unsorted_list.sort()
    return unsorted_list

# OCCURENCE

def count_occurrences(my_list, repeated_element):
    count = my_list.count(repeated_element)
    return count


# FINDING INDEX

def find_index(the_list, index_element):
    index_number = the_list.index(index_element)
    return index_number