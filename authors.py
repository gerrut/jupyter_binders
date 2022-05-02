

def clearLine(line):
    line = line.title()
    line = cleanAuthors(line)
    return line

def cleanAuthors(authors):
    cleaned_author_list = []
    titles = ["Dr.", "Prof.", "Drs.", "Ing.", "Ir.", "Mr.", "Mevr."]
    for title in titles:
        authors = authors.replace(title, "")
    authors = authors.strip()

    # vervang " En " en " And " door een ,
    authors = authors.replace(" En ", ",")
    authors = authors.replace(" And ", ",")
    authors = authors.replace("&", ",")

    # extraheer individuele auteurs (let op, we gebruiken de komma!)
    author_list = authors.split(",")
    for author in author_list:
        cleaned_author_list.append(clean_author(author))
    return ("; ".join(cleaned_author_list))

def clean_author(author):
    first_name = ""
    middle_name = ""
    last_name = ""
    author_out = ""

    # Aanname: hooguit één van de voornamen is voluit en we beginnen altijd met voorletter of voornaam in dit journal
    # splits de naam aan de hand van de spatie
    name_parts = author.split(" ")
    for part in name_parts:
        if part.find(".") >= 0:
            if len(first_name)==0:
                first_name = part
            else:
                first_name += " "+ part
        elif len(part)==1:
            if len(first_name)==0:
                first_name = part+"."
            else:
                first_name += " "+ part+"."
        elif is_middle_name(part):
            if len(middle_name)== 0:
                middle_name = part
            else:
                middle_name += " " + part
        else:
            if len(first_name)==0:
                first_name = part
            elif len(last_name)==0:
                last_name = part
            else:
                last_name += " " + part

    author_out = last_name + ", " + first_name
    author_out = author_out.replace(". ", ".")
    if middle_name != "":
        author_out += " " + middle_name.lower()
    author_out = author_out.strip()
    author_out = author_out.replace("  ", " ")
    return author_out


def is_middle_name(part):
    tussenvoegsels = ["aan", "af", "bij", "de", "den", "der", "d'", "het", "'t", "in", "onder", "op", "over", "'s", "'t",
                      "te", "ten", "ter", "tot", "uit", "uijt", "van", "ver", "voor"]
    part = part.lower()
    part = part.strip()
    for tussenvoegsel in tussenvoegsels:
        if part == tussenvoegsel:
            return True
    return False

def test():
    print(clearLine("PROF. MR. L. G. A. SCHLICHTING"))
    print(clearLine("PROF. DR. G. KUYPERS en P. D. DUIKER"))
    print(clearLine("MEVR. DRS. G. E. VAN DER MAESEN en DRS. G. H. SGHOLTEN"))
    print(clearLine("A. DE SWAAN"))
    #tijdschrift twee (let op: de inhoudsopgave staat vaak achteraan)
    print(clearLine("R. B. Andeweg, K. L. L.M. Dittrich, M. P. H. van Haeften"))
    print(clearLine("C. van der Eijk and W. J. P. Kok"))
    #tijdschrift drie
    print(clearLine("R. A.G. van Puijenbroek en L.B. Snippenburg"))
    print(clearLine("JJ. vanCuiÏenburg,J. Kleinnijenhuis en J.A. de Ridder"))
    #tijdschrift vier
    print(clearLine("Wouter van der Brug and Huib Pellikaan"))
    print(clearLine("Joop J.M. van Holsteyn, Galen A. Irwin and J osje M. den Ridder"))

#test()