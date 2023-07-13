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
header = codecs.open("src/pnml/header.pnml",'r','utf8')
sections.append(header.read())
header.close()


# Open the file for the functions and append it to the list just created above
# This file contains the various switches designated as functions for town type, historical era sprite designation, road-awareness of houses etc.
print ("Appending functions...")
functions = codecs.open("src/pnml/functions.pnml",'r','utf8')
sections.append(functions.read())
functions.close()


# Open the file containing the nml-code for the custom ground sprites this set provides and append it to the "sections" list
print ("Appending ground sprites...")
ground_sprites = codecs.open("src/pnml/ground_sprites.pnml", 'r', 'utf8')
sections.append(ground_sprites.read())
ground_sprites.close()


# Open the file containing the nml-code for the custom ground sprites this set provides and append it to the "sections" list
print ("Appending farm fields...")
farm_fields = codecs.open("src/pnml/farm_fields.pnml", 'r', 'utf8')
sections.append(farm_fields.read())
farm_fields.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'farm house'...")
farm_house = codecs.open("src/pnml/farm_house.pnml", 'r', 'utf8')
sections.append(farm_house.read())
farm_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'old town houses'...")
old_town_houses = codecs.open("src/pnml/old_town_houses.pnml", 'r', 'utf8')
sections.append(old_town_houses.read())
old_town_houses.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shops and offices 1'...")
shops_offices_1 = codecs.open("src/pnml/shops_offices_1.pnml", 'r', 'utf8')
sections.append(shops_offices_1.read())
shops_offices_1.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'church'...")
church = codecs.open("src/pnml/church.pnml", 'r', 'utf8')
sections.append(church.read())
church.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'town hall'...")
town_hall = codecs.open("src/pnml/town_hall.pnml", 'r', 'utf8')
sections.append(town_hall.read())
town_hall.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'farm estate'...")
farm_estate = codecs.open("src/pnml/farm_estate.pnml", 'r', 'utf8')
sections.append(farm_estate.read())
farm_estate.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'small farm'...")
small_farm = codecs.open("src/pnml/small_farm.pnml", 'r', 'utf8')
sections.append(small_farm.read())
small_farm.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'school'...")
school = codecs.open("src/pnml/school.pnml", 'r', 'utf8')
sections.append(school.read())
school.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'old house'...")
old_house = codecs.open("src/pnml/old_house.pnml", 'r', 'utf8')
sections.append(old_house.read())
old_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'workshop'...")
workshop = codecs.open("src/pnml/workshop.pnml", 'r', 'utf8')
sections.append(workshop.read())
workshop.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'house'...")
house = codecs.open("src/pnml/house.pnml", 'r', 'utf8')
sections.append(house.read())
house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shop'...")
shop = codecs.open("src/pnml/shop.pnml", 'r', 'utf8')
sections.append(shop.read())
shop.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'farm'...")
farm = codecs.open("src/pnml/farm.pnml", 'r', 'utf8')
sections.append(farm.read())
farm.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'alley houses'...")
alley_houses = codecs.open("src/pnml/alley_houses.pnml", 'r', 'utf8')
sections.append(alley_houses.read())
alley_houses.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'town church 1'...")
town_church_1 = codecs.open("src/pnml/town_church_1.pnml", 'r', 'utf8')
sections.append(town_church_1.read())
town_church_1.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'old town house'...")
old_town_house = codecs.open("src/pnml/old_town_house.pnml", 'r', 'utf8')
sections.append(old_town_house.read())
old_town_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'trading house'...")
trading_house = codecs.open("src/pnml/trading_house.pnml", 'r', 'utf8')
sections.append(trading_house.read())
trading_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'merchant house'...")
merchant_house = codecs.open("src/pnml/merchant_house.pnml", 'r', 'utf8')
sections.append(merchant_house.read())
merchant_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shops'...")
shops = codecs.open("src/pnml/shops.pnml", 'r', 'utf8')
sections.append(shops.read())
shops.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shops and offices 2'...")
shops_offices_2 = codecs.open("src/pnml/shops_offices_2.pnml", 'r', 'utf8')
sections.append(shops_offices_2.read())
shops_offices_2.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'mansion'...")
mansion = codecs.open("src/pnml/mansion.pnml", 'r', 'utf8')
sections.append(mansion.read())
mansion.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'apartment building'...")
apartment_building = codecs.open("src/pnml/apartment_building.pnml", 'r', 'utf8')
sections.append(apartment_building.read())
apartment_building.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'multi family home'...")
multi_family_home = codecs.open("src/pnml/multi_family_home.pnml", 'r', 'utf8')
sections.append(multi_family_home.read())
multi_family_home.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'high school'...")
high_school = codecs.open("src/pnml/high_school.pnml", 'r', 'utf8')
sections.append(high_school.read())
high_school.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'theatre'...")
theatre = codecs.open("src/pnml/theatre.pnml", 'r', 'utf8')
sections.append(theatre.read())
theatre.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'cinema'...")
cinema = codecs.open("src/pnml/cinema.pnml", 'r', 'utf8')
sections.append(cinema.read())
cinema.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'stadium'...")
stadium = codecs.open("src/pnml/stadium.pnml", 'r', 'utf8')
sections.append(stadium.read())
stadium.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'hospital'...")
hospital = codecs.open("src/pnml/hospital.pnml", 'r', 'utf8')
sections.append(hospital.read())
hospital.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shops and offices 3'...")
shops_offices_3 = codecs.open("src/pnml/shops_offices_3.pnml", 'r', 'utf8')
sections.append(shops_offices_3.read())
shops_offices_3.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'city park'...")
city_park = codecs.open("src/pnml/city_park.pnml", 'r', 'utf8')
sections.append(city_park.read())
city_park.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'cathedral'...")
cathedral = codecs.open("src/pnml/cathedral.pnml", 'r', 'utf8')
sections.append(cathedral.read())
cathedral.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'city hall'...")
city_hall = codecs.open("src/pnml/city_hall.pnml", 'r', 'utf8')
sections.append(city_hall.read())
city_hall.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'grand hotel'...")
grand_hotel = codecs.open("src/pnml/grand_hotel.pnml", 'r', 'utf8')
sections.append(grand_hotel.read())
grand_hotel.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'shopping mall'...")
shopping_mall = codecs.open("src/pnml/shopping_mall.pnml", 'r', 'utf8')
sections.append(shopping_mall.read())
shopping_mall.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'apartment block 1'...")
apartment_block_1 = codecs.open("src/pnml/apartment_block_1.pnml", 'r', 'utf8')
sections.append(apartment_block_1.read())
apartment_block_1.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'town church 2'...")
town_church_2 = codecs.open("src/pnml/town_church_2.pnml", 'r', 'utf8')
sections.append(town_church_2.read())
town_church_2.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'apartments and shops'...")
apartments_shops = codecs.open("src/pnml/apartments_shops.pnml", 'r', 'utf8')
sections.append(apartments_shops.read())
apartments_shops.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'department store'...")
department_store = codecs.open("src/pnml/department_store.pnml", 'r', 'utf8')
sections.append(department_store.read())
department_store.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'guest house'...")
guest_house = codecs.open("src/pnml/guest_house.pnml", 'r', 'utf8')
sections.append(guest_house.read())
guest_house.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'hotel'...")
hotel = codecs.open("src/pnml/hotel.pnml", 'r', 'utf8')
sections.append(hotel.read())
hotel.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'office building'...")
office_building = codecs.open("src/pnml/office_building.pnml", 'r', 'utf8')
sections.append(office_building.read())
office_building.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'large office building'...")
large_office_building = codecs.open("src/pnml/large_office_building.pnml", 'r', 'utf8')
sections.append(large_office_building.read())
large_office_building.close()


# Open the file containing the nml-code for this house type and append it to the "sections" list
print ("Appending house type 'tall office building'...")
tall_office_building = codecs.open("src/pnml/tall_office_building.pnml", 'r', 'utf8')
sections.append(tall_office_building.read())
tall_office_building.close()


# Create the final .nml-file and make it writable
# Then write the "sections" list into 'cet.nml' using new lines for each part
print ("Creating NML file...")
processed_nml_file = codecs.open('cet.nml','w','utf8')
processed_nml_file.write('\n'.join(sections)) 
processed_nml_file.close()