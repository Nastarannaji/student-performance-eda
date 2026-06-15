import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load data
df = pd.read_csv("data/StudentsPerformance.csv")

# --------------------
# BASIC UNDERSTANDING
# --------------------
print(df.head())
print(df.info())
print(df.sample(5))

# --------------------
# DATA QUALITY CHECKS
# --------------------

# Missing values
print("Missing values:\n", df.isnull().sum())

# Duplicates
print("Duplicates:", df.duplicated().sum())

# Category consistency checks
print(df["gender"].value_counts())
print(df["race/ethnicity"].value_counts())
print(df["parental level of education"].value_counts())
print(df["lunch"].value_counts())
print(df["test preparation course"].value_counts())

# Numerical summary
print(df.describe())


# --------------------
#exploratory data analysis (EDA)
# --------------------

print(df["math score"].describe())
print(df["reading score"].describe())
print(df["writing score"].describe())

df["average score"]=(df["math score"] + df["reading score"] + df["writing score"]) / 3



# --------------------
#visual distribution 
# --------------------

sns.histplot(df["average score"], bins=29 )
plt.title("distribution of average student scores")
plt.savefig("distribution of average score")
plt.close()

sns.barplot(x="gender", y="average score", data=df)
plt.title("Gender vs Average Score")
plt.savefig("gender_vs_average_score.png")
plt.close()

sns.barplot(x="test preparation course" , y="average score" , data=df)
plt.title("test_prep_vs_score")
plt.savefig("test_prep_vs_score.png")
plt.close()

sns.barplot(x="parental level of education" ,y="average score", data=df)
plt.title("parental_education_vs_score")
plt.savefig("parental_education_vs_score")
plt.close()

# --------------------
#QUERIES 
# --------------------

print(df.groupby("lunch")["average score"].mean())
print(df.groupby("parental level of education")["average score"].mean() )
print(df.groupby("race/ethnicity")["average score"].mean())
print(df.groupby("gender")["average score"].mean() )
print(df.groupby("test preparation course")["average score"].mean())