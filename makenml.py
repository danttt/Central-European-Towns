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


# Open the file for the functions and append it to the list just created above
# This file contains the various switches designated as functions for town type, historical era sprite designation, road-awareness of houses etc.
print ("Appending functions...")
functions = codecs.open("pnml/functions.pnml",'r','utf8')
sections.append(functions.read())
functions.close()


# Open the file containing the nml-code for the custom ground sprites this set provides and append it to the "sections" list
print ("Appending ground sprites...")
ground_sprites = codecs.open("pnml/ground_sprites.pnml", 'r', 'utf8')
sections.append(ground_sprites.read())
ground_sprites.close()


# Open the file containing the nml-code for the custom ground sprites this set provides and append it to the "sections" list
print ("Appending farm fields...")
farm_fields = codecs.open("pnml/farm_fields.pnml", 'r', 'utf8')
sections.append(farm_fields.read())
farm_fields.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'farm house'...")
farm_house = codecs.open("pnml/farm_house.pnml", 'r', 'utf8')
sections.append(farm_house.read())
farm_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'town houses'...")
town_houses = codecs.open("pnml/town_houses.pnml", 'r', 'utf8')
sections.append(town_houses.read())
town_houses.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shops and offices 1'...")
shops_offices_1 = codecs.open("pnml/shops_offices_1.pnml", 'r', 'utf8')
sections.append(shops_offices_1.read())
shops_offices_1.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'church'...")
church = codecs.open("pnml/church.pnml", 'r', 'utf8')
sections.append(church.read())
church.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'town hall'...")
town_hall = codecs.open("pnml/town_hall.pnml", 'r', 'utf8')
sections.append(town_hall.read())
town_hall.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'farm estate'...")
farm_estate = codecs.open("pnml/farm_estate.pnml", 'r', 'utf8')
sections.append(farm_estate.read())
farm_estate.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'small farm'...")
small_farm = codecs.open("pnml/small_farm.pnml", 'r', 'utf8')
sections.append(small_farm.read())
small_farm.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'school'...")
school = codecs.open("pnml/school.pnml", 'r', 'utf8')
sections.append(school.read())
school.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'old house'...")
old_house = codecs.open("pnml/old_house.pnml", 'r', 'utf8')
sections.append(old_house.read())
old_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'workshop'...")
workshop = codecs.open("pnml/workshop.pnml", 'r', 'utf8')
sections.append(workshop.read())
workshop.close()


# Create the final .nml-file and make it writable
# Then write the "sections" list into 'cet.nml' using new lines for each part
print ("Creating NML file...")
processed_nml_file = codecs.open('cet.nml','w','utf8')
processed_nml_file.write('\n'.join(sections)) 
processed_nml_file.close()