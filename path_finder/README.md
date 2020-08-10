# Path finder visualizer
Its an implementation of A* (pronounced "A-star") search algorithm to find the optimal path between two points. In this algorithm each path has a weight, the cost to move from one node to another, but in this visualizer each node has the same weight, at least for now, wich means there may exist multiple optimal solutions, for example if you start in the top left corner to the bottom right corner without any obstacles, any of the paths that you move only right and down will be optimal.

## How to use
The only requirement to run this project besides python is the pygame module used for rendering. To install it you can run the code bellow after you've installed python.
```bash
# install pygame
$ pip install pygame
``` 

### Commands
There are two points in the grid, the green dot is the start position and the red is the target position, you can right click and drag any of them to any node you want. If you right click in an empty space (white node) this node will become an obstacle (black node) and vice-versa.
Press enter or the return key to start the visualizer. The blue nodes will form the optimal path until now. To toggle the debug mode you can press the space bar, so the open set (green nodes), the closed set (red nodes) will be displayed.