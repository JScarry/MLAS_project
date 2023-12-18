# Machine learning and statistics

Author: Jarlath Scarry

### Introduction

This repository contains my assignments for the Machine Learning and Statistics modulle of the Higher Diploma in Science in Data Analytics course at ATU 2023. 

It contains:

– A README.md giving a summary of the purpose and contents of the repository, 
  and instructions to clone and run any code or notebooks in it.

– A .gitignore file to ignore any temporary files and folders that should not normally 
  be committed to the repository.

- A project notebook 
    -  Exploring classification algorithms applied on the iris flower data set
    
- A tasks notebook containing the following 5 tasks:
    - Task 1. Square roots
    - Task 2. Chi-square test
    - Task 3. t-test
    - Task 4. k Nearest Neighbours
    - Task 5. Principal Component Analysis
 
 - Supporting materials
    - data folder
    - images folder


### How to use this repository

If you are familiar with Jupyter notebooks and github, then away you go and enjoy! If not, don't worry. There are ways to view notebooks and run code without any experience or special downloads.

#### What is Github?

GitHub is a web-based platform used by developers when collaborating on software development projects. It offers a place where developers and teams can store, manage and keep control of versions. I have used it to store and manage my project. 

#### What is a jupyter notebook?

A Jupyter Notebook is an web-based notebook that allows readers to view documents containing live code, charts, illustrations and explanatory text. It should all make sense when you run your first notebook!

#### How do I view the notebooks?

Notebooks are in jupyter notebook format. They appear as .ipynb file types. The most convinent way to view this file type is on the Jupyter notebooks viewer website [nbviewer](https://nbviewer.org/). 

<a href="https://nbviewer.org" target="_blank">nbviewer</a>

Right click on the notebook and "copy link address". Paste the address into the box and go! You can view the notebook, however you will not be able to run the code :(

#### How do I run the code in the notebooks?

If you have a google account you can use google colab. Sign in and follow these instructions.  
https://colab.research.google.com/?utm_source=scs-index

##### Clone project to your colab.

1. +code. Make a new code cell.
2. Paste in this command and run: !git clone https://github.com/JScarry/MLAS_project

![clone my project](https://github.com/JScarry/MLAS_project/tree/main/images/colab_steps1.png)

##### Open the notebooks

1. File
2. Open notebook
3. Github
4. Paste my github link and search:     https://github.com/JScarry
5. Select the notebook:                 JScarry/MLAS_project

![open a notebook](https://github.com/JScarry/MLAS_project/tree/main/images/colab_steps2.png)

The notebook should load and run.
6. Scroll down and read the documentation
7. Press play to run the code cells

![run some code](https://github.com/JScarry/MLAS_project/tree/main/images/colab_steps3.png)


### Tasks

Assessment throughout the simester involved working on 5 task notebooks. Task titles and a berif description are listed below.

Task 1. Square roots
Write a function sqrt(x) to approximate the square root of a floating point number x without using the power operator or a package.

Task 2. Chi-square test
Consider the contingency table given. Use scipy.stats to perform a chi-squared test to see whether there is any evidence of an association between the results.

Task 3.
Perform a t-test on the famous penguins data set3 to investigate whether there is evidence of a significant difference in the body
mass of male and female gentoo penguins.

Task 4.
Using the famous iris data set suggest whether the setosa class is easily separable from the other two classes. Provide evidence for your answer.

Task 5.
Perform Principal Component Analysis on the iris data set reducing the number of dimensions to two. Explain the purpose of the analysis and your results.

### Project

A notebook exploring classification algorithms applied on the iris flower data set associated with Ronald. A breif explanation of what supervised learning is and then explain what classification algorithms are. A description of the KNN classification algorithm and implementation of it using the scikit-learn Python library.


### References

Jupyter Notebook - python code editor notebook
Python - the programming language
Python libraries - Various python libraires including: math, random, 
Scikit-learn - machine learning library
Pandas - data analysis library
Matplotlib - plotting library
Google colab - Google cloud-based platform with a free Jupyter notebook environment to run and execute code.
