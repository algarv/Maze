<h1> a-MAZE-ing Python Challenge </h1>

This package generates a maze then solves it with recursive back tracking.

<h5> Maze Generation: </h5>

The maze generation function randomly selects a start and end point and creates an array of wall indexes and path indexes, with at least one chain of open 
paths between the start and end points. The function takes a size input to determine the number of rows and columns of the array.

<h5> Maze Solving: </h5>

The solver employs recursive backtracking to find a path between the start and end pixels. From the stating point, it randomly selects an ajacent index. 
If the index is valid, it will "move" to that index and then choose a new adjacent index. If the path is a wall (the value is 1), it will add the index to the 
list of walls and choose a new adjacent index. Any paths previously travelled to are added to their own list, and will only be returned to if an index has no other
adjacent paths. In that case, any index that requires backtracking is added to the wall list. This is visualized as the travelling blue square turning cyan. 
