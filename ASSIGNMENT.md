# matteson-decision-tree

Create a decision tree inducer using C++ or Python

Your program should take in a csvfile and a list of which attributes you'd like to use in classification.
Your program should use either the gini index or gain-ratio as the selection criteria
Execution of your program should be as follows:
$./myprog mydata.csv 1,2,3,6,7
Where mydata.csv is in the same directory as the program
1,2,3,6,7 are the attributes which we are selecting to use for classification
1 indexed; assuming there are at least 7 attributes (and an additional 8th for the class label)
no need to handle case where user inputs attribute which isn't listed
The last attribute (column) of any dataset should be the nominal attribute to classify to
output of program should be a text file outputting the decision tree
I.e.
Root
|__Node1
|  |__Leaf1,1
|  |__Leaf1,2
|__Node2
|  |__Node2,1
|  |  |__Leaf2,1,1
|  |  |__Leaf2,1,2
|  |__Leaf2,2
|__Leaf3 

(Using a depth-first based tree search is the easiest way to output this, you can also use an online tool to do this output method if you can find one. The point of the project is the inducer)
Your program should be capable of running on zeus.cs.txstate.edu
Your report should describe what you did, how you did it, any troubles you had and examples of its output.
Page 333 has pseudocode for a basic decision tree.
Your report should be in a PDF, and include your code with your submission (or Github repo, if you submit a repo I will be looking at the master branch for evaluation), and include the zeus-executable program in our submission, along with any test data you used to present in your report.
You may work with other students, but no copying (I will be looking over everyone's code)
Bonus if you can implement a postpruning method with it
explain the process in your report with comparative examples of postpruning and no postpruning on the same dataset/attribute selection pair
Bonus if your selection criterion can handle more than just categorical variables
Can either detect automatically, or be passed within the top of the CSV file which type of variable it is
This assignment part is worth 60 pts out of 100 pts for the total classification assignment.