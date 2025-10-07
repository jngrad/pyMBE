import re

def martini3_conversion(filepath_aminoacids):
    """
    Convert the Martini3 amino acids forcefield to make it parseable by ParmEd.
    """
    assert filepath_aminoacids.rsplit("/", 1)[1] == "aminoacids.ff"
    with open(filepath_aminoacids) as f:
        content = f.read().replace("#meta", ";meta").split("\n;;; Links", 1)[0].replace("$stiff_fc", "1000000")

    breakpoints = []
    for m in re.finditer("\n;;; ", content):
        breakpoints.append(m.start())
    breakpoints.append(len(content))

    for i in list(range(len(breakpoints)-1))[::-1]:
        start, stop = (breakpoints[i], breakpoints[i+1])
        block = content[start:stop]
        type2id = {}
        for line in re.search(r"\[ *atoms *\]([\s\S]*?)(?=$|\n\[)", block).group(1).split("\n"):
            line = line.strip()
            if not line or line[0] == ";":
                continue
            tokens = line.split()
            type2id[tokens[4]] = tokens[0]
        for section in re.findall(r"\n\[ *(?:constraints|bonds|angles|dihedrals) *\]([\s\S]*?)(?=$|\n\[)", block):
            section_remapped = section
            for typ, idx in type2id.items():
                section_remapped = re.sub(rf"(\s){re.escape(typ)}(\s)", rf"\g<1>{idx}\g<2>", section_remapped)
            block = block.replace(section, section_remapped)
        block = re.sub(r"\n\[ *exclusions *\]([\s\S]*)(?=$|\n\[)", "", block)
        content = content.replace(content[start:stop], block)

    with open(filepath_aminoacids.rsplit(".", 1)[0] + ".itp", "w") as f:
        f.write(content)
