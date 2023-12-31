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
    - tasks folder (with individual task notebooks)


### How to use this repository

If you are familiar with Jupyter notebooks and github, then away you go and enjoy! If not, don't worry. There are ways to view notebooks and run code without any experience or special downloads.

#### What is Github?

GitHub is a web-based platform used by developers when collaborating on software development projects. It offers a place where developers and teams can store, manage and keep control of versions. I have used it to store and manage my project. 

#### What is a jupyter notebook?

A Jupyter Notebook is an web-based notebook that allows readers to view documents containing live code, charts, illustrations and explanatory text. It should all make sense when you run your first notebook!

#### How do I view the notebooks?

Notebooks are in jupyter notebook format. They appear as .ipynb file types. The most convinent way to view these files is to open them directly in the Github repository.

Just double click on the `project.ipynb` or `tasks.ipynb` files.


Notebooks can also be viewed on the Jupyter notebooks viewer website [nbviewer](https://nbviewer.org/). 

Right click on the notebook and "copy link address". Paste the address into the box and go! You can view the notebook, however you will not be able to run the code :(


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

In summary, we first loaded the Iris dataset. We looked at the data and carried out some preprocessing. Next split it into training 70% and testing 30% sets to test several  classification models from scikit-learn. We create a function `train_score_measure()` to train the models, record their accuracy and measure time and memory usage during the training. We evaluated the accuracy of the KNeighborsClassifier with an estimated k value based on the dataset size and then tested different values of k. 


### References

Specific references in notebooks

General references.

Jupyter Notebook - python code editor notebook

Python - the programming 

Python libraries - Various python libraires including: math, random,

Scikit-learn - machine learning 

Pandas - data analysis 

Matplotlib - plotting 

Google colab - Google cloud-based platform with a free Jupyter notebook environment to run and execute code.
