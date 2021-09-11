#Binary Search  complexity O(log^2n)

"""
look for the value 90 but instead of start at the start start at the middle. if the middle element is less than the element youre looking for discard all the elements to the left of the middle object. if the middle element is greater than 90 than the values to the right are discared
[44, 53, 54, 56, 59, 90, 95, 717, 6756, 918845]
the next middle element is 59 which is less than 90 so all elements to the left are discarded from the search
[90, 95, 717, 6756, 918845]
717 is greater than 90 so all the elements to the right are discarded
[90, 95]
90 is the next middle number and 90 is the value we're looking for

it took 4 jumps or steps to find the value we're searching for.
done sequentially with a queue this would of taken 17 jumps
log^2(21) == 4.39 which is rounded the amount of steps to get to the solution with a binary search

"""
ls1 = [1, 3, 4, 5, 7, 9, 13, 14, 22, 34, 38, 44, 53, 54, 56, 59, 90, 95, 717, 6756, 918845]

"""
a binary search works by making a step that leaves you one of two choices to make.
at every jump you get rid of nearly half of the elements as you had before that step.
"""