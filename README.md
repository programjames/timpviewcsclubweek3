# Search Algorithms
These are some of the more common search algorithms that you might use. There
are far more out there. Some interesting ones that you might also want to look
up are Dijkstra's algorithm and the Floyd-Warshall algorithm. It's also helpful
to know some bugpathing algorithms for when you aren't given the entire map.

-----

# Installation
First make sure you have Python installed on your computer. Then you need to
install Pygame. Run the command

    pip install pygame

Now, download the code. You can either download it as a zip or if you have git
installed you can run the command

    git clone https://github.com/programjames/timpviewcsclubweek3.git

-----

# Depth First Search (DFS)
Depth first search is most useful when you have small memory constraints. It
takes each path of a given length and checks whether it reaches the goal. Once
it finds a path that works it returns it. It isn't very efficient time-wise
but one issue with other search algorithms is you can get very large sets, and
that can slow down your program a lot (even if it supposedly has a better
time complexity, it doesn't mean it will always run faster). Also, if you have
a tree DFS will run just as fast as BFS so DFS is often useful when searching
trees as opposed to regular graphs/maps.

-----

# Breadth First Search (BFS)
Breadth first search works by moving outwards from the start location until
it finds the goal. Each iteration it expands the radius by 1 and places a
"direction" attribute on every new square it encounters pointing back towards
the previous square. Once the end goal is found, it can use these directions
to reconstruct the path from the start to the goal.

Note: It's actually often more useful to start at the "end" and end nowhere.
If you run the BFS without stopping until it hits every square, then
you'll be able to get a path from anywhere on the map to the end, not just from
one start location to the end.

Note 2: DFS is often implemented with recursion, but it can also be implemented
similarly to BFS. However, instead of looping through every location in the
open set every time, you just look at the last location in the open set to be
added. Recursion may simplify DFS a lot, but it also makes it slower and take
up more memory (space).

-----

# A*
A* is similar to DFS except instead of taking the most recent square to be
added to the open set it takes the "best" element. How is the best element
determined? By the known distance from the start + the guessed distance to the
end. Normally the taxicab distance or distance-as-the-crow-flies is used for
the guessed distance. Also, you could play with the formula a little and weight
the guessed distance more important than the distance from the start (that way
it'll choose squares closer to the goal).

-----

# Beamsearch
Beamsearch is a mix of A* and BFS. Instead of taking the single best element
as in A* it takes the top 10 (or 100, or however many you want) best elements.
Beamsearch is useful in strategy games like Chess. If you used A* then what if
the position turns out to be really bad 10 steps in? It wouldn't be able to
correct for that. If you used BFS then it wouldn't be able to get far enough
into the game to make a smart decision.

Also, beamsearch is used lots in CodinGame Fall/Spring challenges ;). It's the
go-to strat.

-----
# Floodfill
Floodfill is not a search algorithm, but it's so similar to BFS that I thought
I should include it. It's an algorithm to find the different "rooms" on a map.
You choose any location on the map and then do something similar to BFS,
without worrying about directions. Eventually it'll run out of new places to go
and you'll have found all the squares in the room. You just repeat this step
until every square has been visited on the map and you get all of the squares
for each room.
