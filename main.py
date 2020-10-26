#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

 #Reading data from csv dataset
data = pd.read_csv('googleplaystore.csv')

def app1():
    data = pd.read_csv('googleplaystore.csv')
    """
    App with the largest number of installs
    """
    data['Installs'] = data['Installs'].apply(lambda x : x.strip('+').replace(',', ''))
    i = data[data['Category'] == '1.9'].index
    data.loc[i]
    data = data.drop(i)
    data['Installs'] = data['Installs'].astype(int)
    res = data.groupby('App')['Installs'].sum().reset_index()
    final_result = res.sort_values(by = 'Installs', ascending = False).head(10)
    plt.bar("App", "Installs", data = final_result, color = "blue")
    plt.xlabel("Apps")
    plt.xticks(rotation = 90)
    plt.ylabel("Install Counts")
    plt.title("Top 10 Apps having Highest Installs")
    plt.show()
def app2():
    store = pd.read_csv('googleplaystore.csv')
    store.Size = store.Size.replace("Varies with device",np.nan)
    store.Size = store.Size.str.replace("M","000")
    store.Size = store.Size.str.replace("k","")
    store.Size = store.Size.replace("1,000+",1000)
    store.Installs = store.Installs.str.replace(",","")
    store.Installs = store.Installs.apply(lambda x: x.strip("+"))
    store.Installs = store.Installs.replace("Free",np.nan)
    store.Price = store.Price.str.replace("$","")
    store = store.drop(store.index[10472])
    store[["Size","Installs","Reviews","Price"]] = store[["Size","Installs","Reviews","Price"]].astype("float")
    store.Category = store.Category.astype("category")
    store.Installs = pd.to_numeric(store.Installs)
    store.Price = pd.to_numeric(store.Price)
    store = store.drop_duplicates(subset = "App", keep = "first")
    free = store[store.Type == "Free"]
    paid = store[store.Type == "Paid"]
    # We can comprasion free and paid app reviews
    free.Reviews.plot(kind = "line", color = "g", linestyle = ":", alpha = .7, 
          grid = True, linewidth = 1, figsize = (12,6), label = "Free")
    paid.Reviews.plot(kind = "line", color = "r", linestyle = "-.", alpha = 1, 
          grid = True, linewidth = 1, figsize = (12,6), label = "Paid")
    plt.legend()
    plt.xlabel("İndex")
    plt.ylabel("Reviews")
    plt.title("Free-Paid")
    plt.show()
def app3():
    store = pd.read_csv('googleplaystore.csv')
    store.Size = store.Size.replace("Varies with device",np.nan)
    store.Size = store.Size.str.replace("M","000")
    store.Size = store.Size.str.replace("k","")
    store.Size = store.Size.replace("1,000+",1000)
    store.Installs = store.Installs.str.replace(",","")
    store.Installs = store.Installs.apply(lambda x: x.strip("+"))
    store.Installs = store.Installs.replace("Free",np.nan)
    store.Price = store.Price.str.replace("$","")
    store = store.drop(store.index[10472])
    store[["Size","Installs","Reviews","Price"]] = store[["Size","Installs","Reviews","Price"]].astype("float")
    store.Category = store.Category.astype("category")
    store.Installs = pd.to_numeric(store.Installs)
    store.Price = pd.to_numeric(store.Price)
    store = store.drop_duplicates(subset = "App", keep = "first")
    free = store[store.Type == "Free"]
    paid = store[store.Type == "Paid"]
    store.Rating.plot(kind = "hist", bins = 50, figsize = (12,6))
    plt.xlabel("Rating")
    plt.title("Rating of Distribution")
    plt.show()
def app4():
    store = pd.read_csv('googleplaystore.csv')
    store.Size = store.Size.replace("Varies with device",np.nan)
    store.Size = store.Size.str.replace("M","000")
    store.Size = store.Size.str.replace("k","")
    store.Size = store.Size.replace("1,000+",1000)
    store.Installs = store.Installs.str.replace(",","")
    store.Installs = store.Installs.apply(lambda x: x.strip("+"))
    store.Installs = store.Installs.replace("Free",np.nan)
    store.Price = store.Price.str.replace("$","")
    store = store.drop(store.index[10472])
    store[["Size","Installs","Reviews","Price"]] = store[["Size","Installs","Reviews","Price"]].astype("float")
    store.Category = store.Category.astype("category")
    store.Installs = pd.to_numeric(store.Installs)
    store.Price = pd.to_numeric(store.Price)
    store = store.drop_duplicates(subset = "App", keep = "first")
    free = store[store.Type == "Free"]
    paid = store[store.Type == "Paid"]
    store.Category.value_counts().plot(kind='barh',figsize= (12,8))   
    plt.show()
def app6():
    data = pd.read_csv('googleplaystore.csv')
    data.Category.value_counts().plot(kind='pie')
    plt.show()
def app7():
    #read_csv load data
    data = pd.read_csv('googleplaystore.csv')
    fig, ax = plt.subplots()
    ax.scatter(x = data.groupby('Category')['Rating'].mean()[1:].index, y = data.groupby('Category')['Rating'].mean()[1:].values)
    plt.ylabel('Category', fontsize=13)
    plt.xlabel('Rating', fontsize=13)
    plt.xticks(rotation=90)
    plt.show()
def app8():
    data = pd.read_csv('googleplaystore.csv')
    data.Installs=data.Installs.apply(lambda x: x.strip('+'))
    data.Installs=data.Installs.apply(lambda x: x.replace(',',''))
    data.Installs=data.Installs.replace('Free',np.nan)
    data.Installs=pd.to_numeric(data.Installs)
    data.Installs=pd.to_numeric(data.Installs)
    data.Installs.hist();
    plt.xlabel('No. of Installs')
    plt.ylabel('Frequency')
    plt.show()
def no_index():
    print("Reading Complete File without index")
    df=pd.read_csv("googleplaystore.csv",index_col=0)
    print(df)
def read():
    df=pd.read_csv("googleplaystore.csv")
    print(df)
def menu():
    print("""
    1.Data Visualization
    2.Read CSV Data 
    3.Data Manipulation
    4.Exit
    """)
    a=input("Enter Your Choice : ")
    if a=="1":
        datavisualization()
    elif a=="2":
        readdatafromfile()
    elif a=="3":
        datamanipulation()
    elif a=="4":
        exit()
    else:
        print("Error")
def datavisualization(): 
    print("""Data Visualization
    1.Top 10 Apps Having Highest Installs(Bar Graph)
    2.Comparison of Reviews of Paid and Free Apps(Line Chart)
    3.Rating Of Distibution(Histogram)
    4.Distribution of App Categories(Bar Graph)
    5.Free v/s Paid(Pie Chart)
    6.Categories(Pie Chart)
    7.Rating-Category(Scatter Chart)
    8.Installs(Histogram)
    9.Current Version Updated(Bar Graph)
    10.Android Versions(Bar Graph)
    11.Content Ratings(Bar Graph)
    12.Content Ratings(Pie Chart)
    13.Categories(Line Chart)
    14.Content Ratings(Line Chart)
    """)
    x=input("Enter Your Choice :")
    if x=="1":
        app1()
    elif x=="2":
        app2()
    elif x=="3":
        app3()
    elif x=="4":
        app4()
    elif x=="6":
        app6()
    elif x=="5":
        app5()
    elif x=="7":
        app7()
    elif x=="8":
        app8()
    elif x=="9":
        app9()
    elif x=="10":
        app10()
    elif x=="11":
        app11()
    elif x=="12":
        app12()
    elif x=="13":
        app13()
    elif x=="14":
        app14()
    else:
        print("Error")
def readdatafromfile():
    print("""
    1.Reading Complete File without Index
    2.Read Complete CSV File
    """)
    b=input("Enter Your Choice :")
    if b=="1":
        no_index()
    elif b=="2":
        read()
def datamanipulation():
    print("""
    Data Maniputlation
    1.Sorting the Data as per your choice
    2.Read Top and Bottom Records from file as per requiremnt
    3.Make the copy of CSV file
    4.Read the Specific Columns
    """)
    c=input("Enter Your Choice  :")
    if c=="2":
        top_bottom_selected_records()
    elif c=="3":
        duplicate()
    elif c=="4":
        specific_col()
    elif c=="1":
        datasort()
    else:
        print("Error")
def top_bottom_selected_records():
    df=pd.read_csv("googleplaystore.csv")
    top=int(input("How many records to display from top:  "))
    print("First",top,"Records")
    print(df.head(top))
    bottom=int(input("How mant records to display from Bottom:"))
    print("Last",bottom,"Records")
    print(df.tail(bottom))
def duplicate():
    print("Duplicate the file with new file")
    df=pd.read_csv("googleplaystore.csv")
    df.to_csv("googleplaystorenew.csv")
    print("Data from the new file")
    print(df)
def specific_col():
    print("Reading Specific column from  CSV file")
    df=pd.read_csv("googleplaystore.csv",usecols=['App','Rating','Type'],index_col=0)
    print(df)
def datasort():
    df=pd.read_csv("googleplaystore.csv")
    print("""
    1.Press to 1 arrange the record as per the App Name
    2.Press to 2 arrange the record as per the App Category 
    3.Press to 3 arrange the record as per the Ratings
    4.Press to 4 arrange the record as per the Reviews
    5.Press to 5 arrange the record as per the Size
    6.Press to 6 arrange the record as per the Installs
    7.Press to 7 arrange the record as per the Type
    8.Press to 8 arrange the record as per the Price
    9.Press to 9 arrange the record as per the Content Ratings
    10.Press to 10 arrange the record as per the Genres
    11.Press to arrange the record as per the Last Update
    12.Press to arrange the record as per the Current Version
    13.Press to arrange the record as per the Android Version
    """)

    ab=input("Enter Your Choice :")

    if ab=="1":
        df.sort_values(["App"])
        print(df)
    elif ab=="2":
        df.sort_values(["Category"],inplace=True)
        print(df)
    elif ab=="3":
        df.sort_values(["Rating"],inplace=True)
        print(df)
    elif ab=="4":
        df.sort_values(["Reviews"],inplace=True)
        print(df)
    elif ab=="5":
        df.sort_values(["Size"],inplace=True)
        print(df)
    elif ab=="6":
        df.sort_values(["Installs"],inplace=True)
        print(df)
    elif ab=="7":
        df.sort_values(["Type"],inplace=True)
        print(df)
    elif ab=="8":
        df.sort_values(["Price"],inplace=True)
        print(df)
    elif ab=="9":
        df.sort_values(["Content Rating"],inplace=True)
        print(df)
    elif ab=="10":
        df.sort_values(["Genres"],inplace=True)
        print(df)
    elif ab=="11":
        df.sort_values(["Last Updated"],inplace=True)
        print(df)
    elif ab=="12":
        df.sort_values(["Current Ver"],inplace=True)
        print(df)
    elif ab=="13":
        df.sort_values(["Android Ver"],inplace=True)
        print(df)
def app5():
    data = pd.read_csv('googleplaystore.csv')
    explode=[0,0.1]
    labels=["Free","Paid"]
    plt.figure(figsize=(5,5))
    plt.pie(data[data['Genres']=='Tools'].Type.value_counts().values,labels=data[data['Genres']=='Tools'].Type.value_counts().index,explode=explode, autopct='%1.1f%%')
    plt.title("Free v/s Paid Apps")
    plt.show()
def app9():
    data = pd.read_csv('googleplaystore.csv')
    temp=data.Current_Ver.replace(np.nan,'Varies with device')
    temp=temp.apply(lambda x: 'Varies with device' if x=='Varies with device'  else  re.findall('^[0-9]\.[0-9]|[\d]|\W*',str(x))[0] )
    data['Current_Ver_updated']=temp
    data.Current_Ver_updated.value_counts().plot(kind="barh", figsize=(15,15));
    plt.legend(bbox_to_anchor=(1.0,1.0))
    plt.xscale('log')
    plt.show()
def app10():
    data = pd.read_csv('googleplaystore.csv')
    data['Version_begin']=data.Android_Ver.apply(lambda x:str(x).split(' and ')[0].split(' - ')[0])
    data.Version_begin=data.Version_begin.replace('4.4W','4.4')
    data['Version_end']=data.Android_Ver.apply(lambda x:str(x).split(' and ')[-1].split(' - ')[-1])
    twowaytable = pd.crosstab(index=data.Version_begin,columns=data.Version_end)
    twowaytable.plot(kind="barh", figsize=(15,15),stacked=True);
    plt.legend(bbox_to_anchor=(1.0,1.0))
    plt.xscale('log')
    plt.show()
def app11():
    data = pd.read_csv('googleplaystore.csv')
    data.Content_Rating.value_counts().plot(kind='bar')
    plt.yscale('log')
    plt.show()
def app12():
    data = pd.read_csv('googleplaystore.csv')
    data.Content_Rating.value_counts().plot(kind='pie')
    plt.show()
def app13():
    data = pd.read_csv('googleplaystore.csv')
    data.Category.value_counts().plot(kind='line')
    plt.show()
def app14():
    data = pd.read_csv('googleplaystore.csv')
    data.Content_Rating.value_counts().plot(kind='line')
    plt.show()











menu()



