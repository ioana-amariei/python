# Write a function that receives as a parameter the path to an xml document and an attrs dictionary and
# returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values.
# For example, for the dictionary:
#       {"class": "url", "name": "url-form", "data-id": "item"}
# will be selected the elements that have the attributes:
#       class = "url" and name = "url", "name": "url-form", " "url-form" and date-id = "item".
import re


def corresponding_elements(xml_path, attrs):
    elements = set()
    keys = attrs.keys()

    try:
        f = open(xml_path, "r")
        content = f.readline()
        element_pattern = "(\w+)"

        while content:
            current_elements = set()
            counter = 0
            for key in keys:
                if re.search(key, content) and re.search(attrs[key], content):
                    result = re.search(element_pattern, content)
                    if result:
                        counter += 1
                        current_elements.add(result.group(0))
            if counter == len(keys):
                for elem in current_elements:
                    elements.add(elem)
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