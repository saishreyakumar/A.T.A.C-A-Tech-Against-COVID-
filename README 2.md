# A.T.A.C
A Tech Against Covid - (yours truly  , from coden't)

how to run the file ?

step 1: run serving.py
step 2: go to the local host 
step 3: select one of the two options from the main page 
step 4: fill in the forms by clicking on each of the buttons sequentially
step 5: click on generate report 
step 6: an image of your xray will appear 
step 7: and check the browser for your report 

all about A.T.A.C

A.T.A.C (pronounced attack) - "A Tech Against COVID"

The world looks at a way to make things easier, to automate processes.
Today we stand amidst a crisis way bigger than all of us, something that was at the least of our expectations.
Our idea is to look at automating healthcare, to make it accessible to each and every person in the country, in short to "nationalize the healthcare system", at least during a pandemic as that of the present.
We are taking covid-19 as the scenario and we’re creating an application that when inputted with patient stats will auto-generate a report 


What can our product achieve?

* increased speed in producing test results 
* highly accurate results 
* healthcare staff safety 
* patient safety 
* equal accessibility of healthcare services to all
* more flexible healthcare services 
* easier procedure
* eliminates human error due to results by highly accurately trained  ML model 
* saves energy, time, money 
  and ultimately lives.

Let’s take a scenario considering the current pandemic:

A person after being tested positive for the coronavirus enters a healthcare utility. He hopes to know how adverse his conditions are and his chances of survival. As a part of our application, it will take in the body temperature, oximeter readings, spirometer readings and will take in the chest x ray image of the patient as an input. based on the above data, the application will generate the adversity of the condition of the patient and will present to him in the form of a report.  
We are using a Keras ML model to train the system to classify the x-ray images and to accurately whether the patient’s lungs seem to be adversely affected by COVID-19  or not. The x ray image input taken in is compared with the vast amount of supplied training data and an absolutely accurate result is obtained as we are eliminating the chance of occurrence  of human errors. We are using convolutional neural network(CNN) for the process , i.e we are using computer vision . we are training the machine to provide the most accurate of results . 
This whole process eliminates the need to wait for a long time for analyzing x-ray scans and reports and therefore people don’t have to wait for days before they find out about their health condition in anxiety. As a cure is implemented earlier, chances of survival also increase. 
A similar scenario can be put forth for those who have been tested negative, but want to get themselves tested. Both positive and negative patients are given different unique codes to differentiate them and to easily identify them.
A similar process can be applied to any pandemic that may arise in the near future and therefore is compatible for the future as well.

“Let’s save time, money, energy and ultimately lives”

 
tech stacks used :

*python 
*keras – TensorFlow – for ml model - CNN
*database – sqlite3
*html
*CSS
*flask
*jinja templates

