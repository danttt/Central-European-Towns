# Credit for this code goes to andythenorth and his comprehensive non-comprehensive templating tutorial in the TT-forums (https://www.tt-forums.net/viewtopic.php?f=68&t=58390)


# Always tell me what you do as I run this script, my dear Python compiler
print ("Running script...")


# This module helps dealing with files that contain unicode (e.g. translations)
import codecs


# Create an empty list where the content of all .nml-files will be included by this script
print ("Creating sections...")
sections = []


# Open the header file and append it to the list just created above
# The header contains the grf block, cargo table, sprite templates etc.
print ("Appending header...")
header = codecs.open("pnml/header.pnml",'r','utf8')
sections.append(header.read())
header.close()


# Create the final .nml-file and make it writable
# Then write the "sections" list into 'cet.nml' using new lines for each part
print ("Creating NML file...")
processed_nml_file = codecs.open('cet.nml','w','utf8')
processed_nml_file.write('\n'.join(sections)) 
processed_nml_file.close()