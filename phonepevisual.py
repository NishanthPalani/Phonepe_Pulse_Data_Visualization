import os
import json
import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px 
from streamlit_option_menu import option_menu
import geopandas as go

#https://www.youtube.com/watch?v=49Tg6ypGjgc&t=112s
#https://www.youtube.com/watch?v=pWxDxhWXJos
#https://github.com/NishanthPalani/Phonepe_Pulse_Data_Visualization/blob/main/README.md

## Connecting to MYSQL and storing the table into DataFrame
myconnection = pymysql.connect(host = '127.0.0.1',user='root',password='admin@123',database = "phonepe_data")
cur = myconnection.cursor()

## Function to retreive data from GIT repository for PhonePe Pulse Data
def data_retrieve():
    global Agg_Trans
    global Map_Trans
    global Top_Trans_District
    global Top_Trans_Pincode
    global Agg_Users
    global Map_Users
    global Top_Users_District
    global Top_Users_Pincode

    path1 = "F:/data science/VS/DataScience projects/pulse/data/aggregated/transaction/country/india/state/"
    path2 = "F:/data science/VS/DataScience projects/pulse/data/map/transaction/hover/country/india/state/"
    path3 = "F:/data science/VS/DataScience projects/pulse/data/top/transaction/country/india/state/"
    path4 = "F:/data science/VS/DataScience projects/pulse/data/aggregated/user/country/india/state/"
    path5 = "F:/data science/VS/DataScience projects/pulse/data/map/user/hover/country/india/state/"
    path6 = "F:/data science/VS/DataScience projects/pulse/data/top/user/country/india/state/"

    Agg_state_list=os.listdir(path1)
    clm1={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Agg_state_list:
        p_i=path1+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['transactionData']:
                    Name=z['name']
                    count=z['paymentInstruments'][0]['count']
                    amount=z['paymentInstruments'][0]['amount']
                    clm1['Transacion_type'].append(Name)
                    clm1['Transacion_count'].append(count)
                    clm1['Transacion_amount'].append(amount)
                    clm1['State'].append(i)
                    clm1['Year'].append(j)
                    clm1['Quater'].append(int(k.strip('.json')))
    Agg_Trans=pd.DataFrame(clm1)


    Agg_state_list=os.listdir(path2)
    clm2={'State':[], 'Year':[],'Quater':[],'District_Name':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Agg_state_list:
        p_i=path2+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['hoverDataList']:
                    Name=z['name']
                    count=z['metric'][0]['count']
                    amount=z['metric'][0]['amount']
                    clm2['District_Name'].append(Name)
                    clm2['Transacion_count'].append(count)
                    clm2['Transacion_amount'].append(amount)
                    clm2['State'].append(i)
                    clm2['Year'].append(j)
                    clm2['Quater'].append(int(k.strip('.json')))
    Map_Trans=pd.DataFrame(clm2)


    Agg_state_list=os.listdir(path3)
    clm3={'State':[], 'Year':[],'Quater':[],'City_Name':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Agg_state_list:
        p_i=path3+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['districts']:
                    Name=z['entityName']
                    count=z['metric']['count']
                    amount=z['metric']['amount']
                    clm3['City_Name'].append(Name)
                    clm3['Transacion_count'].append(count)
                    clm3['Transacion_amount'].append(amount)
                    clm3['State'].append(i)
                    clm3['Year'].append(j)
                    clm3['Quater'].append(int(k.strip('.json')))
    Top_Trans_District=pd.DataFrame(clm3)


    Agg_state_list=os.listdir(path3)
    clm3={'State':[], 'Year':[],'Quater':[],'Pincode_Id':[], 'Transacion_count':[], 'Transacion_amount':[]}

    for i in Agg_state_list:
        p_i=path3+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                for z in D['data']['pincodes']:
                    Name=z['entityName']
                    count=z['metric']['count']
                    amount=z['metric']['amount']
                    clm3['Pincode_Id'].append(Name)
                    clm3['Transacion_count'].append(count)
                    clm3['Transacion_amount'].append(amount)
                    clm3['State'].append(i)
                    clm3['Year'].append(j)
                    clm3['Quater'].append(int(k.strip('.json')))
    Top_Trans_Pincode=pd.DataFrame(clm3)


    Agg_state_list=os.listdir(path4)
    clm4={'State':[], 'Year':[],'Quater':[],'brand_name':[], 'Transacion_count':[], 'Transacion_percentage':[]}

    for i in Agg_state_list:
        p_i=path4+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                try:
                    for z in D["data"]["usersByDevice"]:
                        name = z["brand"]
                        count = z["count"]
                        percentage = z["percentage"]*100
                        #registered_users = z["aggregated"]["registeredUsers"]
                        clm4["brand_name"].append(name)
                        clm4['Transacion_count'].append(count)
                        clm4['Transacion_percentage'].append(percentage)
                        #clm4["Registered_users"].append(registered_users)
                        clm4['State'].append(i)
                        clm4['Year'].append(j)
                        clm4['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    Agg_Users=pd.DataFrame(clm4)
 

    Agg_state_list=os.listdir(path5)
    clm5={'State':[], 'Year':[],'Quater':[],'District_name':[], 'registered_users':[], 'Total_appOpens':[]}

    for i in Agg_state_list:
        p_i=path5+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                try:
                    for z in D["data"]["hoverData"].items():
                        name = z[0]
                        users = z[1]["registeredUsers"]
                        appOpens = z[1]["appOpens"]
                        clm5["District_name"].append(name)
                        clm5['registered_users'].append(users)
                        clm5['Total_appOpens'].append(appOpens)
                        clm5['State'].append(i)
                        clm5['Year'].append(j)
                        clm5['Quater'].append(int(k.strip('.json')))
                except:
                    pass
    Map_Users=pd.DataFrame(clm5)


    Agg_state_list=os.listdir(path6)
    clm6={'State':[], 'Year':[],'Quater':[],'District_name':[], 'registered_users':[]}

    for i in Agg_state_list:
        p_i=path6+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                try:
                    for z in D["data"]["districts"]:
                        name = z["name"]
                        users = z["registeredUsers"]
                        clm6["District_name"].append(name)
                        clm6['registered_users'].append(users)
                        clm6['State'].append(i)
                        clm6['Year'].append(j)
                        clm6['Quater'].append(int(k.strip('.json')))

                except:
                    pass
    Top_Users_District=pd.DataFrame(clm6)


    Agg_state_list=os.listdir(path6)
    clm6={'State':[], 'Year':[],'Quater':[],'Pincode_id':[], 'registered_users':[]}

    for i in Agg_state_list:
        p_i=path6+i+"/"
        Agg_yr=os.listdir(p_i)
        for j in Agg_yr:
            p_j=p_i+j+"/"
            Agg_yr_list=os.listdir(p_j)
            for k in Agg_yr_list:
                p_k=p_j+k
                Data=open(p_k,'r')
                D=json.load(Data)
                #pprint(D)
                try:
                    for z in D["data"]["pincodes"]:
                        name = z["name"]
                        users = z["registeredUsers"]
                        clm6["Pincode_id"].append(name)
                        clm6['registered_users'].append(users)
                        clm6['State'].append(i)
                        clm6['Year'].append(j)
                        clm6['Quater'].append(int(k.strip('.json')))

                except:
                    pass
    Top_Users_Pincode=pd.DataFrame(clm6)

    sql_table_define()
    sql_load()



## Function to define the SQL Table
def sql_table_define():

    myconnection = pymysql.connect(host = '127.0.0.1',user='root',passwd='admin@123')
    cur = myconnection.cursor()
    cur.execute("create database if not exists phonepe_data")
    myconnection = pymysql.connect(host = '127.0.0.1',user='root',passwd='admin@123',database = "phonepe_data")
    cur = myconnection.cursor()
    cur.execute("drop table if exists Aggregate_Transaction")
    cur.execute("drop table if exists Map_Transaction")
    cur.execute("drop table if exists Top_Transaction_District")
    cur.execute("drop table if exists Top_Transaction_Pinciode")
    cur.execute("drop table if exists Aggregate_Users")
    cur.execute("drop table if exists Map_Users")
    cur.execute("drop table if exists Top_Users_District")
    cur.execute("drop table if exists Top_Users_Pincode")
    myconnection.commit()


    cur.execute("create table if not exists Aggregate_Transaction(State VARCHAR(255),Year int,Quarter VARCHAR(10),Transacion_type VARCHAR(255),Transacion_count int,Transacion_amount BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Map_Transaction(State VARCHAR(255),Year int,Quarter VARCHAR(10),District_Name VARCHAR(255),Transacion_count BIGINT,Transacion_amount BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Top_Transaction_District(State VARCHAR(255),Year int,Quarter VARCHAR(10),City_Name VARCHAR(255),Transacion_count BIGINT,Transacion_amount BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Top_Transaction_Pincode(State VARCHAR(255),Year int,Quarter VARCHAR(10),Pincode_id BIGINT,Transacion_count BIGINT,Transacion_amount BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Aggregate_Users(State VARCHAR(255),Year int,Quarter VARCHAR(10),brand_name VARCHAR(255),Transacion_count BIGINT,Transacion_percentage float(9,2))")
    myconnection.commit()
    cur.execute("create table if not exists Map_Users(State VARCHAR(255),Year int,Quarter VARCHAR(10),District_name VARCHAR(255),registered_users BIGINT,Total_appOpens BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Top_Users_District(State VARCHAR(255),Year int,Quarter VARCHAR(10),District_name VARCHAR(255),registered_users BIGINT)")
    myconnection.commit()
    cur.execute("create table if not exists Top_Users_Pincode(State VARCHAR(255),Year int,Quarter VARCHAR(10),Pincode_id BIGINT,registered_users BIGINT)")
    myconnection.commit()


## Function to load the data to SQL Table
def sql_load():
    sql = "insert into Aggregate_Transaction values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Agg_Trans)):
        cur.execute(sql,tuple(Agg_Trans.iloc[i]))
        myconnection.commit()

    sql = "insert into Map_Transaction values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Map_Trans)):
        cur.execute(sql,tuple(Map_Trans.iloc[i]))
        myconnection.commit()

    sql = "insert into Top_Transaction_District values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Top_Trans_District)):
        cur.execute(sql,tuple(Top_Trans_District.iloc[i]))
        myconnection.commit()

    sql = "insert into Top_Transaction_Pincode values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Top_Trans_Pincode)):
        cur.execute(sql,tuple(Top_Trans_Pincode.iloc[i]))
        myconnection.commit()
        
    sql = "insert into Aggregate_Users values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Agg_Users)):
        cur.execute(sql,tuple(Agg_Users.iloc[i]))
        myconnection.commit()

    sql = "insert into Map_Users values(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(Map_Users)):
        cur.execute(sql,tuple(Map_Users.iloc[i]))
        myconnection.commit()

    sql = "insert into Top_Users_District values(%s,%s,%s,%s,%s)"
    for i in range(0,len(Top_Users_District)):
        cur.execute(sql,tuple(Top_Users_District.iloc[i]))
        myconnection.commit()

    sql = "insert into Top_Users_Pincode values(%s,%s,%s,%s,%s)"
    for i in range(0,len(Top_Users_Pincode)):
        cur.execute(sql,tuple(Top_Users_Pincode.iloc[i]))
        myconnection.commit()


## Below steps will retreive data from MYSQL and convert to PANDAS Dataframe
df_agg_trans = pd.read_sql_query("select * from Aggregate_Transaction;",myconnection)
df_agg_trans["year"] = df_agg_trans['Year'].astype(str)
df_agg_trans["Quarter"] = df_agg_trans['Quarter'].astype(str)
df_map_trans = pd.read_sql_query("select * from Map_Transaction;",myconnection)
df_top_trans_district = pd.read_sql_query("select * from Top_Transaction_District;",myconnection)
df_top_trans_pincode = pd.read_sql_query("select * from Top_Transaction_Pincode;",myconnection)
df_agg_user = pd.read_sql_query("select * from Aggregate_Users;",myconnection)
df_map_user = pd.read_sql_query("select * from Map_Users;",myconnection)
df_top_user_district = pd.read_sql_query("select * from Top_Users_District;",myconnection)
df_top_user_pincode = pd.read_sql_query("select * from Top_Users_Pincode;",myconnection)



## Below Class convert will convert the Amount fields to rupees format
class convert:
    def millions(transaction):
        a = transaction
        c = int(a)/1000000
        d = '{:.2f}'.format(c)
        e = str(d) + ' Million'
        return e

    def billions(transaction):
        a = transaction
        c = int(a)/1000000000
        d = '{:.2f}'.format(c)
        e = str(d) + ' Billion'
        return e

    def trillions(transaction):
        a = transaction
        c = int(a)/1000000000000
        d = '{:.2f}'.format(c)
        e = str(d) + ' Trillion'
        return e

    def crores(transaction):
        a = transaction
        c = int(a)/10000000
        d = '{:.2f}'.format(c)
        e = str(d) + ' Crore'
        return e

    def thousands(transaction):
        a = transaction
        c = int(a)/1000
        d = '{:.2f}'.format(c)
        e = str(d) + ' Thousand'
        return e

    def rupees(transaction):
        a = transaction
        if len(a) <= 3:
            return a
        elif len(a) in (4, 5, 6):
            return convert.thousands(a)
        elif len(a) in (7, 8, 9):
            return convert.millions(a)
        elif len(a) in (10, 11, 12):
            return convert.billions(a)
        elif len(a) >= 13:
            return convert.trillions(a)

## Below code will do page title(tab Name) configuration
st.set_page_config(page_title= "Phonepe Pulse Data Visualization",
                   layout= "wide")

## Below code will create the header for sidebar as well the options table 
st.sidebar.header(":violet[**Welcome to the dashboard**]")
with st.sidebar:
    selected = option_menu("Menu", ["Home","Map View","Explore More Data"], 
                icons=["house","flag-fill","bar-chart-line"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F99AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})

## Below code will be active if "Home" is selected from side bar
if selected == "Home":
    st.markdown("# :violet[Phonepe Data Visualization and Exploration]")
    col1,col2 = st.columns([8,1],gap="small")
    with col1:
        st.write(" ")
        st.markdown("### :blue[Overview :]")
        st.markdown("#### This streamlit app aims to give users a friendly environment which can be used to visualize the PhonePe pulse data and gain lots of insights on Transactions, Number of users, Top states and Districts. Bar charts, Pie charts and Geo map visualization are used to get insights.")
        st.markdown("### :blue[Technologies used :]")
        st.markdown("#### - Github - Cloning for input Data")
        st.markdown("#### - Python, Pandas")
        st.markdown("#### - MySQL Streamlit and Plotly")
        st.markdown("#### - Streamlit and Plotly")
    with col2:
        st.write(" ")
## Below code will be active if "Map View" is selected from side bar
elif selected == "Map View":
    st.write("### :violet[Welcome to Map View Page ]")
    trans_user = st.sidebar.radio(
     "Please select the type",
     ('Transaction', 'User'))        ## This will create a radio button for Transactions and User

    ## Below will create a multiselect box for Transaction type, year, Quarter
    if trans_user == "Transaction":
        category_agg_trans_type=st.sidebar.multiselect("Transaction_type:",
                                        options=df_agg_trans["Transacion_type"].unique(),
                                        default='Recharge & bill payments'
                                        )
        category_agg_trans_year=st.sidebar.multiselect("Year:",
                                    options=df_agg_trans["Year"].unique(),
                                    default=2018
                                    )
        category_agg_trans_quarter=st.sidebar.multiselect("Quarter:",
                                options=df_agg_trans["Quarter"].unique(),
                                default="1"
                                )

        ## Below will perform take the selected items from the multiselect and assign as User inputs
        selection_agg_trans = df_agg_trans.query(
            "Transacion_type == @category_agg_trans_type & Year == @category_agg_trans_year & Quarter == @category_agg_trans_quarter"
        )

        ## Below will convert the number format to currency 
        Total_trans_count = convert.rupees(str(selection_agg_trans["Transacion_count"].sum()))
        Total_trans_amount = convert.rupees(str(selection_agg_trans["Transacion_amount"].sum()))

        Total_trans_count1 = (selection_agg_trans.groupby("State")["Transacion_count"].sum())
        Total_trans_amount1 = (selection_agg_trans.groupby("State")["Transacion_amount"].sum())

        Total_trans_count2 = (selection_agg_trans.groupby("State")["Transacion_count"].sum().sort_values(ascending=False).head(1)) #this will extract the first row
        Total_trans_amount2 = (selection_agg_trans.groupby("State")["Transacion_amount"].sum().sort_values(ascending=False).head(1))

        Total_trans_State = Total_trans_count2.index[0]             ## This will only extarct the index iem of Pandas Series
        Total_trans_State = str(Total_trans_State).capitalize()     ## This will make the first letter capital
        Total_trans_count2 = convert.rupees(str(Total_trans_count2[0]))
        Total_trans_amount2 = convert.rupees(str(Total_trans_amount2[0]))

        ## Based on above calculations below will display those in Streamlit page
        col1,col2 = st.columns([1,1],gap="small")
        with col1:
            st.write("#### :orange[Cummulative Total for Transactions & Amount]")
            st.write(":green[Total Transactions] =",Total_trans_count)
            st.write(":green[Total Transaction amount] =",Total_trans_amount)
        with col2:
            st.write("#### :orange[TOP Performed State]")
            st.write(":green[State] =",Total_trans_State)
            st.write(":green[Total Transactions] =",Total_trans_count2)
            st.write(":green[Total Transaction amount] =",Total_trans_amount2)
        
        ## Below code will match the State in to GeoJSON id of choropleth to sketch the outline of India map
        dff = pd.DataFrame(
            {
                "State": ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu-&-kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal'],  # fmt: skip
                "Total_Transactions": Total_trans_count1,
                "Total_amount":Total_trans_amount1
            }
        )

        fig = px.choropleth(
        dff,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color="Total_amount",
        hover_name="State",
        hover_data="Total_Transactions",
        color_continuous_scale='Reds',
        title="India Map View"
        )
        # fig.update_layout(
        # plot_bgcolor="#6F36AD",
        # paper_bgcolor="#6F36AD",
        # font=dict(color="violet"),
        # )
        fig.update_geos(fitbounds="locations", visible=False)
        st.write(fig)


    ## Below will be active when they select User from the radio menu
    ## It will work in the same way as when Transactions is selected in Map view
    if trans_user == "User":
        category_agg_users_brand=st.sidebar.multiselect("Brand:",
                                        options=df_agg_user["brand_name"].unique(),
                                        default='Samsung'
                                        )
        category_agg_users_year=st.sidebar.multiselect("Year:",
                                    options=df_agg_user["Year"].unique(),
                                    default=2018
                                    )
        category_agg_users_quarter=st.sidebar.multiselect("Quarter:",
                                options=df_agg_user["Quarter"].unique(),
                                default="1"
                                )


        selection_agg_users = df_agg_user.query(
            "brand_name == @category_agg_users_brand & Year == @category_agg_users_year & Quarter == @category_agg_users_quarter"
        )


        Total_user_count = convert.rupees(str(selection_agg_users["Transacion_count"].sum()))

        Total_user_count1 = (selection_agg_users.groupby("State")["Transacion_count"].sum())
        Total_user_count11 = (selection_agg_users.groupby("brand_name")["Transacion_count"].sum())

        Total_user_count2 = (selection_agg_users.groupby("brand_name")["Transacion_count"].sum().sort_values(ascending=False).head(1))

        Total_user_Brand = Total_user_count2.index[0]
        Total_user_Brand = str(Total_user_Brand).capitalize()
        Total_user_count2 = convert.rupees(str(Total_user_count2[0]))


        col1,col2 = st.columns([1,1],gap="small")
        with col1:
            st.write("#### :orange[Cummulative Total for Transactions]")
            st.write(":green[Overall Transactions] =",Total_user_count)
        with col2:
            st.write("#### :orange[TOP Performed Brand]")
            st.write(":green[Brand Name] =",Total_user_Brand)
            st.write(":green[Total Transactions Performed] =",Total_user_count2)
        
        dff = pd.DataFrame(
            {
                "State": ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu-&-kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal'],  # fmt: skip
                "Total_Transactions": Total_user_count1
            }
        )

        fig = px.choropleth(
        dff,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color="Total_Transactions",
        hover_name="State",
        hover_data="Total_Transactions",
        color_continuous_scale='Reds',
        title="India Map View"
        )
        # fig.update_layout(
        # plot_bgcolor="#6F36AD",
        # paper_bgcolor="#6F36AD",
        # font=dict(color="violet"),
        # )
        fig.update_geos(fitbounds="locations", visible=False)
        st.write(fig)

else:
    st.write("### :violet[Explore More Data to get additional Insight with Visualized Charts]")
    trans_user = st.sidebar.radio(
     "Please select the type",
     ('Transaction', 'User'))

    if trans_user == "Transaction":
        st.write("### :red[Transaction data representation]")
        colum1,colum2= st.columns([1,1.5],gap="large")
        with colum1:
            quarter = st.slider("Quarter", min_value=1, max_value=4)
            st.write(" ")
            st.write(" ")
        
        with colum2:
            year = st.selectbox("**Year**", (2018, 2019, 2020, 2021, 2022, 2023),index=0)
            st.write(" ")
            st.write(" ")

       ## Below code will extract the details from MYSQL as per the user input from the screen
        colum1,colum2= st.columns([1,1],gap="large")
        with colum1:
            try:
                cur.execute(f"""select State, Year, Quarter, sum(Transacion_count) as Total_Transactions, sum(Transacion_amount) as Total_Transaction_amount
                from Aggregate_Transaction where Year = %s and Quarter = %s
                group by State order by Total_Transaction_amount desc limit 5;""",(year,quarter,))
                s1 = cur.fetchall()
                df1 = pd.DataFrame(s1)
                df1.columns = ["State","Year","Quarter","Total_Transactions","Total_Amount"]
                df1["State"] = df1["State"].str.title()
                df1["Total_Transactions"]= df1.apply(lambda x: convert.rupees(str(x.Total_Transactions)),axis=1)
                df1 = df1.sort_values("Total_Amount",ascending=False)
                fig = px.bar(df1,x="State",y="Total_Amount",color="State",hover_name="State",text="Total_Transactions",
                labels={"State":"State List","Total_Amount":"Total Transaction amount"})
                fig.update_layout(
                    width=400,
                    height=400
                )
                fig.update_traces(marker_line_color = 'black',
                        marker_line_width = 2, opacity = 1)
                fig.update_layout(title_text="Top 5 Performed States in INDIA", title_x=0.2,title_font_color="orange")
                st.write(fig)
            except ValueError:
                print( "Q4 is not valid for 2023")

        with colum2:
            try: 
                state = df1["State"].head(1)
                state = state.item()
                cur.execute(f"""select State,Year, Quarter, District_Name, sum(Transacion_count) as Total_Transactions, sum(Transacion_amount) as Total_Transaction_amount
                    from Map_Transaction where State = %s and Year = %s and Quarter = %s
                    group by State, District_Name order by Total_Transaction_amount desc limit 5;""",(state,year,quarter,))
                s2 = cur.fetchall()
                df2 = pd.DataFrame(s2)
                df2.columns = ["State","Year","Quarter","District Name","Total Transactions","Total Amount"]
                df2["District Name"] = df2["District Name"].str.title()
                fig = px.pie(df2,labels="District Name",names="District Name",values="Total Amount",hover_data="Total Transactions",color_discrete_sequence=px.colors.sequential.Sunset,width=600,height=400)
                fig.update_layout(title_text="Percentage Contribution of Top 5 Districts in "+state, title_x=0.1,title_font_color="orange")
                fig.update_traces(textinfo="percent + value",marker_line_color = 'black',
                        marker_line_width = 2, opacity = 1,pull=[0,0,0,0,0.2])
                st.write(fig)
            except:
                pass

        colum1,colum2= st.columns([1,1],gap="large")
        with colum1:
            st.write(" ")
            try:
                cur.execute(f"""select State,Year, Quarter, City_Name, sum(Transacion_count) as Total_Transactions, sum(Transacion_amount) as Total_Transaction_amount
                    from Top_Transaction_District where State = %s and Year = %s and Quarter = %s
                    group by State, City_Name order by Total_Transaction_amount desc limit 5;""",(state,year,quarter,))
                s3 = cur.fetchall()
                df3 = pd.DataFrame(s3)
                df3.columns = ["State","Year","Quarter","City Name","Total_Transactions","Total_Amount"]
                df3["City Name"] = df3["City Name"].str.title()
                df3["Total_Transactions"] = df3.apply(lambda x: convert.rupees(str(x.Total_Transactions)),axis=1)
                fig = px.bar(df3,x="City Name",y="Total_Amount",color="City Name",hover_name="State",text="Total_Transactions",
                            labels={"City Name":"City List","Total_Amount":"Total Transaction amount"})
                fig.update_layout(
                    width=400,
                    height=400
                )
                fig.update_traces(marker_line_color = 'black',
                        marker_line_width = 2, opacity = 1)
                fig.update_layout(title_text="Top 5 Performed Cities in "+state, title_x=0.2,title_font_color="violet")
                st.write(fig)
            except:
                pass
        with colum2:
            st.write(" ")
            try:
                cur.execute(f"""select State,Year, Quarter, District_Name, sum(Transacion_count) as Total_Transactions, sum(Transacion_amount) as Total_Transaction_amount
                        from Map_Transaction where Year = %s and Quarter = %s
                        group by State, District_Name order by Total_Transaction_amount desc limit 5;""",(year,quarter,))
                s4 = cur.fetchall()
                df4 = pd.DataFrame(s2)
                df4.columns = ["State","Year","Quarter","District Name","Total Transactions","Total Amount"]
                df4["District Name"] = df4["District Name"].str.title()
                fig = px.pie(df4,labels="District Name",names="District Name",values="Total Amount",hover_data="Total Transactions",color_discrete_sequence=px.colors.sequential.Purp,width=600,height=400,hole=0.6)
                fig.update_layout(title_text="Overall Top 5 Performed Districts in INDIA ", title_x=0.1,title_font_color="violet")
                fig.update_traces(textinfo="percent + value",marker_line_color = 'black',
                        marker_line_width = 3, opacity = 1)
                st.write(fig)
            except:
                pass
    
    ## Below else part will be active if User is selected from the Radio button. It also uses MYSQL to extract details based on User input from Streamlit
    else:
        st.write("### :red[User data representation]")
        colum1,colum2= st.columns([1,1.5],gap="large")
        with colum1:
            quarter = st.slider("Quarter", min_value=1, max_value=4)
            st.write(" ")
            st.write(" ")
        
        with colum2:
            year = st.selectbox("**Year**", (2018, 2019, 2020, 2021, 2022, 2023),index=0)
            st.write(" ")
            st.write(" ")

       ## Below will plot the Bar chart
        try:
            cur.execute(f"""select State, Year, Quarter, brand_name, sum(Transacion_count) as Total_Transactions
                    from Aggregate_Users where Year = %s and Quarter = %s
                    group by State, brand_name order by Total_Transactions desc limit 20;""",(year,quarter,))
            s1 = cur.fetchall()
            df1 = pd.DataFrame(s1)
            df1.columns = ["State","Year","Quarter","brand_name","Total_Transactions"]
            df1["brand_name"] = df1["brand_name"].str.title()
            df1["State"] = df1["State"].str.title()
            df1["Total_d1"] = df1.apply(lambda x: convert.rupees(str(x.Total_Transactions)),axis=1)
            fig = px.bar(df1,x="State",y="Total_Transactions",color="brand_name",barmode="group",
                labels={"brand_name":"Brand Name","Total_Transactions":"Total Transaction done"})
            fig.update_layout(
                width=800,
                height=600
            )
            fig.update_traces(marker_line_color = 'black',
                    marker_line_width = 2, opacity = 1)
            fig.update_layout(title_text="Top Brands Performed Transactions in INDIA", title_x=0.3,title_font_color="orange")
            st.write(fig)
        except:
            pass
        st.write(" ")

        ## Below will plot the Bar chart
        try:
            cur.execute(f"""select State, Year, Quarter, sum(registered_users) as Total_Regsitered_users, sum(Total_appOpens) as Total_appOpens
                    from Map_Users where Year = %s and Quarter = %s
                    group by State order by Total_Regsitered_users desc limit 10;""",(year,quarter,))
            s2 = cur.fetchall()
            df2 = pd.DataFrame(s2)
            df2.columns = ["State","Year","Quarter","Total_Registered_Users", "Total_App_Opens"]
            df2["State"] = df2["State"].str.title()
            df2["Total_App_Opens"] = df2.apply(lambda x: convert.rupees(str(x.Total_App_Opens)),axis=1)
            fig = px.bar(df2,x="State",y="Total_Registered_Users",color="Total_App_Opens")
            fig.update_layout(
                width=600,
                height=400
            )
            fig.update_traces(marker_line_color = 'black',
                    marker_line_width = 2, opacity = 1)
            fig.update_layout(title_text="Top 5 States having more Registered Users", title_x=0.3,title_font_color="orange")
            st.write(fig)
        except:
            pass
        st.write(" ")

        ## Below will plot the pie chart
        try:
            cur.execute(f"""select State, Year, Quarter,District_name, sum(registered_users) as Total_Regsitered_users
                    from Top_Users_District where Year = %s and Quarter = %s
                    group by State, District_name order by Total_Regsitered_users desc limit 5;""",(year,quarter,))
            s3 = cur.fetchall()
            df3 = pd.DataFrame(s3)
            df3.columns = ["State","Year","Quarter","District Name","Total Registered Users"]
            df3["District Name"] = df3["District Name"].str.title()
            fig = px.pie(df3,labels="District Name",names="District Name",values="Total Registered Users",hover_data="Total Registered Users",color_discrete_sequence=px.colors.sequential.Rainbow,width=600,height=500)
            fig.update_layout(title_text="Top 5 Districts having more registered Users in INDIA ", title_x=0.1,title_font_color="orange")
            fig.update_traces(textinfo="percent + value",marker_line_color = 'black',
                    marker_line_width = 3, opacity = 1,pull=(0.25,0,0,0,0))
            st.write(fig)
        except:
            pass
