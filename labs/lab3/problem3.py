# 3. Sa se compare doua dictionare fara a folosi operatorul "==" si sa se returneze un tuplu de liste de diferente astfel:
#
#   (cheile_comune_dar_cu_valori_diferite,
#   cheile_care_se_gasesc_doar_in_primul_dict,
#   cheile_care_se_gasesc_doar_in_al_doilea_dict).
#
#   (Atentie, dictionarele trebuiesc parcurse recursiv deoarece la randul lor pot contine alte containere,
#   cum ar fi dictionare, liste, set-uri, etc)


def compare_dictionaries(first, second):
    common_keys_different_values = list(set(x for x in first.keys() for x in second.keys() if first.get(x) != second.get(x)))

    keys_from_first = set(x for x in first.keys())
    keys_from_second = set(x for x in second.keys())

    keys_from_first_only = list(keys_from_first.difference(keys_from_second))
    keys_from_second_only = list(keys_from_second.difference(keys_from_first))

    return common_keys_different_values, keys_from_first_only, keys_from_second_only


print(compare_dictionaries({"a": 3, "b": 2, "d": 5}, {"a": 1, "b": 2, "c": 4}))
