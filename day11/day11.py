"""day11.py
"""
from itertools import combinations, chain
import copy


data = '''
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
'''.strip().splitlines()

HG = 'hydrogen generator'
HM = 'hydrogen-compatible microchip'
LG = 'lithium generator'
LM = 'lithium-compatible microchip'
TG = 'thulium generator'
TM = 'thulium-compatible microchip'
PLG = 'plutonium generator'
PLM = 'plutonium-compatible microchip'
SG = 'strontium generator'
SM = 'strontium-compatible microchip'
PRG = 'promethium generator'
PRM = 'promethium-compatible microchip'
RG = 'ruthenium generator'
RM = 'ruthenium-compatible microchip'
EG = 'elerium generator'
EM = 'elerium-compatible microchip'
DG = 'dilithium generator'
DM = 'dilithium-compatible microchip'
E = 'elevator'

OBJECTS = {
    HG: 'HG',
    HM: 'HM',
    LG: 'LG',
    LM: 'LM',
    TG: 'TG',
    TM: 'TM',
    PLG: 'PLG',
    PLM: 'PLM',
    SG: 'SG',
    SM: 'SM',
    PRG: 'PRG',
    PRM: 'PRM',
    RG: 'RG',
    RM: 'RM',
    EG: 'EG',
    EM: 'EM',
    DG: 'DG',
    DM: 'DM',
    E: 'E'
}
FLOORS = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}


class Building:
    def __init__(self, data):
        self.floors = {}
        self.elevator = 1
        self.process(data)
        self.all_objects = self.get_all_objects()
        self.found_states = {}

    def hash_state(self, floors, elevator):
        return tuple(list(((x[0], tuple(x[1])) for x in floors.items())) + [elevator])

    def process(self, data):
        for line in data:
            for key, num in FLOORS.items():
                if key in line:
                    floor = num
                    break
            for obj, v in OBJECTS.items():
                if obj in line:
                    self.floors[floor] = self.floors.get(floor, []) + [v]

    def get_all_objects(self):
        all_objects = []
        for l in self.floors.values():
            all_objects += l
        all_objects.sort()
        return all_objects

    def get_least_steps(self, floors=None, elevator=None, prev=None):
        floors = self.floors if floors is None else floors
        elevator = self.elevator if elevator is None else elevator
        prev = set() if prev is None else set(prev)
        lowest = float('inf')
        for floor in floors:
            floors[floor].sort()
        q = [(floors, elevator, prev)]
        while q:
            floors, elevator, prev = q.pop(0)
            floors = copy.deepcopy(floors)
            # print(self.draw(floors, elevator))
            # input()
            prev = set(prev)
            state = self.hash_state(floors, elevator)
            prev.add(state)
            if len(prev) < self.found_states.get(state, float('inf')):
                self.found_states[state] = len(prev)
                if len(floors.get(4, [])) == len(self.all_objects):
                    lowest = len(prev) - 1
                    print(f'Found end state in {lowest} steps.')
                    return lowest
                else:
                    items = floors.get(elevator, [])
                    for comb in chain(combinations(items, 2), combinations(items, 1)):
                        comb = list(comb)
                        for nelevator in (elevator + 1, elevator - 1):
                            if nelevator > 0 and nelevator < 5:
                                nfloors = copy.deepcopy(floors)
                                for item in comb:
                                    itemindex = nfloors[elevator].index(item)
                                    del nfloors[elevator][itemindex]
                                nfloors[nelevator] = nfloors.get(nelevator, []) + comb
                                if self.is_allowed(nfloors):
                                    nfloors[nelevator].sort()
                                    q.append((nfloors, nelevator, prev))
            else:
                continue

    def get_active(self, items):
        found = set()
        active = []
        for item in items:
            item = item[:-1]
            if item in found:
                active.append(item)
            else:
                found.add(item)
        return active

    def has_generator(self, items):
        for item in items:
            if item[-1] == 'G':
                return True
        return False

    def is_allowed(self, floors):
        for floor, items in floors.items():
            active = self.get_active(items)
            if self.has_generator(items):
                for item in items:
                    if item[-1] == 'M' and item[:-1] not in active:
                        return False
        return True

    def draw(self, floors=None, elevator=None):
        floors = self.floors if floors is None else floors
        elevator = self.elevator if elevator is None else elevator
        floor = 4
        all_floors = []
        padding = 4
        out = []
        while floor > 0:
            floor_diagram = [x if x in floors.get(floor, []) else '.' for x in self.all_objects]
            floor_diagram = [f'F{str(floor)}'.rjust(padding, " "), '.'.rjust(padding, " ")] + [f'{x.rjust(padding, " ")}' for x in floor_diagram]
            if floor == elevator:
                floor_diagram[1] = 'E'.rjust(padding, ' ')
            out.append(''.join(floor_diagram))
            floor -= 1
        return '\n'.join(out)


b = Building(data)
lowest = b.get_least_steps(b.floors, b.elevator)
print(f'Part 1: {lowest}')

# every time we add a gen, microchip pair it takes 12 more steps
print(f'Part 2: {lowest + 24}')

