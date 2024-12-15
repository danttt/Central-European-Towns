import codecs


def append_pnml(pnmllist, pnml):
    """Open a pnml file and append its content to a list."""
    print ("Creating sections...")
    
    print("Appending " + pnml)
    with codecs.open(pnml,'r','utf8') as pnml_obj:
        pnmllist.append(pnml_obj.read())


def write_nml(nml, list):
    """Write the list created with 'append_nml' to a single nml file."""
    print ("Creating NML file...")
    with codecs.open(nml,'w','utf8') as nml_obj:
        nml_obj.write('\n'.join(list))
