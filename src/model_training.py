from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data/synthetic_data.csv')
le = LabelEncoder()
df['appliance_encoded'] = le.fit_transform(df['appliance'])

X = df[['vibration', 'temperature', 'current', 'appliance_encoded']]
y = df['needs_service']

model = RandomForestClassifier()
model.fit(X, y)

with open('src/model.pkl', 'wb') as f:
    pickle.dump(model, f)
