import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating function to open and read the csv file
def load_data():
    try:
        df=pd.read_csv("Student_Marks.csv")
        print("Data loaded successfully!!")
        return df
    except FileNotFoundError:
        print("CSV file not found")
    except Exception as e:
        print(f"Error {e}")

# Creating function to calculate the average mark of each subject
def calculate_average(df):
    subjects=df.columns[1:]
    average={}

    for sub in subjects:
        avg=df[sub].mean()
        average[sub]=avg

    print("subject wise averages:")
    for sub,avg in average.items():
        print(f"{sub}: {round(avg, 2)}")

# Creating function to find the topper in specific subject
def find_toppers(df):
    subjects=df.columns[1:]
    for sub in subjects:
        topper = df.loc[df[sub].idxmax()]
        print(f"{sub} Topper: {topper['Name']} ({topper[sub]})")

# Creating function for assigning grades based on their percentage
def assign_grades(df):
    grades=[]

    for index, row in df.iterrows():
        total = row[1:].sum()
        percentage = total / 4

        if percentage>=95:
            grade="A+"
        elif percentage>=90:
            grade="A"
        elif percentage>=85:
            grade="B+"
        elif percentage>=80:
            grade="B"
        elif percentage>=75:
            grade="C+"
        elif percentage>=70:
            grade="C"
        elif percentage>=65:
            grade="D+"
        elif percentage>=60:
            grade="D"
        else:
            grade="Fail"

        grades.append(grade)
    
    df["Grade"] = grades

# creating function thats helpful for plotting graph
def plot_graph(df):
    subjects=df.columns[1:5]
    averages=df[subjects].mean()

    plt.figure()
    plt.bar(averages.index,averages.values)
    plt.title("Average Marks Per Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.show()

# Main program

df = load_data()

if df is not None:
    calculate_average(df)
    find_toppers(df)
    assign_grades(df)
    plot_graph(df)

    print("\n📄 Final Data:\n")
    print(df)






    

        




        

    




    