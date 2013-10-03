def pivot_indexer(the_list):
    the_list_summed = float(sum(the_list))
    cumulative_sum = float(0)
    for counter, item in enumerate(the_list):
        cumulative_sum = cumulative_sum + item
        cumulative_sum_less_item = cumulative_sum - item
        target = (the_list_summed - item) / 2
        if len(the_list) <=2 or counter == (len(the_list) - 1):
            return -1
        elif cumulative_sum_less_item == target:
            return counter
    return -1


