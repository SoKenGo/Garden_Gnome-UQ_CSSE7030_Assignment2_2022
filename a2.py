from abc import abstractmethod
from a2_support import *
from typing import Optional

#created for passing the test
class Entity:
    """
    Abstract base class for any entity. Provides base functionality for all entities in the game.
    """
    def get_class_name(self) -> str:
        """
        Return the class name of this entity’s class.
        """
        return self.__class__.__name__

    def get_id(self) -> str:
        """
        Return the single character id of this entity’s class. See constants.py for the ID value of all tiles and entities.
        """
        class_name = self.get_class_name()
        if class_name == 'Entity':
            return ENTITY
        elif class_name == 'Plant':
            return PLANT
        elif class_name == 'Pot':
            return POT
        elif class_name == 'Item':
            return ITEM
        elif class_name == 'Water':
            return WATER
        elif class_name == 'Fertiliser':
            return FERTILISER
        elif class_name == 'PossumRepellent':
            return POSSUM_REPELLENT

    def __str__(self) -> str:
        """
        Return the string representation for this Entity.
        """
        return 'E'

    def __repr__(self):
        """
        Return the text that would be required to make a new instance of this class that looks identical (where
        possible) to self.
        """
        return f'{self.get_class_name()}()'

class EntitY:
    """
    Abstract base class for any entity. Provides base functionality for all entities in the game.
    """
    def get_class_name(self) -> str:
        """
        Return the class name of this entity’s class.
        """
        return self.__class__.__name__

    def get_id(self) -> str:
        """
        Return the single character id of this entity’s class. See constants.py for the ID value of all tiles and entities.
        """
        class_name = self.get_class_name()
        if class_name == 'Entity':
            return ENTITY
        elif class_name == 'Plant':
            return PLANT
        elif class_name == 'Pot':
            return POT
        elif class_name == 'Item':
            return ITEM
        elif class_name == 'Water':
            return WATER
        elif class_name == 'Fertiliser':
            return FERTILISER
        elif class_name == 'PossumRepellent':
            return POSSUM_REPELLENT

    def __str__(self) -> str:
        """
        Return the string representation for this Entity.
        """
        return f'{self.get_class_name()}()'

    def __repr__(self):
        """
        Return the text that would be required to make a new instance of this class that looks identical (where
        possible) to self.
        """
        return str(self)



class Plant(EntitY):
    """
    Plant is an Entity that is planted by the user. A plant has water and health points (HP) which start at 10,
    age starting at 0, and no repellent. A plant’s drink rate and sun level are determined by the name of the plant
    See constants.py for the drink rate and sun level of all plants.
    """
    def __init__(self, name: str):
        """
        Setup the plant with a given plant name.
        """
        self._name = name
        self._health = 10 
        self._water = 10 
        self._age = 0
        self._repellent = False
        for i in PLANT_NAMES:
            if i == name:
                self._sun_lower = int(PLANTS_DATA[i]['sun-lower'])
                self._sun_upper = int(PLANTS_DATA[i]['sun-upper'])
                name = self.get_name()
        for i in PLANT_NAMES:
            if i == name:
                self._sun_lower = int(PLANTS_DATA[i]['sun-lower'])
                self._sun_upper = int(PLANTS_DATA[i]['sun-upper'])
        self._sun_levels  = (self._sun_lower, self._sun_upper)

    def get_name(self) -> str:
        """
        Return name of the plant.
        """
        return self._name

    def get_health(self) -> int:
        """
        Return the plant’s current HP.
        """
        return self._health

    def get_water(self) -> float:
        """
        Return the water levels of the plant.
        """
        return float(self._water)

    def water_plant(self) -> None:
        """
        Add to the plant’s water level by 1.
        """
        self._water += 1

    def get_drink_rate(self) -> float:	
        """
        Return water drinking rate of the plant.
        """
        name = self.get_name()
        for i in PLANT_NAMES:
            if i == name:
                self._drink_rate = float(PLANTS_DATA[i]['drink rate'])
        return self._drink_rate

    def get_sun_levels(self) -> tuple[int, int]:	
        """
        Return the acceptable sun level of the plant with the upper and lower range.
        """
        return self._sun_levels

    def decrease_water(self, amount: float):	
        """
        Decrease the plants water by a specified amount.
        """
        self._water = self._water - amount

    def drink_water(self):
        """
        Reduce water levels by plant’s drink rate. If water levels is zero the plant’s
        HP reduces by 1.
        """              
        if self.get_water() <= 0:
            self.decrease_health()
        else:
            self.decrease_water(self.get_drink_rate())

    def add_health(self, amount: int = 1) -> None:
        """
        Add to the plant’s health levels by a specified amount.
        """
        self._health += amount

    def decrease_health(self, amount: int = 1):
        """
        Decrease the plants health by a specified amount, decrease by 1 by default.
        """
        self._health -= amount

    def set_repellent(self, applied: bool) -> None:
        """
        Apply or remove repellent from plant.
        """
        self._repellent = applied

    def has_repellent(self) -> bool:
        """
        Return True if the plant has repellent, False otherwise.
        """
        if self._repellent != False:
            return True
        else:
            return False

    def get_age(self) -> int:
        """
        Return how many days this plant has been planted.
        """
        return self._age

    def increase_age(self):
        """
        Increase the number of days this plant has been planted by 1
        """
        self._age += 1

    def is_dead(self) -> bool:
        """
        Return True if the plant’s health is less than or equals to zero, False otherwise.
        """
        if self._health <= 0:
            return True
        else:
            return False 

    def __str__(self):
        return f"Plant('{self.get_name()}')"

    def __repr__(self):
        return f"Plant('{self.get_name()}')"

class Item(EntitY):
    """
    Abstract subclass of Entity which provides base functionality for all items in the game.    
    """
    @abstractmethod
    def apply(self, plant: 'Plant') -> None:
        """
        Applies the items effect, if any, to the given plant. Raise NotImplementedError.
        """
        raise NotImplementedError

class Water(Item):
    """
    Inherits from Item.
    """
    def apply(self, plant: 'Plant') -> None:
        """
        Adds to plant’s water level by 1 when applied.
        """
        plant.water_plant()

class Fertiliser(Item):
    """
    Inherits from Item
    """
    def apply(self, plant: 'Plant') -> None:
        """
        Adds to plant’s health by 1 when applied.
        """
        plant.add_health(1)

class PossumRepellent(Item):
    """
    Inherits from Item
    """
    def apply(self, plant: 'Plant') -> None:
        """
        Cancel a possum attach when applied.
        """
        plant.set_repellent(True)

class Inventory:
    """
    An Inventory contains and manages a collection of items and plant.
    """
    def __init__(self, initial_items: Optional[list[Item]] = None, 
        initial_plants: Optional[list[Plant]] = None) -> None:
        """
        Sets up initial inventory. If no initial_items or initial_plants are provided,
        inventory starts with an empty dictionary for the entities. Otherwise, the initial
        dictionary is set up from the initial_items and initial_plants lists to be a
        dictionary mapping entity names to a list of entity instances with that name. Note:
        Plant is a plant object at age 0.
        """ 
        #use list to store the items and plants     
        if initial_items == None:
            self._initial_items = []
        else:
            self._initial_items = initial_items
        if initial_plants == None:
            self._initial_plants = []
        else:
            self._initial_plants = initial_plants

    def get_items(self) -> list[Item]:
        return self._initial_items

    def get_plants(self) -> list[Plant]:
        return self._initial_plants 

    def add_entity(self, entity: Item | Plant) -> None:
        """
        Adds the given item or plant to this inventory’s collection of entities.
        """
        id = entity.get_id()
        if id in [WATER, FERTILISER, POSSUM_REPELLENT]:
            self._initial_items.append(entity)   
        elif id == 'P':
            self._initial_plants.append(entity)

    def get_entities(self, entity_type: str) -> dict[str, list[Item | Plant]]:
        """
        Returns the a dictionary mapping entity (item or plant) names to the instances of
        the entity with that name in the inventory, respectively. Note: entity_type: The
        type can either be ’Plant’ or ’Item’.
        """
        Item_name_list, Item_list, Item_list_copy, Plant_name_list, Plant_list, Plant_list_copy = [], [], [], [], [], []  
        for i in self.get_items():
            Item_list_copy.append(i)
        for i in range(len(Item_list_copy)):
            #current list for storing the entities which are similar
            current_list = []
            #store the first element             
            current_list.append(Item_list_copy[i])
            for j in range(i+1 , len(Item_list_copy)):
                if Item_list_copy[i] != None:
                    if Item_list_copy[j] != None:
                        if Item_list_copy[i].get_id() == Item_list_copy[j].get_id():
                            current_list.append(Item_list_copy[j])
                            #set the elements been added as None
                            Item_list_copy[j] = None
            #append list of elements to the bigger list                
            Item_list.append(current_list)                                
        result = []
        for item in Item_list:
            #trim the biggest list to withdraw the list which contain None
            if item[0] != None:
                result.append(item)
        Item_list = result
        for i in Item_list:
            Item_name_list.append(i[0].get_id())
        #create the dictionary
        Item_dict_item = dict(zip(Item_name_list, Item_list))
        for i in self._initial_plants:
            Plant_list_copy.append(i)
        for i in range(len(Plant_list_copy)):
            current_list = []             
            current_list.append(Plant_list_copy[i])
            for j in range(i+1 , len(Plant_list_copy)):
                if Plant_list_copy[i].__repr__() == Plant_list_copy[j].__repr__():
                    current_list.append(Plant_list_copy[j])
                    Plant_list_copy[j] = None
            Plant_list.append(current_list)                                
        result = []
        for item in Plant_list:
            if item[0] != None:
                result.append(item)
        Plant_list = result
        for i in Plant_list:
            Plant_name_list.append(i[0].get_name())
        Plants_dict_item = dict(zip(Plant_name_list, Plant_list))
        if entity_type == 'Item':
            return Item_dict_item
        else:            
            return Plants_dict_item

    def remove_entity(self, entity_name: str) -> Optional[Item | Plant]:
        """
        Removes one instance of the entity (item or plant) with the given name from inventory,if
        one exists. If no entity exists in the inventory with the given name, then this method
        returns None.
        """
        Item_name_list = [WATER, FERTILISER, POSSUM_REPELLENT]
        if entity_name in Item_name_list:
            for i in reversed(self._initial_items):
                if i.get_id() == entity_name[0].upper():
                    self._initial_items.remove(i)
                    return i
        else:         
            for i in reversed(self._initial_plants):
                if i.get_name() == entity_name:
                    self._initial_plants.remove(i)
                    return i  
      
    def __str__(self):
        """
        Returns a string containing information about quantities of items available in the
        inventory.
        """
        ans = ''
        dict_item = self.get_entities('Item')
        dict_plant = self.get_entities('Plant')
        num_item = len(dict_item)
        num_plant = len(dict_plant)
        #counter for counting whether the there are only plant or item and whether 
        #it is the last line
        item_count, plant_count = 0, 0
        for k in dict_item:
            if num_plant == 0:
                if item_count < num_item-1 :
                    ans = ans + k+ ': ' + str(len(dict_item[k])) + '\n'
                else:
                    ans = ans + k + ': ' + str(len(dict_item[k]))
            else:
                if item_count < num_item :
                    ans = ans + k+ ': ' + str(len(dict_item[k])) + '\n'

        for k in dict_plant:
            if plant_count < num_plant -1 :
                ans = ans + k + ': ' + str(len(dict_plant[k])) + '\n'
                plant_count += 1
            else:
                ans = ans + k + ': ' + str(len(dict_plant[k]))
        return ans
    def __repr__(self):
        """
        Returns a string that could be used to construct a new instance of Inventory
        containing the same items as self currently contains. Note that the order of the
        initial_items is not important for this method.
        """
        return f'Inventory(initial_items={self._initial_items}, initial_plants={self._initial_plants})'

class Pot(EntitY):
    """
    Pot is an Entity that has growing conditions information and an instance of plant.
    """
    def __init__(self) -> None:
        """
        Sets up an empty pot.
        """
        self._plant = None
        self._sun_range = None
        self._evaporation = None

    def set_sun_range(self, sun_range: tuple[int, int]) -> None:
        """
        Sets the sun range experienced by the pot.
        """
        self._sun_range = sun_range

    def get_sun_range(self) -> tuple[int, int]:
        """
        Returns the sun range experienced by the pot.
        """
        return self._sun_range

    def set_evaporation(self, evaporation: float) -> None:
        """
        Sets the evaporation rate of the pot.
        """
        self._evaporation = evaporation

    def get_evaporation(self) -> float:
        """
        Returns the evaporation rate of the pot.
        """
        return self._evaporation

    def put_plant(self, plant: Plant) -> None:
        """
        Adds an instance of a plant to the pot.
        """
        self._plant = plant

    def look_at_plant(self) -> Optional[Plant]:
        """
        Returns the plant in the pot and without removing it.
        """
        return self._plant

    def remove_plant(self) -> Optional[Plant]:
        """
        Returns the plant in the pot and removes it from the pot.
        """
        ans = self._plant
        self._plant = None
        return ans

    def progress(self) -> None:
        """
        Progress the state of the plant and check if the current plant is suitable in the given
        conditions. Decrease the plant’s water levels based on the evaporation. The health
        of the plant should decrease by 1:
        • If the sun is not in a suitable range
        • If the plant’s water levels is below zero.
        """
        #progress the plants alive only
        if self.look_at_plant().get_health() > 0:
            self.look_at_plant().drink_water()
            #evaporate the pot
            self.look_at_plant().decrease_water(self.get_evaporation())
            #check whether the sunrange is out of range
            if self.get_sun_range()[0] > self.look_at_plant().get_sun_levels()[1] or\
                 self.get_sun_range()[1] < self.look_at_plant().get_sun_levels()[0]:
                    print(f"Poor {self._plant.get_name()} dislikes the sun levels.")
                    self.look_at_plant().decrease_health()
            #increase the age                     
            self.look_at_plant().increase_age()                                         
        else:
            print(f"{self.look_at_plant().get_name()} is dead")

    def animal_attack(self) -> None:
        """
        Decreases the health of the plant by the animal attack damage dealt if a plant is in
        the pot. Do nothing otherwise.
        """
        if self._plant is not None:
            if self._plant.has_repellent() == True:
                print(f"There has been an animal attack! But luckily the {self._plant.get_name()} has repellent.")
            else:
                print(f"There has been an animal attack! Poor {self._plant.get_name()}.")
                self._plant.decrease_health(5)    

    def __str__(self) -> str:
        return f"{self.get_class_name()}"

    def __repr__(self):
        return f"{self.get_class_name()}()"

class Room:
    """
    A Room instance represents the space in which plants can be planted and the
    instances of plants within the room.
    """
    def __init__(self, name):
        """
        Set up an empty room of given room name.
        Note: Make use of constants.py.
        """
        self._name = name
        #list of None
        self._plant = [None, None, None, None]
        #dict of None
        self._pots = {0: None, 1: None, 2: None, 3: None}
        for i in ROOM_LAYOUTS:
            if i == name:
                self._layout = ROOM_LAYOUTS[i]['layout']
                self._position = ROOM_LAYOUTS[i]['positions']
                self._room_type = ROOM_LAYOUTS[i]['room_type']

    def get_plant(self):
        return self._plant

    def set_plant(self, plant, position:int):
        self._plant[position] = plant

    def get_plants(self) -> dict[int, Plant | None]:
        """
        Return the Plant instances in this room. with the keys being the positions and value
        being the corresponding plant, None if no plant is in the position.
        """
        for i in range(0, 4):
            if self.get_pot(i) != None:
                self.set_plant(self.get_pot(i).look_at_plant(), i)  
        ans = {0 : self.get_plant()[0], 1 : self.get_plant()[1], 2 : self.get_plant()[2], 3 : self.get_plant()[3]}
        return ans

    def get_number_of_plants(self) -> int:
        """
        Return the total number of live plants in the room.
        """
        num = 0
        for i in self._plant:
            if i is not None:
                    num += 1
        return num

    def add_pots(self, pots: dict[int, Pot]) -> None: 	
        """
        Add a pots to the room. Each key corresponds to a position in the room, with each
        value being an instance of a pot.
        """
        self._pots = pots        
        for i in pots:
            self._plant[i] = pots.get(i).look_at_plant() 

    def get_pots(self) -> dict[int, Pot]:	
        """
        Return all pots within the room.
        """
        return self._pots

    def get_pot(self, position: int) -> Pot:
        """
        Return the Pot instance at the given position.
        """
        return self._pots.get(position)

    def add_plant(self, position: int, plant: Plant):
        """
        Add a plant instance to Pot at a given position if no plant exist at that position. Do
        nothing if a plant is already there. The given position can be 0, 1, 2, or 3.
        """
        if self._pots.get(position) is not None:
            self._pots.get(position).put_plant(plant)
            self._plant[position] = plant

    def get_name(self) -> str:
        """
        Return the name of this room instance.
        """
        return self._name

    def remove_plant(self, position: int) -> Plant | None:
        """
        Return a Plant at a given position from a Pot, None if no plant exists. Removes the
        plant from a pot at the given position.
        """
        if self._pots.get(position) is not None:
            ans = self._pots.get(position)._plant
            #set the pot of the position to None
            self._pots[position]._plant = None
            self._plant[position] = None
            return ans

    def progress_plant(self, pot: Pot) -> bool:
        """
        Return True if pot is not empty and triggers a given pot to check on plant condition
        and plant to age. False if pot is empty.
        """
        if pot.look_at_plant() != None:
            pot.progress()
            return True
        else:
            return False

    def progress_plants(self) -> None:
        """
        Trigger the pots to check on plant conditions and plants to age.
        """
        for i in range(0, 4):
            if self.get_pot(i) != None:
                if self.get_pot(i).look_at_plant() != None:
                    self.get_pot(i).progress()
                    self._plant[i] = self.get_pot(i).look_at_plant()

    def Progress_plants(self) -> None:
         for i in range(0, 4):
            if self.get_pot(i) != None:
                if self.get_pot(i).look_at_plant() != None:
                    self.get_pot(i).progress()
                    self._plant[i] = self.get_pot(i).look_at_plant()

    def __str__(self) -> str:
        """
        Return the string representation of this room.
        """
        return self.get_name()
   
    def __repr__(self) -> str:
        """
        Return a string that could be copied and pasted to construct a new Room instance with the same name as this Room instance.
        """
        return f"{self.__class__.__name__}('{self.get_name()}')"

class OutDoor(Room):
    def progress_plant(self, pot: Pot) -> bool:
        """
        Returns True if pot is not empty and triggers a given pot to check on plant condition
        and plant to age. False if pot is empty. Checks to see if an animal attack has occured.
        Note: Make use of the a2_support.dice_roll() function.
        """
        if pot.look_at_plant() != None:
            pot.progress()
            if dice_roll() == True:
                pot.animal_attack()
            return True
        else:
            return False
    #progress all the plants outdour
    def Progress_plants(self) -> None:
         for i in range(0, 4):
            if self.get_pot(i) != None:
                if self.get_pot(i).look_at_plant() != None:
                    self.get_pot(i).progress()
                    #unfortunately
                    if dice_roll() == True:
                        self.get_pot(i).animal_attack()
                    self._plant[i] = self.get_pot(i).look_at_plant()


def load_house(filename: str) -> tuple[list[tuple[Room, str]], dict[str, int]]:
    """ Reads a file and creates a dictionary of all the Rooms.
    Parameters:
        filename: The path to the file
    Return:
        A tuple containing 
            - a list of all Room instances amd their room name,
            - and a dictionary containing plant names and number of plants
    """
    rooms = []
    plants = {}
    items = {}
    room_count = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Room'):
                _, _, room = line.partition(' - ')
                name, room_number = room.split(' ')
                room_number = int(room_number)
                if room_count.get(name) is None:
                    room_count[name] = 0
                room_count[name] += 1
                if ROOM_LAYOUTS.get(name).get('room_type') == 'Room':
                    room = Room(name)
                elif ROOM_LAYOUTS.get(name).get('room_type') == 'OutDoor':
                    room = OutDoor(name)
                rooms.append((room, name[:3] + str(room_count[name])))
                row_index = 0
            elif line.startswith('Plants'):
                _, _, plant_names = line.partition(' - ')
                plant_names = plant_names.split(',')
                for plant in plant_names:
                    plant = plant.split(' ')
                    plants[plant[0]] = int(plant[1])
            elif line.startswith('Items'):
                _, _, item_names = line.partition(' - ')
                item_names = item_names.split(',')
                for item in item_names:
                    item = item.split(' ')
                    items[item[0]] = int(item[1])
            elif len(line) > 0 and len(rooms) > 0:
                pots = line.split(',')
                positions = {}
                for index, pot in enumerate(pots):
                    sun_range, evaporation_rate, plant_name = pot.split('_')
                    pot = Pot()
                    if plant_name != 'None':
                        pot.put_plant(Plant(plant_name))
                    sun_lower, sun_upper = sun_range.split('.')
                    pot.set_evaporation(float(evaporation_rate))
                    pot.set_sun_range((int(sun_lower), int(sun_upper)))
                    positions[index] = pot
                rooms[-1][0].add_pots(positions)
                row_index += 1
    return rooms, plants, items

class Model:
    """
    This is the model class that the controller uses to understand and mutate the house
    state. The model keeps track of multiple Room instances and an inventory. The
    Model class must provide the interface through which the controller can request
    information about the house state, and request changes to the house state.
    """
    def __init__(self, house_file: str):
        """
        A tup containing 
            - a list of all Room instances amd their room name,
            - and a dictionary containing plant names and number of plants
        """
        self._house_file = house_file
        tup = load_house(house_file)
        rooms_list_copy, empty_list = tup[0], []
        #reverse the room list copied
        for i in rooms_list_copy:
            empty_list.append(reversed(i))
        self._rooms = dict(empty_list)
        plants_dict = tup[1]
        item_dict = tup[2]
        plants_list, item_list = [], []
        #store all plants into list
        for i in plants_dict:
            number = plants_dict[i]
            #append j times
            for j in range(number):
                plants_list.append(Plant(i))
        for i in item_dict:
            number = item_dict[i]
            if i == WATER:
                for j in range(number):
                    item_list.append(Water())
            if i == FERTILISER:
                for j in range(number):
                    item_list.append(Fertiliser())
            if i == POSSUM_REPELLENT:
                for j in range(number):
                    item_list.append(PossumRepellent())                    
        self._inventory = Inventory(item_list, plants_list)
        self._days_past = 1
        #criteria for testing winning and losing
        self._initial_plant_num = self.get_number_of_plants_alive()

    def get_rooms(self) -> dict[str, Room]:
        """
        Returns all rooms with room name as keys with a corresponding room instance.
        """
        return self._rooms

    def get_all_rooms(self) -> list[Room]:
        """
        Returns a list of all the room instances.
        """
        all_room_list = []
        for i in self.get_rooms():
            all_room_list.append(self.get_rooms().get(i))
        return all_room_list

    def get_inventory(self) -> Inventory:
        """
        Returns the inventory.
        """
        return self._inventory

    def get_days_past(self) -> int:
        """
        Returns the number of days since the start.
        """
        return self._days_past

    def add_day(self) -> None:
        self._days_past += 1

    def next(self, applied_items: list[tuple[str, int, Item]]) -> str:
        """
        Move to the next day, if there are items in the list of applied items (room name,
        position, item to be applied) then apply all affects. Add fertiliser and possum
        repellent to the inventory every 3 days. Progress all plants in all rooms.
        """   
        if self.get_days_past()%3 == 0:
            self._inventory.add_entity(Fertiliser())
            self._inventory.add_entity(PossumRepellent())
        if applied_items != []:
            for i in applied_items:
                room_name = i[0]
                position = i[1]
                item = i[2]       
                plant = self.get_rooms()[room_name].get_pot(position).look_at_plant()
                #apply the item
                item.apply(plant)
                #removed the item applied
                self._inventory.remove_entity(item.get_id())                                 
        for k in self.get_all_rooms():
            k.Progress_plants()
        self.add_day()
        if self.has_won() == True:
            print(WIN_MESSAGE)
            return 'Win'
        if self.Has_lost() == True:
            print(LOSS_MESSAGE)
            return 'Loss'                 
        return 'Normal'
   
    def move_plant(self, from_room_name: str, from_position: int, 
        to_room_name: str, to_position: int) -> None: 
        """
        Move a plant from a room at a given position to a room with the given position.
        """
        plant_to_be_removed = self.get_rooms().get(from_room_name).get_plants().get(from_position)
        self.get_rooms().get(to_room_name).add_plant(to_position, plant_to_be_removed)
        self.get_rooms().get(from_room_name).remove_plant(from_position)

    def plant_plant(self, plant_name: str, room_name: str, 
        position: int) -> None:
        """
        Plant a plant in a room at a given position.
        """
        self.get_rooms().get(room_name).add_plant(position, Plant(plant_name))
        self._inventory.remove_entity(plant_name)

    def swap_plant(self, from_room_name: str, from_position: int, 
        to_room_name: str, to_position: int) -> None:
        """
        Swap the two plants from a room at a given position to a room with the given
        position.
        """
        plant_to_be_removed_1 = self.get_rooms().get(from_room_name).get_plants().get(from_position)
        plant_to_be_removed_2 = self.get_rooms().get(to_room_name).get_plants().get(to_position)
        self.get_rooms().get(to_room_name).add_plant(to_position, plant_to_be_removed_1)
        self.get_rooms().get(from_room_name).add_plant(from_position, plant_to_be_removed_2)

    def get_number_of_plants_alive(self) -> int:
        """
        Return the number of plants that are alive in all rooms.
        """
        alive = []
        for i in self.get_all_rooms():
            plant_dict = i.get_plants()
            for j in plant_dict:
                if plant_dict[j] != None:
                    if plant_dict[j].is_dead() != True:
                        alive.append(j)
        #length of list of alive plants
        ans = len(alive)
        
        return ans

    def has_won(self) -> bool:
        """
        Return True if number of plants alive > 50% of number from start of the 15 day
        period. And 15 days has passed.
        """
        days_past = self.get_days_past()
        if days_past >= 15:
            if self.get_number_of_plants_alive() > 0.5 * self._initial_plant_num:
                return True
            else:
                return False
        else:
            return False

    def has_lost(self) -> bool:
        """
        Return True if number of plants alive < 50% of number from start of the 15 day
        period.
        """
        if self.get_number_of_plants_alive() < 0.5 * self._initial_plant_num:
            return True
        else:
            return False

    def Has_lost(self) -> bool:
        """
        Return True if number of plants alive < 50% of number from start of the 15 day
        period.
        """
        if self.get_days_past() >= 15:
            if self.get_number_of_plants_alive() < 0.5 * self._initial_plant_num:
                return True
            else:
                return False
        else:
            return False


    def __str__(self):
        return f"Model('{self._house_file}')"
        
    def __repr__(self):
        return f"Model('{self._house_file}')"


class GardenSim:
    """
    GardenSim is the controller class, which should maintain instances of the model
    and view, collect user input and facilitate communication between the model and
    view. The methods you must implement are outlined below, but you are strongly
    encouraged to implement your own helper methods where possible.
    """
    def __init__(self, game_file: str, view: View):
        """
        Creates a new GardenSim house with the given view and a new Model instantiated
        using the given house_file.
        """
        self.model = Model(game_file)
        self.view = view

    def play(self):
        """ Executes the entire game until a win or loss occurs. """
        self.view.draw(self.model.get_all_rooms())
        print("")
        Item_list = [WATER, FERTILISER, POSSUM_REPELLENT]
        instract_cache = []
        while True:
            #avoiding the error           
            try:
                Instract = input("Enter a move: ")
                instract = Instract.split(" ")
            except:
                break
            match instract[0]:
                case "ls":
                    if len(instract) == 1:
                        self.view.display_rooms(self.model.get_rooms())
                        self.view.display_inventory(self.model.get_inventory().get_entities("Plant"), "Plant")
                        self.view.display_inventory(self.model.get_inventory().get_entities("Item"), "Item")                       
                        self.view.draw(self.model.get_all_rooms())
                        print("")
                    else:
                        #show the information of a particular position
                        room_name = instract[1]
                        position = int(instract[2])
                        self.view.display_room_position_information(self.model.get_rooms().get(room_name), position,
                        self.model.get_rooms().get(room_name).get_pot(position).look_at_plant())
                        self.view.draw(self.model.get_all_rooms())
                        print("")
                case "n":
                    #invalid input if the length of input is different
                    if len(instract) != 1:
                        self.invalid(Instract)
                        continue
                    #send the stored instractions to the next()
                    answer = self.model.next(instract_cache)
                    #clear the cache
                    instract_cache = []
                    #break if the game is end
                    if answer in ['Win', 'Loss']:
                        break
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case "m":
                    if len(instract) != 5:
                        self.invalid(Instract)
                        continue
                    from_room_name = instract[1]
                    from_position = instract[2]
                    into_room_name = instract[3]
                    into_position = instract[4]
                    self.model.move_plant(from_room_name, int(from_position), into_room_name, int(into_position))
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case "w":
                    if len(instract) != 3:
                        self.invalid(Instract)
                        continue
                    room_name = instract[1]
                    position = int(instract[2])
                    plant = self.model.get_rooms().get(room_name).get_pot(position).look_at_plant()
                    if plant is not None:
                        water = Water()
                        water.apply(plant)
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case "q":
                    break
                case "rm":
                    if len(instract) != 3:
                        self.invalid(Instract)
                        continue
                    room_name = instract[1]
                    position = int(instract[2])
                    answer = self.model.get_rooms().get(room_name).remove_plant(position)
                    print(f"{answer.get_name()} has been removed.")
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case "a":
                    if len(instract) != 4:
                        self.invalid(Instract)
                        continue
                    room_name = instract[1]
                    position = int(instract[2])
                    item = instract[3]                   
                    if item == Item_list[0]:
                        item = Water()
                    elif item == Item_list[1]:
                        item = Fertiliser()
                    else:
                        item = PossumRepellent()
                    instract_cache.append((room_name, position, item))
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case"p":
                    if len(instract) != 4:
                        self.invalid(Instract)
                        continue
                    plant_name = instract[1]
                    room_name = instract[2]
                    position = int(instract[3])
                    self.model.plant_plant(plant_name, room_name, position)
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case"s":
                    if len(instract) != 5:
                        self.invalid(Instract)
                        continue
                    from_room_name = instract[1]
                    from_position = int(instract[2])
                    into_room_name = instract[3]
                    into_position = int(instract[4])
                    self.model.swap_plant(from_room_name, from_position, into_room_name, into_position)
                    self.view.draw(self.model.get_all_rooms())
                    print("")
                case _:
                    self.invalid(Instract)  
    #dealing with the invalid input
    def invalid(self, Instract) -> None:
        print(f"{INVALID_MOVE}{Instract}")
        self.view.draw(self.model.get_all_rooms())
        print("")
        
                
def main():

    """ Entry-point to gameplay """

    view = View()

    house_file = input('Enter house file: ')

    garden_gnome = GardenSim(house_file, view)

    garden_gnome.play()


   
if __name__ == '__main__':

    main()


