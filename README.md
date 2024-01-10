# Phonepe_Pulse_Data_Visualization

## *Introduction*

Phonepe_Pulse_Data_Visualization aims to give users a friendly environment which can be used to visualize the PhonePe pulse data and gain lots of insights on Transactions, Number of users, Top states and District. We have used Geo India map visualization and some of Bar charts, Pie charts to get more insights. Inorder to achieve a user friendly environment this was built on top of Streamlit Dashboard.

## *Table of Contents*

1.  Technologies used
1.  Libraries used
1.  Features
1.  Geo India map visualization
1.  Data Analysis using Streeamlit and Plotly


## *Technologies used*

1. Python    - for Coding
1. MYSQL     - SQL Database for storing the Phonepe_data
1. Streamlit - for Visualization front-end
1. Plotly    - to perform visualized charts for data analysis

## *Libraries used*

Below libraires were used to code the project
```python
-- import streamlit as st
-- import pandas as pd
-- import pymysql
-- import plotly.express as px 
-- from streamlit_option_menu import option_menu
```

## *Features*

- Cloning the Phonepe data from "https://github.com/PhonePe/pulse.git"
- Store the retrieved data in a MySQL database.
- Convert the retrieved data to Pandas
- Creating a Geo Map visualization for India
- Analyze and visualize data using Streamlit and Plotly to gain more insights

## *Geo Map visualization for India*

Geo Map for India was built from choropleth using a geojson id for States. Once the outline was drawn the actual data was appened by converting it to Dataframe which will locate State wise Transactions and User details. This is made simple for Users to select and give their own set of data from the Select box eg. Type of transactions, year, quarter.. Based on User input the Map will how the range how much contributions were made by each state and which state wins the play for each criteria

## *Data Analysis using Streeamlit and Plotly*

We have used plotly Pie and Bar charts to seggregate the data based on number of users, Transactions performed. Users can use the friendly enivronment of Streamlit to play with datas by specifying Transaction_type, Year, Qaurter for which they wanted to do analysis. Once the details are selected the Charts will be displayed with the comparison between states, transactions done, Total amount done for each.


Hope this project will help you undersatnd the data and get more insights!! Thankyou:) 

**Contact**

📧 Email: nishanthnici@gmail.com 
