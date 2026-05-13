import streamlit as st

st.title("🍕 Pizza Order System")

veg_pizza = {"Margherita": 150, "Farmhouse": 200}
non_veg_pizza = {"Chicken Delight": 250, "Pepperoni": 300}
toppings = {"Olive": 50, "Cheese Blast": 70, "Mushroom": 30}

# Choose category
choice = st.radio("Choose pizza type:", ["Veg", "Non-Veg"])

# Show menu based on choice
if choice == "Veg":
    menu = veg_pizza
else:
    menu = non_veg_pizza

# Select pizza
pizza_name = st.selectbox("Select your pizza:", list(menu.keys()))

# Choose size
size = st.selectbox("Choose size:", ["Small", "Medium", "Large"])

# Choose toppings
selected_toppings = st.multiselect("Choose toppings:", list(toppings.keys()))

# Calculate price
price = menu[pizza_name]

if size == "Medium":
    price += 50
elif size == "Large":
    price += 100

# Add toppings cost
for topping in selected_toppings:
    price += toppings[topping]

# Order button
if st.button("Place Order"):
    st.success(f"Your total bill is ₹{price}")