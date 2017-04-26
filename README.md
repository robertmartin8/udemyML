# Udemy Machine Learning

This repository will contain my code following [Udemy's Machine Learning A-Z course](https://www.udemy.com/machinelearning/learn/v4/overview), by Kirill Eremenko and Hadelin de Ponteves.

Initially I planned on writing notes for all the topics, and I still plan to do this at some stage, but as it happens the course is focused on practical application rather than theory.

The code is not just the same as Hadelin's, in many cases I have made improvements by using libraries that Hadelin has overlooked (e.g backwards elimination in R). I have also included many pictures of plots, some of which are original.

## Also contained in this repository

- `Python_vs_R.md`. This summarises my opinions on when one should use python or R. For each machine learning model, I make some comments on the ease/quality of implementation in each language, and give a verdict on which languag I would use in future.
- A 'cool gif' which was my first experiment into fiddling with the parameters. The gif shows the effect on the classification plot of varying the penalty parameter in the SVM model. I made the gif using an online tool, though the individual images I generated with my own code.
- Various templates. In the Udemy course, Hadelin writes templates that make applying certain models very straightforward. I have made (what I believe to be) improvements.
    - regression templates
    - classification templates
    - plot templates, which contain the code to generate a variety of plots

## Thoughts on the course

The Udemy ML course is one of those courses that advertises its lack of mathematics as if it were a good thing. While there is no doubt that the course gives you the very practical ability to formulaically solve a data problem, if your dataset deviates from the standard, you may have trouble.

Basically, I would have liked to see some more theory, because often this gives you a much better idea of what the various parameters do, and how to improve your results.

However, what I don't understand is where they draw the line between writing code from scratch and using the available libraries. The course makes massive use of the standard libraries most of the time (which I have no objection to), but then sometimes it neglects to use a built-in which would save many lines of code. For example, the backwards-elimination method that we implemented from scratch in R can be replaced by the built in `step()` function. Literally 6 characters.

While I am complaining quite a lot, this course has sparked/renewed my interest in machine learning, and has given me the motivation to go and learn the theory, either from a textbook like Elements of Statistical Learning, or from a more rigorous course like Andrew Ng's machine learning on Coursera, which I had previously started, but had given up on. 
