<b>TLDR:</b>

This is a Python implementation of a simple decision tree using Gini impurity.  I used a List of lists to represent a matrix that became the core of the dataset.

To complete this assignment, I followed the excellent [tutorial](https://www.youtube.com/watch?v=LDRbO9a6XPU) on Classification and Regression Trees on the Google Developers Youtube channel, called "Let’s Write a Decision Tree Classifier from Scratch - Machine Learning Recipes #8".  Let's look at the code, and how I implemented the decision tree.


Now for the long part:


To run this tree inducer, we need to provide a file in csv format, with the nominal class in the last column, and a list of attributes to use in our tree. It is assumed for the purpose of this assignment that our commandline arguments are correctly, and the csv file is in the correct format, and the attributes selected are present in the file.

An example to run the program:

`python simple_gini_tree.py iris.csv 1,2,3,4`

(Note: the counting of attributes start at 1. Do not include the last column, which is assumed to be the nominal class.)

First, we have to process our data, which is in csv format. Python makes this simple, because we can `import csv` and use the csv reader to turn the csv_file into a list of list.  In this case, our rows are data elements, and the columns are attributes.  During this process, we will only include the columns indicated in the original commandline invocation.  Additionally, we remove the first row of the data, to save as the headers for attributes when we will print our tree, later.

With our dataset, we will next build our tree recursively.
The first step is to calculate the best splitting criteria for the whole dataset.  We do this by defining a helper class called Decision. Decision has a column, or attribute, and a value to split on.  We create our Decision class and and it's associated information gain by running calculating the gini index for each value in each attribute for the dataset, saving the one that gives us the greatest amound of infogain.  

After performing this, if there is no information gain, we know we have found a leaf. This is because all the datum in the dataset have the same class. 

If it isn't a leaf, we partition the array into two subarrays based on finding the best attribute and rule to split on.  This is where the gini index comes into play.

The gini index is calculated by counting all of the classes in the dataset.  Then for each label, we calculate the probablity that we would choose that label at random for any datum in the dataset.  If the probability is 100 percent, then the dataset is composed of only one class, and it is pure.  The purity ranges from 0 to 1.  So, the best gain we can get is by comparing the current gini index, to the gini index that would be remaining after the decision.  

After calculating this, and splitting our dataset into a left and right (or true and false) based on the attribute and value chosed for our decision, we perform make_tree recursively on the datasets until we have only leaves left.  Now our tree is built, and we can return the root node! 

After this process, we can simply print the tree, which should display the number of nodes and leaves.  Here is some sample output from running:

`python simple_gini_tree.py iris.csv 1,2,3,4`

```
Processing  iris.csv
With attributes  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
Is petal_width >= 1.0?
--> True:
  Is petal_width >= 1.8?
  --> True:
    Is petal_length >= 4.9?
    --> True:
      Predict {'Iris-virginica': 43}
    --> False:
      Is sepal_width >= 3.2?
      --> True:
        Predict {'Iris-versicolor': 1}
      --> False:
        Predict {'Iris-virginica': 2}
  --> False:
    Is petal_length >= 5.0?
    --> True:
      Is petal_width >= 1.6?
      --> True:
        Is petal_length >= 5.8?
        --> True:
          Predict {'Iris-virginica': 1}
        --> False:
          Predict {'Iris-versicolor': 2}
      --> False:
        Predict {'Iris-virginica': 3}
    --> False:
      Is petal_width >= 1.7?
      --> True:
        Predict {'Iris-virginica': 1}
      --> False:
        Predict {'Iris-versicolor': 47}
--> False:
  Predict {'Iris-setosa': 50}
  ```