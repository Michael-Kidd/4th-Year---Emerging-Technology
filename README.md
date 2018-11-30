# 4th Year Emerging Technology

----------

----------


The Programs, notebooks and files contained here have multiple purposes:

- A Numpy notebook that shows how the numpy package works and the different distributions that are used with numpy.
- A Iris Dataset notebook that shows how keras can learn from data set created using flowers and can be read in and we can use to determine an unknown flower and test the neural network to narrow down which flower we have input.
- A Mnist Notebook that shows how to use the Mnist data set to identify handwritten digits.
- The main Project program written in python and allows a user to write an image on a canvas and will train a neural network to identify what the user have written.
- A Digit recognition notebook that explains and breaks down the steps and structure of the project.
 

## Getting Started

------


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

----------

* Anaconda - A free and open source distribution of the Python and R programming languages for data science and machine learning related applications.
* Tkinter - A GUI used as standard in Python, We will use this to Take a Digit from the user.
* Keras - A High level machine learning API, used to train neural networks.
* Numpy - A fundamental package for scientific computing in python. We use it for array handling and random distributions.
* Matplotlib - 2D plotting library for python. We use it to show plots in our notebooks.
* SKlearn - Used for machine learning in Python.
* Gzip - Lossless Compression and Decompression utility we use to manage the MNist Data Set.
* Pillow - an image library in python. We will use it to manage images for our programs.

#### Installing Anaconda

----------

What things you need to install the software and how to install them

Install Anaconda along with python, During the installation make sure to choose the option to add python and Anaconda to the envoirnment path. Download Anaconda from the following location.

[Anaconda Download Link](https://www.anaconda.com/download/)

To Install Anaconda Click the Link Above and your will see the following screen: <br />
![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/AnacondaDownload.png)

Choose a Version of python that you wish to use then click to download it. Locate the downloaded file and run it.<br />

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen1Anaconda.png)

You will be presented with this screen.<br />

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen2Anaconda.PNG)

Once you go passed the Terms and Conditions you will see the next screen.<br />

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen3Anaconda.PNG)

Here you can choose if you want to install the program just for you or for all users on your machine.<br />

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen4Anaconda.PNG)

On the next screen you must select both options. The first will add Anaconda to the PATH Environment, the second will set the version of python you chose as the Default on this machine.<br />

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen5Anaconda.PNG)

Once completed click next, now Anaconda will install.

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Screen6Anaconda.PNG)



#### Installing Keras
----------
Install Keras by running the following command in a Command Line: <br /> 


```
$ Conda install Keras 
```

#### Installing Pillow
----------

Install Pillow by running the following command in a Command Line: <br />


```
$ Conda install Pillow 
```

#### Installing Numpy
----------
Install Numpy by running the following command in a Command Line: <br />


```
$ Conda install numpy 
```

#### Installing Scipy
----------

Install Scipy by running the following command in a Command Line: <br />


```
$ Conda install scipy 
```

#### Installing Matplotlib
----------

Install matplotlib by running the following command in a Command Line: <br />


```
$ Conda install matplotlib 
```

#### Installing SLearn
----------
Install SKLearn by running the following command: <br />


```
$ Conda install scikit-learn
```

## Running the tests
----

[![Link](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/youtube.PNG)](https://www.youtube.com/watch?v=NEdvWyPBqVg&feature=youtu.be)

### How to test the Digit Recognition Program.
----

First you must clone the repo: Open up a command line terminal and change to the directory where you would like to store the files

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone.PNG)

Then you must clone by using the following command as seen in the image below:

```
$ git clone https://github.com/Michael-Kidd/4th-Year---Emerging-Technology
```

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone2.PNG)

Run the following command to be presented with the canvas that will show the GUI you will use:

```
$ python DigitRecognition.py
```

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit.PNG)

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit2.PNG)

Simply now write Digits into the canvas and click "Check Number"

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit3.PNG)

In the image I drew an 8, then When I let the program determine the number and was given the result "You write the number [8]".
Write any number you wish between 0-9.

## Deployment.
----
### How to Run the Notebook.
----

First you must clone the Repo: Open up a command line terminal and change to the directory where you would like to store the files

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone.PNG)

Then you must clone by using the following command as seen in the image below:

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone.PNG)

Run the Following command to start Jupyter Notebook.

```
$ Jupyter Notebook
```

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/notebookrun.PNG)

Below you can see Jupyter Notebook running and can select one of the Notebooks to view.

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/notebookrun2.PNG)

### How to Run the Digit Recognition Program.
----

To run the program, you must follow the same steps as if you were testing the program.
First you must clone the repo: Open up a command line terminal and change to the directory where you would like to store the files

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone.PNG)

Then you must clone by using the following command as seen in the image below:

```
$ git clone https://github.com/Michael-Kidd/4th-Year---Emerging-Technology
```

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/Gitclone2.PNG)

Run the following command to be presented with the canvas that will show the GUI you will use:

```
$ python DigitRecognition.py
```

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit.PNG)

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit2.PNG)

Simply now write Digits into the canvas and click "Check Number"

![](https://raw.githubusercontent.com/Michael-Kidd/4th-Year---Emerging-Technology/master/Data/images%20for%20wiki%20and%20readme/RunpyDigit3.PNG)

In the image I drew an 8, then When I let the program determine the number and was given the result "You write the number [8]".
Write any number you wish between 0-9.
## Built With
---

* [Python](https://www.python.org/downloads/) - The Programming Language used.
* [Keras](https://keras.io/) - High-level neural networks API.
* [Tensorflow](https://www.tensorflow.org/) - Machine learning framework.


## Versioning
----

This program will only be used during the completion of the course and will have no release or commercial use.

## Authors
----

* **Michael Kidd** - *Main body of work* - [GitHub](https://github.com/Michael-Kidd/)

## License
----

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
----

Thank you to Dr. Ian McLoughlin for the course work, assistance and tutorials on completing the project