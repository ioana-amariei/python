# 4. Fie functia build_xml_element care primeste urmatorii parametri:
#   tag, content si elemente cheie-valoare date ca parametri cu nume.
# 	Sa se construiasca si sa se returneze un string care reprezinta elementul XML aferent.
# 	Exemplu: build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid") =>
# 	"<a href=\"http://python.org\" _class=\"my-link\" id=\"someid\">Hello there</a>"


def build_xml_element(tag, content, dictionary):
    start_tag = "<" + tag + " "
    end_tag = "</" + tag + ">"

    xml_element = start_tag
    for key in dictionary:
        xml_element += key + "=\\\"" + dictionary.get(key) + "\\\" "
    xml_element += ">" + content + end_tag

    return xml_element


print(build_xml_element("a", "Hello there", {"href": "http://python.org", "_class": "my-link", "id": "someid"}))
