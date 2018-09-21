# Python-For-Data-Mining
Using Native Python for Data Mining
# Installing Python IDE

Follow this link, scroll to the end of page and download Python for 32 or 64 bit as per your Windows Version<br>
<a>https://www.python.org/downloads/release/python-364/</a><br>
Click on downloaded .exe file to install<br><br>

# Setting Environment Variable for Python

Environment Variables are set so that when we import libraries in our scripts; operating system knows where to locate those libraries.<br><br>
Right Click on My PC<br><br>
Select Properties<br><br>
Click on Advanced System Settings<br><br>
Click on Environment Variables<br><br>
Under System Variables click New<br><br>
Set variable name to PYTHON_HOME<br><br>
Locate python form C:\Users\hp\AppData\Local\Programs\Python\Python36\ replace "hp" with your username<br><br>
Set variable value to the <b>full path of Python36 folder</b><br><br>
Now locate: variable named "path" under system variables<br><br>
Click "Edit" and at the end of Variable Value add ";%PYTHON_HOME%/"<br><br>
Make sure you added semi-colon before PYTHON_HOME<br><br>
Click OK and OK and OK<br><br>
Now you can check if environment variable is set by running this command in CMD <b>echo %PYTHON_HOME% </b><br><br>
Now run: python --version to validate new environment settings.

# Required Packages

To invoke Weka from Python these packages are required<br>
<ul>
  <li>Pip</li>
  <li>Numpy</li>
  <li>Imaging</li>
  <li>Matplotlib</li>
  <li>Pygraphviz</li>
  <li>Pandas</li>
  <li>Sci-Kit Learn</li>
</ul><br>

# Installing Required PIP Setup Tools for Python

Press <b>WINDOW+R</b> write <b>cmd</b> and press <b>Enter</b> <br><br>
Run <b>python --verison</b> to check if python is properly installed<br><br>
Now,<br><br>
Run <b>python -m pip install --upgrade pip setuptools wheel</b><br><br>
PIP setup tools will be updated.

# Installing Imaging
Run <b>python -m pip install pillow</b><br><br>

# Installing Matplotlib
Run <b>python -m pip install matplotlib</b><br><br>

# Installing Pygraphviz
Errors for Pygraphviz are not resolved yet<br><br>
But for now, you can use Graphviz<br><br>
Run <b>python -m pip install graphviz</b><br><br>

# Installing Pandas
Run <b>python -m pip install pandas</b><br><br>

# Installing Sci-Kit Learn
Run <b>python -m pip install -U scikit-learn</b><br><br>

# Downloading and Running Provided Scripts

Click the green colored <b>Clone or download</b> button on top right corner of this page<br><br>
Click <b>Download Zip</b><br><br>
Extract the downloaded .zip file<br><br>
Navigate to the extracted folder<br><br>
Press Shift and Right Click simultaneously<br><br>
Select <b>Open command window here</b><br><br>
Write <b>python zeror.py</b> and press enter<br><br>
Wait till it loads the libraries: It will output a histogram of data in a new window<br><br>
Similarly, you can run and check output of other files by writing <b>python filename.py</b>

# Copyright Statement

These scripts are just for learning purposes. Kindly don't copy and paste same code and files in your assignment as you won't be the only genius.
