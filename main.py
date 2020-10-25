#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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
def app5():
    data= pd.read_csv('googleplaystore.csv')
    plt.figure(figsize=(20,7))
    sns.countplot(data['Content Rating'])
    plt.xticks(rotation=-90)
    plt.show()
def app6():
    df = pd.read_csv('googleplaystore.csv')
    df_reviews = pd.read_csv('googleplaystore_user_reviews.csv')
    df['Rating'].fillna((df['Rating'].mean()), inplace=True)
    df1 = df.dropna()
    df1[df1.duplicated(['App'])]
    df1[df1['App']=="Quick PDF Scanner + OCR FREE"]
    df1.sort_values(by=['Reviews'], inplace=True)
    df2 = df1.drop_duplicates(keep='last',subset=['App'])
    df2['Installs'].unique()
    #Converting the Installs number into float value and copying in a different column
    df2['Installs_num'] = df2['Installs'].apply(lambda x: float(x.split("+")[0].replace(",","")))
    df2['Installs_num'].unique()
    df2['Price'].unique()
    #converting the price into float values
    df2['Price_USD'] = df2['Price'].apply(lambda x: float(x.replace("$","")))
    df2['Price_USD'].unique()
    #Converting reviews count into int
    df2['Reviews_count']= df1['Reviews'].apply(lambda x: int(x))
    df2['Size'].replace('Varies with device',np.nan,inplace=True)
    df2["Size"] = (df2["Size"].replace(r'[kM]+$', '', regex=True).astype(float) * df2["Size"].str.extract(r'[\d\.]+([kM]+)', expand=False).fillna(1).replace(["k","M"], [10**3, 10**6]).astype(int))
    df2["Android Ver"].replace('Varies with device',np.nan,inplace=True)
    df2['Size'].fillna((df2['Size'].mean()), inplace=True)
    #Our final data frame with all the extra values removed
    df3 = df2.drop(['Reviews','Installs','Price','Android Ver'],axis='columns')

    fig = plt.figure(figsize=(16,8)) 
    labels = df3['Category'].value_counts(sort = True).index
    sizes = df3['Category'].value_counts(sort = True)
    plt.pie(sizes,labels=labels,autopct='%1.1f%%', shadow=True)
    plt.title('Top categories',size = 20)
    plt.legend(labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
def no_index():
    print("Reading Complete File without index")
    df=pd.read_csv("googleplaystore.csv",index_col=0)
    print(df)
def new_column_name():
    print("Adding new column name to existing Data")
def read():
    df=pd.read_csv("googleplaystore.csv")
    print(df)
def menu():
    a=input("""
    1.Data Visualization
    2.Read CSV Data 
    3.Data Manipulation
    4.Exit
    """)
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
    x=input("""
    Data Visualization
    1.Top 10 Apps Having Highest Installs
    2.Comparison of Reviews of Paid and Free Apps
    3.Rating Of Distibution
    4.Distribution of App Categories
    5.Content Rating
    6.Top Categories

    """)
    if x=="1":
        app1()
    elif x=="2":
        app2()
    elif x=="3":
        app3()
    elif x=="4":
        app4()
    elif x=="5":
        app5()
    elif x=="6":
        app6()
    else:
        print("Error")
def readdatafromfile():
    b=input("""
    1.Reading Complete File without Index
    2.Read Complete CSV File
    """)
    if b=="1":
        no_index()
    elif b=="2":
        read()
def datamanipulation():
    c=input("""
    Data Maniputlation
    1.Sorting the Data as per your choice
    2.Read Top and Bottom Records from file as per requiremnt
    3.Make the copy of CSV file
    4.Read the Specific Columns
    """)
    if c=="2":
        top_bottom_selected_records()
    elif c=="3":
        duplicate()
    elif c=="4":
        specific_col()
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

menu()
