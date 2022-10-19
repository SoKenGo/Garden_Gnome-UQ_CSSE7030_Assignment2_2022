ROOM_ROW = 7

ROOM_COL = 4

ENTITY = 'E'

PLANT = 'P'

POT = 'U'

EMPTY = ' '

SEPARATOR = '#'

ITEM = 'I'

WATER = 'W'

FERTILISER = 'F'

POSSUM_REPELLENT = 'R'

ANIMAL_ATTACK_DAMAGE = 5

BALCONY_WALLS = {(1,0): '-', (2,0): '|', (3,0): '-',(3,1): '-', (4,1): '|',(5,1): '-',(5,2): '-', (6,2): '|',(0,0): POT, (2,1): POT, (4,2): POT, (6,3): POT}
BEDROOM_WALLS  = {(4,0): '-',(4,1): '-',(4,2): '-',(4,3): '-',(5,0): '|',(5,3): '|',(6,0): '|',(6,3): '|',(3,0): POT, (3,1): POT, (3,2): POT,(3,3): POT}
GREENHOUSE_WALLS  = {(1,0): '/',(4,0): '-',(0,1): '/',(5,1): '-',(0,2): chr(92),(5,2): '-',(1,3):chr(92),(4,3): '-',(5,0): '|',(5,3): '|',(6,0): '|',(6,3): '|',(6,1):'|',(6,2):'|',(3,0): POT, (4,1): POT, (4,2): POT,(3,3): POT}
LIVING_WALLS  = {(2,1):'.',(2,2):'.',(3,1):'_',(3,2):'_',(1,0): '-',(1,1):'-',(1,2):'-',(1,3):'-',(2,0):'|',(2,3):'|',(3,0):'|',(3,3):'|',(4,0):'-',(4,1):'-',(4,2):'-',(4,3):'-',(5,1):'|',(5,2):'|',(6,0):'|',(6,1):'=',(6,2):'=',(6,3):'|',(0,0): POT, (0,1): POT,(0,2): POT,(0,3):POT}
TOILET_WALLS = {(2,0):'-',(2,1):'|', (3,1):'|', (4,0):chr(39), (5,0):'.', (4,1):'-', (4,2):'-', (5,3):chr(41), (6,1):chr(41), (6,2):chr(40),(1,0):POT,(1,1):POT,(3,2):POT,(6,3):POT}
PAUL_OFFICE_WALLS = {(3,0):'-',(3,1):'-',(3,2):'-',(3,3):'-',(4,3):'/',(4,0):chr(92), (5,1):'-',(5,2):'-',(6,1):'H',(6,2):'H',(2,0): POT,(2,1): POT, (2,2): POT,(2,3): POT}

ROOM_LAYOUTS = {
    'Balcony': {
        'layout': BALCONY_WALLS,
        'positions': {0: (0,0), 1: (2,1), 2: (4,2), 3: (6,3)},
        'room_type': 'OutDoor'
    },
    'Bedroom': {
        'layout': BEDROOM_WALLS,
        'positions': {0: (3,0), 1: (3,1), 2: (3,2), 3: (3,3)},
        'room_type': 'Room'
    },
    'Greenhouse': {
        'layout': GREENHOUSE_WALLS,
        'positions': {0: (3,0), 1: (4,1), 2: (4,2), 3: (3,3)},
        'room_type': 'OutDoor'
    },
    'Living': {
        'layout': LIVING_WALLS,
        'positions': {0: (0,0), 1: (0,1), 2: (0,2), 3: (0,3)},
        'room_type': 'Room'
    },
    'Toilet': {
        'layout': TOILET_WALLS,
        'positions': {0: (1,0), 1: (1,1), 2: (3,2), 3: (6,3)},
        'room_type': 'Room'
    },
    'Paul_Office': {
        'layout': PAUL_OFFICE_WALLS,
        'positions': {0: (2,0), 1: (2,1), 2: (2,2), 3: (2,3)},
        'room_type': 'Room'
    }
}

PLANTS_DATA = {
    'Rebutia': {
        'drink rate': 0.1,
        'sun-lower': 6,
        'sun-upper': 10,
    },
    'Cereus': {
        'drink rate': 0.1,
        'sun-lower': 7,
        'sun-upper': 10,
    },
    'Disocactus': {
        'drink rate': 0.3,
        'sun-lower': 6,
        'sun-upper': 10,
    },
    'BridgesiiMonstrose': {
        'drink rate': 0.5,
        'sun-lower': 3,
        'sun-upper': 6,
    },
    'SnakePlant': {
        'drink rate': 0.6,
        'sun-lower': 4,
        'sun-upper': 6,
    },
    'PeaceLily': {
        'drink rate': 0.6,
        'sun-lower': 5,
        'sun-upper': 8,
    },
    'JadePlant': {
        'drink rate': 0.7,
        'sun-lower': 4,
        'sun-upper': 6,
    },
    'Monstera': {
        'drink rate': 0.8,
        'sun-lower': 4,
        'sun-upper': 7,
    },
    'FiddleLeafFig': {
        'drink rate': 0.8,
        'sun-lower': 5,
        'sun-upper': 8,
    },
    'Enoki': {
        'drink rate': 1,
        'sun-lower': 1,
        'sun-upper': 3,
    },
    'KingOyster': {
        'drink rate': 1,
        'sun-lower': 1,
        'sun-upper': 2,
    },
    'LionsManeMushroom': {
        'drink rate': 1,
        'sun-lower': 1,
        'sun-upper': 2,
    }
}

PLANT_NAMES =  list(PLANTS_DATA)

WIN_MESSAGE = 'Well done for keeping more than half the plants alive.'

LOSS_MESSAGE = 'You have managed to kill off most of the plants.'

INVALID_MOVE = 'move not found: '