from campus_graph import CampusGraph as cg
from node import Node

# TODO: Have building node, then closest nodes (distance 0) be the entrances


# Create a graph
G = cg()
node_list = []

building_list = [
    {"name": "northern_neck", "node_type": "building"},

    {"name": "hampton_roads", "node_type": "building"},

    {"name": "commonwealth", "node_type": "building"},

    {"name": "eastern_shore", "node_type": "building"},

    {"name": "dominion", "node_type": "building"},

    {"name": "blue_ridge", "node_type": "building"},
    {"name": "sandbridge", "node_type": "building"},

    {"name": "piedmont", "node_type": "building"},
    {"name": "tidewater", "node_type": "building"},

    {"name": "grayson", "node_type": "building"},
    {"name": "franklin", "node_type": "building"},

    {"name": "amherst", "node_type": "building"},
    {"name": "brunswick", "node_type": "building"},

    {"name": "hanover", "node_type": "building"},

    # parent_building = set(["essex", "carroll", "dickenson"])
    {"name": "essex", "node_type": "building"},
    {"name": "carroll", "node_type": "building"},
    {"name": "dickenson", "node_type": "building"},

    {"name": "southside", "node_type": "building"},
]

# Add building nodes to the graph
# for building in building_list:
#     new_node = Node(name=building["name"], node_type=building["node_type"])
#     node_list.append(new_node)
#     G.add_node(new_node)



# Add walking point nodes to the graph
sidewalk_list = [
    {"name": "X1", "node_type": "sidewalk"},
    {"name": "X2", "node_type": "sidewalk"},
    {"name": "X3", "node_type": "sidewalk"},
    {"name": "X4", "node_type": "sidewalk"},
    {"name": "X5", "node_type": "sidewalk"},
    {"name": "X6", "node_type": "sidewalk"},
    {"name": "X7", "node_type": "sidewalk"},
    {"name": "X8", "node_type": "sidewalk"},
    {"name": "X9", "node_type": "sidewalk"},
    {"name": "X10", "node_type": "sidewalk"},
    {"name": "X11", "node_type": "sidewalk"},
    {"name": "X12", "node_type": "sidewalk"},
    {"name": "X13", "node_type": "sidewalk"},
    {"name": "X14", "node_type": "sidewalk"},
    {"name": "X15", "node_type": "sidewalk"},
    {"name": "X16", "node_type": "sidewalk"},
    {"name": "X17", "node_type": "sidewalk"},
    {"name": "X18", "node_type": "sidewalk"},
    {"name": "X19", "node_type": "sidewalk"},
    {"name": "X20", "node_type": "sidewalk"},
    {"name": "X21", "node_type": "sidewalk"},
    {"name": "X22", "node_type": "sidewalk"},
    {"name": "X23", "node_type": "sidewalk"},
    {"name": "X24", "node_type": "sidewalk"},
    {"name": "X25", "node_type": "sidewalk"},
    {"name": "X26", "node_type": "sidewalk"},
    {"name": "X27", "node_type": "sidewalk"},
    {"name": "X28", "node_type": "sidewalk"},
    {"name": "X29", "node_type": "sidewalk"},
    {"name": "X30", "node_type": "sidewalk"},
    {"name": "X31", "node_type": "sidewalk"},
    {"name": "X32", "node_type": "sidewalk"},
    {"name": "X33", "node_type": "sidewalk"},
    {"name": "X34", "node_type": "sidewalk"},
    {"name": "X35", "node_type": "sidewalk"},
    {"name": "X36", "node_type": "sidewalk"},
    {"name": "X37", "node_type": "sidewalk"},
    {"name": "X38", "node_type": "sidewalk"},
    {"name": "X39", "node_type": "sidewalk"},
    {"name": "X40", "node_type": "sidewalk"},
    {"name": "X41", "node_type": "sidewalk"},
    {"name": "X42", "node_type": "sidewalk"},
    {"name": "X43", "node_type": "sidewalk"},
    {"name": "X44", "node_type": "sidewalk"},
    {"name": "X45", "node_type": "sidewalk"},
    {"name": "X46", "node_type": "sidewalk"},
    {"name": "X47", "node_type": "sidewalk"},
    {"name": "X48", "node_type": "sidewalk"},
    {"name": "X49", "node_type": "sidewalk"},
    {"name": "X50", "node_type": "sidewalk"},
    {"name": "X51", "node_type": "sidewalk"},
    {"name": "X52", "node_type": "sidewalk"},
    {"name": "X53", "node_type": "sidewalk"},
    {"name": "X54", "node_type": "sidewalk"},
    {"name": "X55", "node_type": "sidewalk"},
    {"name": "X56", "node_type": "sidewalk"},
]



for sidewalk in sidewalk_list:
    new_node = Node(name=sidewalk["name"], node_type=sidewalk["node_type"])
    node_list.append(new_node)
    G.add_node(new_node)

building_entrance_list = [
    {"name": "amherst_1", "node_type": "building_entrance", "parent_building": {"amherst", "brunswick"}},
    {"name": "amherst_2", "node_type": "building_entrance", "parent_building": {"amherst", "brunswick"}},

    {"name": "blue_ridge_1", "node_type": "building_entrance", "parent_building": {"blue_ridge", "sandbridge"}},
    {"name": "blue_ridge_2", "node_type": "building_entrance", "parent_building": {"blue_ridge", "sandbridge"}},
    {"name": "blue_ridge_3", "node_type": "building_entrance", "parent_building": {"blue_ridge", "sandbridge"}},

    {"name": "brunswick_1", "node_type": "building_entrance", "parent_building": {"amherst", "brunswick"}},
    {"name": "brunswick_2", "node_type": "building_entrance", "parent_building": {"amherst", "brunswick"}},

    {"name": "carroll_1", "node_type": "building_entrance", "parent_building": {"essex", "carroll", "dickenson"}},

    {"name": "commonwealth_1", "node_type": "building_entrance", "parent_building": {"commonwealth"}},
    {"name": "commonwealth_2", "node_type": "building_entrance", "parent_building": {"commonwealth"}},
    {"name": "commonwealth_3", "node_type": "building_entrance", "parent_building": {"commonwealth"}},

    {"name": "dickenson_1", "node_type": "building_entrance", "parent_building": {"essex", "carroll", "dickenson"}},
    {"name": "dickenson_2", "node_type": "building_entrance", "parent_building": {"essex", "carroll", "dickenson"}},

    {"name": "dominion_1", "node_type": "building_entrance", "parent_building": {"dominion"}},
    {"name": "dominion_2", "node_type": "building_entrance", "parent_building": {"dominion"}},
    {"name": "dominion_3", "node_type": "building_entrance", "parent_building": {"dominion"}},

    {"name": "eastern_shore_1", "node_type": "building_entrance", "parent_building": {"eastern_shore"}},
    {"name": "eastern_shore_2", "node_type": "building_entrance", "parent_building": {"eastern_shore"}},
    {"name": "eastern_shore_3", "node_type": "building_entrance", "parent_building": {"eastern_shore"}},


    {"name": "essex_1", "node_type": "building_entrance", "parent_building": {"essex", "carroll", "dickenson"}},

    {"name": "franklin_1", "node_type": "building_entrance", "parent_building": {"franklin", "grayson"}},
    {"name": "grayson_1", "node_type": "building_entrance", "parent_building": {"franklin", "grayson"}},
    {"name": "grayson_2", "node_type": "building_entrance", "parent_building": {"franklin", "grayson"}},

    {"name": "hampton_roads_1", "node_type": "building_entrance", "parent_building": {"hampton_roads"}},
    {"name": "hampton_roads_2", "node_type": "building_entrance", "parent_building": {"hampton_roads"}},
    {"name": "hampton_roads_3", "node_type": "building_entrance", "parent_building": {"hampton_roads"}},

    {"name": "hanover_1", "node_type": "building_entrance", "parent_building": {"hanover"}},
    {"name": "hanover_2", "node_type": "building_entrance", "parent_building": {"hanover"}},

    {"name": "northern_neck_1", "node_type": "building_entrance", "parent_building": {"northern_neck"}},
    {"name": "northern_neck_2", "node_type": "building_entrance", "parent_building": {"northern_neck"}},
    {"name": "northern_neck_3", "node_type": "building_entrance", "parent_building": {"northern_neck"}},
    {"name": "northern_neck_4", "node_type": "building_entrance", "parent_building": {"northern_neck"}},
    {"name": "northern_neck_5", "node_type": "building_entrance", "parent_building": {"northern_neck"}},

    {"name": "piedmont_1", "node_type": "building_entrance", "parent_building": {"piedmont", "tidewater"}},
    {"name": "piedmont_2", "node_type": "building_entrance", "parent_building": {"piedmont", "tidewater"}},

    {"name": "sandbridge_1", "node_type": "building_entrance", "parent_building": {"blue_ridge", "sandbridge"}},
    {"name": "sandbridge_2", "node_type": "building_entrance", "parent_building": {"blue_ridge", "sandbridge"}},

    {"name": "southside_1", "node_type": "building_entrance", "parent_building": {"southside"}},

    {"name": "tidewater_1", "node_type": "building_entrance", "parent_building": {"piedmont", "tidewater"}},
    {"name": "tidewater_2", "node_type": "building_entrance", "parent_building": {"piedmont", "tidewater"}},
]


for building_entrance in building_entrance_list:
    new_node = Node(name=building_entrance["name"], node_type=building_entrance["node_type"], parent_building=building_entrance["parent_building"])
    node_list.append(new_node)
    G.add_node(new_node)

# SIDEWALK NODES

edges_sidewalk = [
    ("X1", "X2", 120),
    ("X1", "X5", 350),
    ("X1", "X6", 170),

    ("X2", "X3", 125),
    ("X2", "X6", 112),

    ("X3", "X4", 74),
    ("X3", "X6", 174),

    ("X4", "X8", 150),
    ("X4", "X15", 833),

    ("X5", "X10", 150),
    ("X5", "X25", 200),

    ("X6", "X7", 56),

    ("X7", "X9", 10),
    ("X7", "X10", 250),

    ("X8", "X11", 46),
    ("X8", "X12", 35),

    ("X9", "X13", 49),
    ("X9", "X14", 46),

    ("X10", "X18", 75),

    ("X11", "X12", 66),
    ("X11", "X19", 120),

    ("X12", "X16", 98),

    ("X13", "X16", 120),
    ("X13", "X14", 66),

    ("X14", "X17", 69),

    ("X15", "X20", 109),

    ("X16", "X22", 89),

    ("X17", "X18", 130),
    ("X17", "X23", 95),

    ("X18", "X28", 260),

    ("X19", "X20", 75),
    ("X19", "X24", 100),

    ("X20", "X26", 109),

    ("X21", "X22", 85),
    ("X21", "X24", 210),
    ("X21", "X36", 270),

    ("X22", "X27", 180),

    ("X23", "X27", 140),
    ("X23", "X32", 190),

    ("X24", "X26", 10),

    ("X25", "X28", 100),

    ("X26", "X30", 95),

    ("X27", "X31", 79),

    ("X29", "X30", 36),
    ("X29", "X33", 59),

    ("X30", "X35", 62),

    ("X31", "X32", 49),
    ("X31", "X34", 36),

    ("X32", "X34", 33),

    ("X33", "X35", 36),

    ("X34", "X36", 170),
    ("X34", "X40", 140),

    ("X35", "X37", 30),

    ("X36", "X39", 230),
    ("X36", "X50", 350),

    ("X37", "X38", 59),

    ("X38", "X39", 23),

    ("X39", "X46", 110),


    ("X40", "X41", 210),
    ("X40", "X43", 75),

    ("X41", "X44", 43),

    ("X42", "X46", 59),
    ("X42", "X47", 43),

    ("X43", "X45", 23),

    ("X45", "X50", 140),


    ("X46", "X48", 43),

    ("X47", "X48", 56),

    ("X48", "X49", 69),

    ("X49", "X54", 83),

    ("X50", "X51", 30),

    ("X51", "X52", 13),
    ("X51", "X53", 16),

    ("X52", "X56", 205),

    ("X53", "X55", 170),

    ("X54", "X55", 75),

]

for edge in edges_sidewalk:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)

# NORTHERN NECK

edges_northern_neck = [
    ("northern_neck_5", "X8", 47),
    ("northern_neck_5", "X11", 27),
    ("northern_neck_3", "X20", 60),
    ("northern_neck_3", "X19", 50),
    ("northern_neck_1", "X15", 43),
    ("northern_neck_2", "X15", 34),
]

for edge in edges_northern_neck:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# HAMPTON ROADS

edges_hampton_roads = [
    ("hampton_roads_2", "X3", 190),
    ("hampton_roads_1", "X8", 49),
    ("hampton_roads_2", "X7", 35),
    ("hampton_roads_2", "X2", 130),
    ("hampton_roads_2", "X1", 190),
    ("hampton_roads_3", "X5", 280),
    ("hampton_roads_1", "X4", 135)
]


for edge in edges_hampton_roads:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)

# COMMONWEALTH

edges_commonwealth = [
    ("commonwealth_1", "X19", 28),
    ("commonwealth_1", "X24", 104),
    ("commonwealth_2", "X21", 40),
    ("commonwealth_3", "X22", 21),
    ("commonwealth_3", "X16", 95),
    ("commonwealth_2", "blue_ridge_3", 70),
    ("commonwealth_1", "blue_ridge_1", 127)
]

for edge in edges_commonwealth:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# EASTERN SHORE

edges_eastern_shore = [
    ("eastern_shore_1", "X18", 70),
    ("eastern_shore_3", "X25", 66),
    ("eastern_shore_2", "X28", 58),
    ("eastern_shore_2", "X5", 209)
]

for edge in edges_eastern_shore:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)

# BLUE RIDGE, NOTE: BR5 = blue_ridge_3

edges_blue_ridge = [
    ("blue_ridge_1", "X24", 40),
    ("blue_ridge_3", "X21", 72),
    ("blue_ridge_2", "X29", 37),
    ("blue_ridge_3", "dominion_1", 121)
]

for edge in edges_blue_ridge:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# SANDBRIDGE, NOTE: blue_ridge_3 = sandbridge_2, blue_ridge_4 = sandbridge_1

edges_sandbridge = [
    ("sandbridge_2", "X33", 71),
    ("sandbridge_2", "X37", 78),
    ("sandbridge_1", "X38", 33),
    ("sandbridge_1", "X39", 35),
    ("sandbridge_1", "X36", 210),
    ("sandbridge_2", "blue_ridge_2", 87),
    ("sandbridge_1", "piedmont_1", 70)
]

for edge in edges_sandbridge:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# DOMINION

edges_dominion = [
    ("dominion_1", "X22", 45),
    ("dominion_2", "X27", 69),
    ("dominion_3", "X36", 98),
    ("dominion_3", "X34", 74),
    ("dominion_3", "grayson_2", 78)
]

for edge in edges_dominion:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# GRAYSON

edges_grayson = [
    ("grayson_1", "X40", 102),
    ("grayson_1", "X45", 101),
    ("grayson_2", "X34", 76),
]

for edge in edges_grayson:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)



# FRANKLIN, NOTE: grayson_1 == franklin_2 (same building)

edges_franklin = [
    ("franklin_1", "X45", 125),
    ("franklin_1", "tidewater_2", 93),
    ("franklin_1", "X50", 93)
]

for edge in edges_franklin:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# PIEDMONT

edges_piedmont = [
    ("piedmont_1", "X39", 69),
    ("piedmont_2", "X42", 32),
    ("piedmont_2", "tidewater_1", 42),
]

for edge in edges_piedmont:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# TIDEWATER

edges_tidewater = [
    ("tidewater_1", "X47", 36),
    ("tidewater_2", "X36", 242),
    ("tidewater_2", "X50", 157)
]

for edge in edges_tidewater:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# SOUTHSIDE

edges_southside = [
    ("southside_1", "X55", 51),
    ("southside_1", "X53", 128),
]

for edge in edges_southside:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# AMHERST, NOTE: amherst_2 == brunswick_1 (same building)

edges_amherst = [
    ("amherst_1", "X32", 41),
]

for edge in edges_amherst:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# BRUNSWICK

edges_brunswick = [
    ("brunswick_1", "X40", 110),
    ("brunswick_2", "X41", 64),
]

for edge in edges_brunswick:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# HANOVER

edges_hanover = [
    ("hanover_1", "X43", 5),
    ("hanover_2", "X40", 75),
]

for edge in edges_hanover:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# ESSEX

edges_essex = [
    ("essex_1", "X50", 77),
    ("essex_1", "X45", 101),
    ("essex_1", "franklin_1", 92),
]

for edge in edges_essex:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# DICKENSON

edges_dickenson = [
    ("dickenson_1", "X45", 147),
    ("dickenson_2", "X44", 192),
]

for edge in edges_dickenson:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


# CARROLL

edges_carroll = [
    ("carroll_1", "X44", 15),
]

for edge in edges_carroll:
    source = G.get_node(edge[0])
    destination = G.get_node(edge[1])
    weight = edge[2]
    G.add_edge(source, destination, weight)


start = G.get_node("eastern_shore_3")
end = G.get_node("piedmont_1")
print(G.dijkstra(start, end))