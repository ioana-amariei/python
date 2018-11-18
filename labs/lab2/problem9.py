# 9. Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter al celui
# 	de-al 2-lea element din tuplă. Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


def take_third_character_from_second_tuple(current_tuple):
    return current_tuple[1][2]


def get_sorted_from(list_of_tuples):
    list_of_tuples.sort(key=take_third_character_from_second_tuple)
    print(list_of_tuples)


get_sorted_from([('abc', 'bcd'), ('abc', 'zza')])

