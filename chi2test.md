## Ensuring fairness of the dice

Refer to the original [blog post](https://towardsdatascience.com/running-chi-square-tests-in-python-with-die-roll-data-b9903817c51b) for detatils.

In the table below three approaches to trow hexadecimal dice with 10% filling were recorded to be used then in the chi2-square independence test.

Side|Group 1|Group 2|Group 3
--- |  ---  |  ---  |  ---
0   |10	    |12	    |10
1   |4	    |2	    |2
2   |2	    |4	    |0
3   |9	    |5	    |4
4   |5	    |2	    |6
5   |8	    |9	    |8
6   |7	    |7	    |7
7   |3	    |4	    |5
8   |2	    |9	    |5
9   |8	    |7	    |5
A   |5	    |9	    |8
B   |6	    |2	    |6
C   |6	    |8	    |7
D   |4	    |3	    |1
E   |2	    |2	    |4
F   |4	    |5	    |4
Total|85    |90	    |82

This dataset is used in first part of the calculation in the form of numpy array:

```python
dice = np.array([ [10,4,2,9,5,8,7,3,2,8,5,6,6,4,2,4], [12,2,4,5,2,9,7,4,9,7,9,2,8,3,2,5], [10,2,0,4,6,8,7,5,5,5,8,6,7,1,4,4]])
```

Then numpy sums array lines and the script executes standard chi-square test assuming that expected distribution is equal to all 16 categories. 

The test failed for the instance dataset and the dice is not fair.