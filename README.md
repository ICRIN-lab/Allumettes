# Lucifer Task 

## CONTENTS OF THIS FILE

* Introduction
* Lucifer Task
* Task design example
* Requirements
* Contributions
* More informations
* Contact


## INTRODUCTION

Our research team is studying different aspects of psychiatric disorders. Our present project is all about exploring obssessive compulsive disorders' secret garden. For that matter, we designed original home-made cognitive tasks, fresh out of the oven!

## Lucifer Task

If you have tried the other cognitive tasks, you probably think that we are going to set the stage on fire one more time with this Lucifer task. Well, you're not totally wrong, however for security matters that is not what we are asking our participants. 

What is it about then ? Let us give you a hint : *Charlie Babbitt? Raymond? Dustin Hoffman? Tom Cruise ?* ... Still no clue ? **[RAIN MAN](https://youtu.be/Kc-jq06IKtk)**, the movie ! 

If you guessed or at least know what we are talking about, remember that scene when Raymond guessed the 246 toothpicks on the floor in  a few seconds ? THAT is the idea behind our task : counting the number of lucifers displayed in 2 seconds. 

If you have no idea what we are talking about, "Step 3" is mandatory (for obvious reasons).


All the images are stored in the file "img". Our code generates random number of lucifers, with different orientations and shapes. You can find it in [generate_lucifers](https://github.com/ICRIN-lab/lucifer/tree/main/generate_lucifers").   

There are 100 trials. Each visual stimuli contains a random number of lucifers in different orientations and shapes, and is displayed for  2 seconds. A question appears afterward "Combien d'allumettes avez-vous vu ?" *in french* ("How many lucifers are there ?"). The participants have to choose among 2 propositions, only one is right.

The task starts with instructions written in french, and are designed for "Trackpad" response.

## Task Design example

Here is an example of the task. 

![img_readme](https://user-images.githubusercontent.com/92592951/169014965-6b71fa07-aa2c-463d-afea-96554cd59b6c.png)
![question_readme](https://user-images.githubusercontent.com/92592951/169014991-1fe010ee-6667-4fa5-98c2-c57e3ba7ab43.png)



## REQUIREMENTS

### Imports :

We use the package PsychoPy under Python 3.6 to run the tasks. Furthermore, Lucifer Task requires the import of time, as the time spent by the participants is a valuable data.
```python
import time
from list_images import images
from psychopy import core
from Template_Task_Psychopy.task_template import TaskTemplate
```

In order to import TaskTemplate, here are our recommendations. :

* **Step 1** : Clone Template_Task_Psychopy repository from GitHub 


Here's the link :  <a href="https://github.com/ICRIN-lab/Template_Task_Psychopy.git"> here </a>


* **Step 2**: Create a symbolic link locally with Template_Task_Psychopy :

```python
  yourtask_directory % ln -s ../Template_Task_Psychopy Template_Task_Psychopy
```  

* **Step 3**: Watch Rain Man.

### Specificities :

If you want to try this cognitive task using your keyboard, don't forget to the response_pad to False

```python
class SevenDiff(TaskTemplate):
    nb_ans = 4
    response_pad = False  # has to be set on "True" if a trackpad is used.
```

## Contributions

To contribute, please fork the repository, hack in a feature branch, and send a pull request.

## More informations

Homepage: [iCRIN Lab](http://icrin.fr/)

## Contact us

Mail : contact@icrin.fr
Twitter : https://twitter.com/RedwanMaatoug
