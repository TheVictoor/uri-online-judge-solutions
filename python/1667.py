import re

text = []

while True:
    try:
        inp = input()
        text.append(inp)
    except:
        break

text = " ".join(text)

text = text.strip()
text = re.sub(r"\s+", " ", text)


def replace_function(tag: re.Match):
    value = tag.group(0)

    if value == "\n <hr> " or value == "\n<hr> " or value == "\n<hr>":
        return "\n" + ("-" * 80) + "\n"
    if value == " <hr> " or value == "<hr> " or value == "<hr>":
        return ("-" * 80) + "\n"
    if value == " <br> " or value == "<br> " or value == "<br>":
        return "\n"


def fix_rule(match: re.Match):
    value = match.group(0)
    parts = re.split(r"\b", value)

    if len(parts) == 1:
        parts[0] = parts[0][:-1] + "\n" + parts[0][-1]
        return "".join(parts)

    last_part = parts[-1]

    if last_part == "":
        parts[-3] = "\n"
    else:
        parts[-1] = "\n" + parts[-1]

    return "".join(parts)


text = re.sub(r"(\n\s?<hr>\s?)|(\s?<hr>\s?)|(\s?<br>\s?)", replace_function, text)
text = re.sub(r"[^\n]{81}", fix_rule, text)
text = re.sub(r"\s+$", "", text)
text = re.sub(r"\n ", "\n", text)

print(text)
