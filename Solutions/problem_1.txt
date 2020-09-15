Give each node within the directed graph a weight. This weight is dependent on the distance from the first node.

For example, A would have a weight of 0, B would have a weight of 1 (1 distance unit away from A), C would have a weight of 2 (2 distance units away from A)



So what will happen is the following:



Exchange the position of the nodes whose total weight add up to (length of the directed graph -1) In this case, 3-1 = 2.

A will exchange with C (since the weight of A is 0 hence it will find node C with weight 2 to exchange as their total weight adds up to 2)

B with a weight of 1 will find another node with weight 1 to exchange. However, this another node is itself actually. Then the exchange will stop.



At the end of the exchange, the directed graph will be C -> B -> A   
