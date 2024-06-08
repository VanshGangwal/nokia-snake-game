def speed_list_generator(starting_speed=0.2, percentage_increase=10, number_of_iteration=50):
    li = [starting_speed]
    for i in range(number_of_iteration):
        li.append(1 / ((1 / li[i]) * (1 + (percentage_increase / 100))))
    return li
