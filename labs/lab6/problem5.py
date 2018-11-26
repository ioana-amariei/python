# Write another variant of the function from the previous exercise that returns those elements
# 	that have at least one attribute that corresponds to a key-value pair in the dictionary.


import re


def corresponding_elements(xml_path, attrs):
    elements = set()
    keys = attrs.keys()

    try:
        f = open(xml_path, "r")
        content = f.readline()
        element_pattern = "(\w+)"

        while content:
            for key in keys:
                if re.search(key, content) and re.search(attrs[key], content):
                    result = re.search(element_pattern, content)
                    if result:
                        elements.add(result.group(0))
            content = f.readline()

        f.close()
    except Exception as e:
        print(e)

    return list(elements)


price_attributes_dictionary = {
    'coin': 'euros',
    'recommendations': 'true',
    'fast': 'true'
}
details_attributes_dictionary = {
    'detailed': 'true'
}


print(corresponding_elements("menu.xml", price_attributes_dictionary))
print(corresponding_elements("menu.xml", details_attributes_dictionary))