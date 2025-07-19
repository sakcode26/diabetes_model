import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


file="C:/Users/hp/Downloads/pima-indians-diabetes.csv"
cols=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

df=pd.read_csv(file,names=cols)
print(df.head())

X=df.drop(['Outcome'], axis=1)
y=df['Outcome']

#preprocess and split
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2, random_state=42)

model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)
