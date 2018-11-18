# 5. Fie functia validate_dict care primeste ca parametru un set de tuple care reprezinta reguli de validare pentru un
#  dictionar cu chei de tipul string si valori tot de tipul string si un dictionar.
#   O regula este definita astfel:
# 	(cheie, "prefix", "middle", "sufix").
#   O valoare este considerata valida daca incepe cu "prefix", "middle" se gaseste in
# 	interiorul valorii (nu la inceput sau sfarsit) si se sfarsete cu "sufix".

# 	Functia va returna True daca dictionarul dat ca parametru respecta toate regulile, False in caz contrar.

# 	Exemplu: regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] si
# 	dictionarul {"key2": "starting the engine in the middle of the winter",
#   "key1": "come inside, it's too cold outside", "key3": "this is not valid"} => False
# 	deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3" care nu apare in reguli.


def is_valid_value(prefix, middle, suffix, value):
    return value.startswith(prefix) \
           and middle in value \
           and value.endswith(suffix) \
           and not value.startswith(middle) \
           and not value.endswith(middle)


def validate_dict(validation_rules, dictionary):
    dictionary_copy = dictionary.copy()
    for key, prefix, middle, suffix in validation_rules:
        if key not in dictionary:
            return False
        if is_valid_value(prefix, middle, suffix, dictionary[key]) is not True:
            return False
        dictionary_copy.pop(key)

    if len(dictionary_copy) is not 0:
        return False

    return True


print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
                    {"key2": "starting the engine in the middle of the winter",
                     "key1": "come inside, it's too cold outside", "key3": "this is not valid"}))

print(validate_dict([("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "this", "valid", "valid")],
                    {"key2": "starting the engine in the middle of the winter",
                     "key1": "come inside, it's too cold outside", "key3": "this is not valid"}))
