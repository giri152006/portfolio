# SET OPERATIONS


# UNION SET

def union_sets(set_a, set_b):
    union_set = set_a | set_b
    return union_set


# ADDING ELEMENT

def add_element(my_set, element):
    my_set.add(element)
    return my_set


# SUBSET

def is_subset(set_a, set_b):
    subset = set_a.issubset(set_b)
    return subset


# INTERSECTION SET
# INTERSECTION SET

def intersection_sets(set_a, set_b):
    intersection_set = set_a & set_b
    return intersection_set


# SYMMETRIC DIFFERENCE

def symmetric_difference(set_a, set_b):
    symmetric_difference = set_a ^ set_b
    return symmetric_difference


# REMOVE ELEMENT

def remove_element(my_set, element):
    my_set.remove(element)
    return my_set


# SET DIFFERNCE

def difference_sets(set_a, set_b):
    differnce_set = set_a - set_b
    return differnce_set


# DISJOINT
def is_disjoint(set_a, set_b):
    disjoint = set_a.isdisjoint(set_b)
    return disjoint


# CLEAR SET

def clear_set(my_set):
    my_set.clear()
    return my_set