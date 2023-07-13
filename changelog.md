Central European Towns 0.7.0 (2023-07-08) (Build 7)
----------------------------------------------------
- ADD: house type apartments and shops
- ADD: house type department store
- ADD: house type guest house
- ADD: house type hotel
- ADD: house type office building
- ADD: house type large office building
- ADD: house type tall office building
- CHANGE: Set standard probability of all houses to 7 in order to define some lower or higher probabilities later
- CHANGE: Set probability for farm estate to 1, was appearing to often in villages


Central European Towns 0.6.0 (2023-07-08) (Build 6)
----------------------------------------------------
- FEATURE: cities create a ring of historistic (late 19th century) block perimeter houses
- ADD: house type apartment block 1
- ADD: house type town church 2
- ADD: Full set of sprites for white block perimeter circle for shops and offices 3
- CHANGE: church for towns and cities has now a life span of only 20 years since it protects the historistic buildings around it
- CHANGE: Roof colors of most old town houses (alley houses ,trading house) are now red or close to that


Central European Towns 0.5.0 (2023-06-29) (Build 5)
----------------------------------------------------
- FEATURE: Expanding city park with only roads as limitations
- ADD: expanded house type old town house to cities
- ADD: expanded house type shops to cities
- ADD: expanded house type shops and offices 2 to cities
- ADD: expanded house type apartment building to cities
- ADD: expanded house type multi family home to cities
- ADD: expanded house type high school to cities
- ADD: expanded house type town church 1 to cities
- ADD: house type shops and offices 3
- ADD: house type cathedral
- ADD: house type city hall
- ADD: house type grand hotel the appearance of which is regulated by proximity functions (can only be built near larger station or special city buildings)
- ADD: house type shopping mall
- ADD: Function for proximity detection of larger stations (three or more tiles)
- ADD: Function for proximity detection of special buildings (building class 3)
- CHANGE: house types theatre and cinema appear now in cities
- CHANGE: trading house is only available in cities and in era01
- CHANGE: old town houses now appear in cities only in era01
- CHANGE: shops and offices 1 (historistic block perimeter houses) only appear in era02
- CHANGE: alley houses and merchant house appear in cities in era01, in era02 they only appear in towns
- CHANGE: town church 1 and high school in towns limited via distance rather than via unique building switch
- CHANGE: road awareness function now distinguishes between the cases of no road being around the building tile and road tiles in multiple directions
- CHANGE: shops and offices 1 has now seperate sprite each for backyard (no road around) and non-block-perimeter (roads around in multiple directions)
- FIX: Red farm fields were to flashy, colored them in a darker red


Central European Towns 0.4.0 (2023-06-23) (Build 4)
----------------------------------------------------
- ADD: house type alley houses for Towns
- ADD: house type house for towns and cities
- ADD: house type town church 1 (2X1 orientation)
- ADD: house type old town house
- ADD: house type trading house (for towns)
- ADD: house type merchant house (for towns)
- ADD: house type shops for towns
- ADD: house type shops and offices 2 for towns
- ADD: house type mansion
- ADD: house type apartment building for towns
- ADD: house type multi family home for villages and towns
- ADD: house type high school for towns
- ADD: house type theatre (for towns)
- ADD: house type cinema (for towns)
- ADD: expanded house type church to appear in towns and cities
- ADD: house type stadium
- ADD: house type hospital
- CHANGE: Rename house type town houses as old town houses 
- CHANGE: Excluded renamed house type old town houses from town zone 4 (was all before)
- CHANGE: Rename house type church item for villages
- CHANGE: Expand church appearance to all eras
- FIX: Unified sprites so that all are ready for snow addition
- FIX: Unified sprite denotation for the parts of multi-tile houses (..._00x_N instead of ..._N_00x)


Central European Towns 0.3.0 (2023-06-18) (Build 3)
----------------------------------------------------
- ADD: farm fields for the use with various house types
- ADD: house type small farm
- ADD: house type school for villages
- ADD: house type old house
- ADD: house type workshop for villages
- ADD: house type house for villages
- ADD: house type shop for villages
- ADD: house type farm
- CHANGE: farm house has now equal amount of sprites for eras 01, 02
- CHANGE: town houses now available in all town zones
- FIX: reset numbering of era from 1-6 instead of 0-5 since era definition "0" for the first historical era caused sprites to change after 1850


Central European Towns 0.2.0 (2023-06-13) (Build 2)
----------------------------------------------------
- FEATURE: road-awareness for block perimeter houses built in cities
- FEATURE: old town creation for houses built prior to 1850 (era00)
- ADD: house type church
- ADD: house type town hall
- ADD: house type farm estate
- CHANGE: house type farm house is now limited to villages and town zones 2,3 and 4, in order to create denser village cores without so many fields or gardens (not yet implemented)
- FIX: include stations into road-awareness function so that bus stops do not lead to wrong alignment


Central European Towns 0.1.0 (2023-06-11) (Build 1)
----------------------------------------------------
- First build within the new project management frame containing the elements listed below
- English language file
- Functions for town type and historical Era
- Custom concrete ground sprite
- House type farm house (including sprites, nml code and lang file entry; this info will be skipped 
- House type town houses
- House type shops and offices 1