# This module helps dealing with files containing unicode (e.g. translations).
import codecs

# Create an empty list.
# The content of all .nml-files will be put into it.
print ("Creating sections...")
sections = []


def append_pnml(pnml):
    """Open a pnml file and append its content to a list."""
    print("Appending " + pnml)
    with codecs.open(pnml,'r','utf8') as pnml_obj:
        sections.append(pnml_obj.read())


def write_nml(nml):
    """Write the list created with 'append_nml' to a single nml file."""
    print ("Creating NML file...")
    with codecs.open(nml,'w','utf8') as nml_obj:
        nml_obj.write('\n'.join(sections))


# Use 'append_pnml' to store the content of all pnml files in a list.
append_pnml("src/pnml/header.pnml")
append_pnml("src/pnml/functions.pnml")
append_pnml("src/pnml/ground_sprites.pnml")
append_pnml("src/pnml/farm_fields.pnml")
append_pnml("src/pnml/farm_house.pnml")
append_pnml("src/pnml/old_town_houses.pnml")
append_pnml("src/pnml/shops_offices_1.pnml")
append_pnml("src/pnml/church.pnml")
append_pnml("src/pnml/town_hall.pnml")
append_pnml("src/pnml/farm_estate.pnml")
append_pnml("src/pnml/small_farm.pnml")
append_pnml("src/pnml/school.pnml")
append_pnml("src/pnml/old_house.pnml")
append_pnml("src/pnml/workshop.pnml")
append_pnml("src/pnml/house.pnml")
append_pnml("src/pnml/shop.pnml")
append_pnml("src/pnml/farm.pnml")
append_pnml("src/pnml/alley_houses.pnml")
append_pnml("src/pnml/town_church_1.pnml")
append_pnml("src/pnml/old_town_house.pnml")
append_pnml("src/pnml/trading_house.pnml")
append_pnml("src/pnml/merchant_house.pnml")
append_pnml("src/pnml/shops.pnml")
append_pnml("src/pnml/shops_offices_2.pnml")
append_pnml("src/pnml/mansion.pnml")
append_pnml("src/pnml/apartment_building.pnml")
append_pnml("src/pnml/multi_family_home.pnml")
append_pnml("src/pnml/high_school.pnml")
append_pnml("src/pnml/theatre.pnml")
append_pnml("src/pnml/cinema.pnml")
append_pnml("src/pnml/stadium.pnml")
append_pnml("src/pnml/hospital.pnml")
append_pnml("src/pnml/shops_offices_3.pnml")
append_pnml("src/pnml/city_park.pnml")
append_pnml("src/pnml/cathedral.pnml")
append_pnml("src/pnml/city_hall.pnml")
append_pnml("src/pnml/grand_hotel.pnml")
append_pnml("src/pnml/shopping_mall.pnml")
append_pnml("src/pnml/apartment_block_1.pnml")
append_pnml("src/pnml/town_church_2.pnml")
append_pnml("src/pnml/apartments_shops.pnml")
append_pnml("src/pnml/department_store.pnml")
append_pnml("src/pnml/guest_house.pnml")
append_pnml("src/pnml/hotel.pnml")
append_pnml("src/pnml/office_building.pnml")
append_pnml("src/pnml/large_office_building.pnml")
append_pnml("src/pnml/tall_office_building.pnml")


# Use 'write_nml' to create the nml file.
write_nml("cet.nml")
