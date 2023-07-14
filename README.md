# Central European Towns (CET)

![Photo credit: dant](doc/cet_collage_721x400.png)

An OpenTTD full houses replacement set that adds house types and sprites in Central European (Austrian, German, Swiss) style to the game.

In addition, CET introduces three town types: Village, Town, and City. Each in-game town will progress through these stages, thereby changing its look and structure.


## Contributors

Graphics by Chataigne, Fraenklie and dant (super_dan). 

Code by dant (super_dan).

Thanks to Andythenorth for his templating tutorial which helped very much in organising the code.


## Main Features

### Town Types
CET aims to simulate the architectural and structural features of real Central European settlements. To achieve this, the set introduces three town types based on their population: 

| **Town Type** | **Population**     |
|:-------------:|:-------------------|
| Village       | 0 – 1,000          |
| Town          | 1,000 – 10,000     |
| City          | > 10,000           |

In a standard, randomly generated game all in-game towns will most likely be villages. The in-game designation of a town as a city has no effect on this progression, apart from possibly elevating a town into the 'Town' type right at the start of the game.


### Features of The Town Types
The three town types regulate what house types can be built in a town and where (in which town zones).

* **Villages** are small rural or suburban settlements. In their centre, churches, schools or inns can appear.
* **Towns** build larger houses like shops and offices in their centre. Small residential houses move to the outer town zones. Towns build a town hall, and, among other special buildings, one or more larger town churches.
* **Cities** have block perimeter development throughout their innermost town zone. They build a city hall and cathedrals, as well as city parks and possibly business districts made up of large office buildings.


### Historical Eras
The set introduces six historical eras to help changing the look of in-game towns based on real architectural history. Villages, for example, in the late game slowly change from being dominated by farms into residential suburbs.

The historical eras are defined as follows:
* 1700 – 1849: Era 01
* 1850 – 1919: Era 02
* 1920 – 1949: Era 03
* 1950 – 1979: Era 04
* 1980 – 2009: Era 05
* 2010 – 9999: Era 06


### Old Town Districts and Historicist Rings
When starting before 1920, towns will form an old town district and a ring of historicist (late 19th century historism-inspired) houses around it.

* All Town and City houses built before 1850 (Era 01) are protected if they are within a radius of three tiles of a town hall, church or town church. They form an old town district.
* From 1850 onwards, Cities build wall-to-wall block perimeter houses in the innermost town zone. The ones built up to 1919 (in Era 02) become protected after that year within a radius of three tiles around the old town district.
* If the houses that enable protection (town hall, churches, town churches) are demolished by the player, the old town district and the historicist ring disappear unless these house types are rebuilt close-by.
* If a Village becomes a Town only after 1919, no old town district or historicist ring appears. 
* A game with a start year later than 1919 will see no old town districts either.


### City Parks
In the town type City larger park areas can be build in multiple locations.

* The first couple of city park tiles appear randomly. 
* Consecutive park tiles are exclusively built next to others, so that larger park areas form automatically.
* City park tiles are protected from auto-removal by the game.
* The spread of these areas is limited only by the road network. Thus, if players want to 'grow' a city park, they can adjust the roads to make for bigger spaces in between them.


### Conditions for Certain House Types
Some house types have special (proximity) conditions for them to be built.

* Hotels and grand hotels (multi-tile hotels) need infrastructure or special house types (city hall, cathedral, city park) to be built. They appear only when at least three station tiles or one tile of a special house type are present in a radius of three tiles around their building tile.
* Office buildings and skyscrapers need a higher station density. They, too, check for the presence of at least three station tiles in a radius of three tiles around their building tile.


## Code Reference

All code is thoroughly commented. For better handling, the main nml file has been split into pnml files for each house type, the header, and the set's functions. The main nml file is compiled by the help of the 'makenml' python script. All data is provided in /src/ (https://github.com/danttt/Central-European-Towns).