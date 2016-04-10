## P1: Movie Trailer Website

### Overview of the Project:

For the first project in _Udacity_'s **Full Stack Web Development Nanodegree**, I needed to write server-side code in *Python* to store a list of my favorite movies, including box art imagery and a movie trailer URL. I then needed to use the code to generate a static web page allowing visitors to browse the movies and watch the trailers. The goal of this project was to establish a foundation in core programming concepts using *Python*.

### Minimum tasks that needed to be completed to meet expectations:

At a minimum, I needed to define a Movie class, instantiate various Movie objects using that class, and then create a list using the newly created objects. The list then needed to be passed to the `open_movies_page()` function found in `fresh_tomatoes.py`, which then generates an `.html` file using the information contained in the objects.

### Additional functionalities I decided to implement to exceed expectations:

In order to exceed the project's expectations, I decided to:
 1. Modify the *Bootstrap* template (i.e. the color scheme and the navbar) to make the website more visually appealing.
 2. Define a function that parses the information contained in an *XML* file passed as a commandline argument, which can then be used to create the objects.
 3. Add a *jQuery* mouseover event that displays the description of the movie and hide the box art imagery whenever the use moves the mouse over a movie tile.
 4. Add a *jQuery* mouseout event that displays the box art imagery and hide the description of the movie whenever the users moves the mouse out of a movie tile.

### Description of Files, Classes and Functions:

* **start.py:** This is the only file that needs to be manually run by the user. In order to launch the script and generate the static `.html` web page, one needs to run the following command: `python start.py movies.xml`.

* **entertainment_center.py:** Once the start.py script is run, the first function that is called is `createObjects()`, which is found in this class. This function subsequently calls `parsexml()`, which parses the information contained in an *XML* file passed as a commandline argument, and then uses that information to create objects using the `Movie` class defined in `media.py`. A list is then created using the newly-created Movie objects and then passed the list to the `open_movies_page()` function found in `fresh_tomatoes.py`, which automatically generate the file `fresh_tomatoes.html` which is the website that can be displayed in the browser of the user.

* **media.py:** This file contain the `Movie` class used to instantiate `Movie` objects. The class defines a simple constructor and function that opens movie trailers using the **webbrowser** module, which is called whenever the user clicks on 'Watch trailer'.

* **fresh_tomatoes.py:** This file, in addition to containing all the *HTML* and *CSS* required to generate the static web page, contains the `open_movies_page()` function that takes a list of `Movie` objects passed as argument and generate the `.html` file.

* **README.md**: This is the file you're reading.

### License 

MIT License

Copyright (c) 2016 minimal1st

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
