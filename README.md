# Select Yes or No

![tkinter window](https://github.com/Duvey314/yesorno/blob/master/resources/tkinter_selector.PNG)


## Table of contents
* [Overview](#overview)
* [Technologies](#technologies)

### Overview
This project is a look at what data you can collect from something as simple as selecting yes or no. Once the user makes a selection, a number of visualizations are displayed.

The first iteration of this project used the tkinter gui to display a selector window. The results were then displayed in a new window and visualizations were added using matplotlib. Much of the data collected used IP-API to collect things like IP address, location, and internet provider. The position on the button selected is displayed using matplotlib and the event function in tkinter. The database is sotred locally as a csv.

![yes selection](https://github.com/Duvey314/yesorno/blob/master/resources/yes_click_locations.PNG)

The second iteration is the production version of the project. The idea is the same but the implementation is different. To move the framework onto the web the first thing to do is implement the selection and answer windows in JavaScript to make pushing the project to the web easier. The second is that the matplotlib library works well for static graphs but I would like to use graphs that are more interactive. Because of this, I will switch to plotly to give more filtering and interactivity to the graphs. Lastly, the local storage in a csv does not work for a web application. I will instead be using the MongoDB Atlas Cloud service.

### Technologies

* tkinter
* MatPlotLib
* Plotly
* MongoDB


