import streamlit as st
from joblib import load

# Load the trained model
model = load('model.joblib')

# Load the label encoder for district names
label_encoder = load('label_encoder.joblib')

district_names = ['Bagalkot', 'Yadgir', 'Bengaluru City', 'Tumakuru', 'Bengaluru Dist', 'Hassan', 'Mandya', 'Belagavi Dist', 'Chitradurga', 'Shivamogga', 'Mysuru Dist', 'Ramanagara', 'Udupi', 'Uttara Kannada', 'Bidar', 'Mangaluru City', 'Davanagere', 'Vijayapura', 'Chikkamagaluru', 'Dakshina Kannada', 'Mysuru City', 'Haveri', 'Kalaburagi', 'Chickballapura', 'Raichur', 'Kolar', 'Belagavi City', 'Koppal', 'Chamarajanagar', 'Ballari', 'Vijayanagara', 'Dharwad', 'Kodagu', 'Kalaburagi City', 'K.G.F', 'Karnataka Railways', 'Gadag', 'Hubballi Dharwad City']

st.title("Accident Prediction Model")
st.header("Predict Accidents in Karnataka")

district_name = st.selectbox("Select District", district_names)
year = st.number_input("Enter Year", min_value=2025, max_value=2035, value=2025)

if st.button("Predict Accidents"):
    # Encode district name to numerical value using label encoder
    district_id = label_encoder.transform([district_name])[0]

    # Predict accidents for the input district and year
    predicted_accidents = int(model.predict([[district_id, year]]))

    # Display the prediction result
    st.write(f"Predicted Accidents in {district_name} for {year}: {predicted_accidents}")

if __name__ == "__main__":
    st.write("Ready to predict accidents!")
