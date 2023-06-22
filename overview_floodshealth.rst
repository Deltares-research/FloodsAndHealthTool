Introduction
=======

Introduction to the Floods and Health Tool
----------------------

What is the Floods and Health Tool?
^^^^^

This tool performs spatial analysis of floods and population density data in order to identify areas and exposure groups (children/adults) that are at risk of waterborne disease transmission due to flooding. 
The aim of the script is to show the distribution of the population in areas affected by floods, and how different flood levels are likely to affect the risk of infection with a given pathogen for different exposure groups. 
The infection risk and burden of disease are calculated using a Quantitative microbial risk assessment (QMRA), SIR model and the Daily adjusted life years (DALY).

Why the Floods and Health Tool?
^^^^^

Floods can have significant effects on public health, which include direct injuries, destructed health infrastructures, mental health issues and the spread of water or vector-borne diseases. 
These consequences on human well-being can be assessed by incorporating health impacts into flood modelling to allow a comprehensive risk assessment by understanding potential hazards, vulnerabilities and exposures. 
This is done by identifying high risk areas and exposure groups, as well as response strategies and interventions to reduce the risk of infection and disease transmission.

By using the Quantitative Microbial Risk Assessment (QMRA) method in combination with the Susceptible-Infected-Recovered (SIR) approach and the DALY (Disability Adjusted Life Years), 
the Floods and Health model forecasts the infection risk for persons affected by flooding for water-borne diseases and the estimated risk of disease transmission and disease burden in the population. 

We have two goals:  

1. We would like to use this FLood & Health model in the future to make flood risk management scenariose, e.g., probabilistic flood map  
The model can be used to determine the relative change in infection risk and disease transmission in flood risk management scenarios in different regions to communicate risks and propose intervention measures to policymakers and the public (“Flood scenario setting”). 

2. To predict the area and amount of people that are at risk to determine where medication is needed, which areas need medical care (now cast) 
The model can be used to determine the number of persons that potentially will get ill in case of a flood disaster. (“Nowcast in case of disaster”). 

What's behind the Floods and Health Tool? 
^^^^^
The model uses the flood maps produced by SFINCS and WFLOW as part of the HydroMT package and transforms it into the requested format for the health assessment.
Ideally, the input data includes the severity (depth, area) and duration of the flood, as well as demographic information about the affected population (age, social status, pre-existing health conditions) and critical (health) infrastructure.

.. figure:: C:/Users/bleser/OneDrive - Stichting Deltares/Desktop/Floods&Health Quantification/Conceptual model floods&health.png
   :width: 600px
   :align: center

   Floods and Health Tool workflow.

At the current state, the model:

1. Combines the flood maps with population density data to identify the number of people affected by the flood.
2. Uses the age distribution of the population to identify the number of children and adults affected by the flood.
3. Uses the flood depth to identify exposure groups (children/adults) that are at risk of waterborne disease transmission due to flooding.
4. Uses a fixed concentration of pathogens (E.coli) in the floodwater to calculate the infection risk for the exposure groups with the QMRA approach.
5. Uses the infection risk and the number of people affected by the flood to calculate the estimated risk of disease transmission in the population with the SIR approach.
6. Uses the estimated risk of disease transmission in the population and the number of people affected by the flood to calculate the DALY.


How to use the Floods and Health Tool?
^^^^^

