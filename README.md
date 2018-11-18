# Min Gen Tree

This is a implementation of minimum generator tree algorithm.

### in terminal
First load a json file typing open {weight_1 vertex1_1 vertex2_1 weight_2 vertex1_2 vertex2_2}. Then type start execute the algorithm. Type help for more instructions.

json file structure:
{
    "node1":{"next_node1":weight1, "next_node2":weight2}
}

The json file must be redundant, example:

{
    "1":{"2":1,"3":3},
    "2":{"1":1,"3":1,"4":2,"5":3},
    "3":{"1":3,"2":1,"5":2},
    "4":{"2":2,"5":-3,"6":3},
    "5":{"2":3,"3":2,"4":-3,"6":2},
    "6":{"4":3,"5":2}
}