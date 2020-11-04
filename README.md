# AI Project: pathFinder
[![Video](https://img.youtube.com/vi/ks3G9B3yI0c/0.jpg)](https://www.youtube.com/watch?v=ks3G9B3yI0c)
<br>
This is a very short project I did for our Artificial Intelligence lab course in November. <br>
It was made with Python 3, PyGame for the GUI and interaction, and PIL for converting the map to an array. The code is mostly my own (Everyone uses Stackoverflow a little :p) <br>
<br>
<br>
The program lets you draw a map with walls (red), dust (peach/brown) and lets you put a vacuum cleaner (lol) on it which "cleans" the dust by traveling to available spots on the map.
<br>
<hr>
<p><b>Tools</b>:</p>
<ul>
<li>Code: Python3</li>
<li>UI: PyGame Library</li>
<li>Image manipulation: PIL Library</li>
</ul>
<br>
<hr>
<p><b>How it works</b>:</p>
The algorithm for searching is DFS, and when a pixel of dust is found, it switches to BFS, and when all adjacent specs of dust are collected, it goes back to DFS. It seems more realistic this way than just BFS all the way 🤣
<br>
The program runs at a slight, adjustable delay because otherwise it does everything in a split-second with no hope of seeing what's actually going on.
<br>
<br>
It refreshes 60 times a second (60 FPS) to reflect any changes made to the program by the user or agent.
<br>
<br>
After the map is drawn with PyGame, it is saved as an image. Then, the image is saved as a 2D array with 3 colors each (Red, Green, Blue). When the start button is pressed, the program runs a 2D BFS/DFS algorithm on the array and checks the color value of each pixel to see if it can be traversed and/or cleaned.
After the map is saved, the image is looped once (normal loop) to count dust pixels, and when the cleaning is done, it's looped once again to compare what percentage of the map has been cleaned.
<br>
<br>
Some background info:
At the time of being assigned to do a project, I didn't have any knowledge regarding what to do, what kind of algorithms to use, and I didn't understand most of the projects that came up when searching for "AI Project" on Google. They were way out of my league, and I didn't have the prerequisite knowledge for making something like a chatbot without using Google's APIs.
So I just took the idea of a vacuum cleaner agent thing from the textbook we were following and decided to make a "simulator" of it in a program 🤣
The program is not very polished, and it could've been improved if I was tasked with the project after being taught things like hill climbing and A* search. The only use case I can think of this is for first year students who can't visualize these graph search algorithms in their head. It is what it is though, so if anyone would like to have a look at it feel free to download it.
