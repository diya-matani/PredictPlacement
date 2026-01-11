# train_and_save_model.py
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1) Load & clean data
csv_path = "F:/AI Models/Placement-Predicator/Placement_Data_Full_Class.csv"
df = pd.read_csv(csv_path)
df.drop(['sl_no', 'salary'], axis=1, inplace=True)

# Map target to numeric
# Original 'status' column has 'Placed' and 'Not Placed'
df['status'] = df['status'].map({'Not Placed': 0, 'Placed': 1})

# unify categorical variants
df['gender']   = df['gender'].replace({'M':'Male','F':'Female'})
df['ssc_b']    = df['ssc_b'].replace({'Central Board':'Central','Others':'Others'})
df['hsc_b']    = df['hsc_b'].replace({'Central Board':'Central','Others':'Others'})
df['hsc_s']    = df['hsc_s'].replace({'Other':'Others'})
df['degree_t'] = df['degree_t'].replace({'Sci&Tech':'Sci&Tech','Comm&Mgmt':'Comm&Mgmt','Others':'Others'})
df['workex']   = df['workex'].replace({'Yes':'Yes','No':'No'})

# fill missing mba_p with mean
if df['mba_p'].isna().any():
    df['mba_p'] = df['mba_p'].fillna(df['mba_p'].mean())

# drop any leftover NaNs
df.dropna(inplace=True)

# 2) Split features & target
X = df.drop('status', axis=1)
y = df['status']

# 3) Define preprocessing pipeline
num_cols = X.select_dtypes(include=['int64','float64']).columns.tolist()
cat_cols = ['gender','ssc_b','hsc_b','hsc_s','degree_t','workex','specialisation']

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols),
])

# 4) Build model pipeline with LogisticRegression
clf = Pipeline([
    ("pre", preprocessor),
    ("lr", LogisticRegression(
        class_weight='balanced',
        max_iter=1000,
        random_state=42
    )),
])

# 5) Train-test split and fit
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

clf.fit(X_train, y_train)

# optional: print performance
print(f"Train accuracy: {clf.score(X_train, y_train):.3f}")
print(f"Test  accuracy: {clf.score(X_test, y_test):.3f}")

# 6) Save pipeline
output_path = "placement_pipeline.pkl"
with open(output_path, "wb") as f:
    pickle.dump(clf, f)

print(f"✅ Pipeline trained & saved to {output_path}")
