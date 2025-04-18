import streamlit as st
import db_manager as db
from datetime import datetime

# Inject CSS styles
st.markdown("""
    <style>
    body {
        background-image: linear-gradient(to right, #fceabb, #f8b500);
        background-attachment: fixed;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 15px;
    }
    h1 {
        color: #333;
        font-size: 3rem;
        text-align: center;
    }
    h2 {
        color: #555;
        font-size: 2rem;
        border-bottom: 2px solid #f8b500;
        padding-bottom: 0.5rem;
    }
    .stButton>button {
        background-color: #f8b500;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 1rem;
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    db.create_table()
    st.title("🧥 Clothes Brand Stock Management")

    menu = ["Add Item", "View Inventory", "Update Stock", "Delete Item"]
    choice = st.sidebar.selectbox("📂 Menu", menu)

    if choice == "Add Item":
        st.markdown("### ➕ Add New Clothing Item")
        name = st.text_input("👕 Item Name")
        category = st.selectbox("🗂️ Category", ["T-Shirts", "Jeans", "Jackets", "Shoes", "Others"])
        size = st.selectbox("📏 Size", ["S", "M", "L", "XL", "Free"])
        quantity = st.number_input("🔢 Quantity", min_value=0)
        price = st.number_input("💸 Price", min_value=0.0, step=0.1)
        if st.button("Add"):
            db.add_item(name, category, size, quantity, price, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.success("✅ Item added successfully!")

    elif choice == "View Inventory":
        st.markdown("### 📦 Current Stock")
        items = db.view_items()
        if items:
            for i in items:
                st.markdown(f"""
                    <div style="background-color:#fff2cc; padding:10px; margin:10px 0; border-radius:10px;">
                        <strong>{i[1]}</strong> <br>
                        Category: {i[2]} | Size: {i[3]} | Qty: {i[4]} | ₹{i[5]} <br>
                        <small>Updated: {i[6]}</small>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No items in inventory.")

    elif choice == "Update Stock":
        st.markdown("### 🔁 Update Item Quantity")
        items = db.view_items()
        item_dict = {f"{i[1]} (ID: {i[0]})": i[0] for i in items}
        if item_dict:
            selected = st.selectbox("Select Item", list(item_dict.keys()))
            new_qty = st.number_input("New Quantity", min_value=0)
            if st.button("Update"):
                db.update_quantity(item_dict[selected], new_qty, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                st.success("✅ Quantity updated.")
        else:
            st.warning("⚠️ No items to update.")

    elif choice == "Delete Item":
        st.markdown("### 🗑️ Delete Item")
        items = db.view_items()
        item_dict = {f"{i[1]} (ID: {i[0]})": i[0] for i in items}
        if item_dict:
            selected = st.selectbox("Select Item to Delete", list(item_dict.keys()))
            if st.button("Delete"):
                db.delete_item(item_dict[selected])
                st.success("✅ Item deleted.")
        else:
            st.warning("⚠️ No items to delete.")
    
    st.markdown('</div>', unsafe_allow_html=True)
