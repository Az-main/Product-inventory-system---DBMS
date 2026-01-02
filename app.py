import streamlit as st
from product_management import create_product, get_all_products, update_product, delete_product

# Page Configuration
st.set_page_config(
    page_title="Product Inventory System",
    page_icon="📦",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-msg {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 5px;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📋 Navigation")
page = st.sidebar.radio("Select Module", ["🏠 Home", "📦 Product Inventory"])

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.markdown("<h1 class='main-header'>📦 Product Inventory System</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### Welcome to the Product Inventory System!")
    st.write("This application allows you to manage **Products** efficiently.")
    
    st.info("### 📦 Product Inventory Features\n- Add new products\n- View all products\n- Update product details\n- Remove products")
    
    st.markdown("---")
    st.write("**👈 Select 'Product Inventory' from the sidebar to get started!**")

# ==================== PRODUCT INVENTORY ====================
elif page == "📦 Product Inventory":
    st.markdown("<h1 class='main-header'>📦 Product Inventory</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Tabs for different operations
    tab1, tab2, tab3 = st.tabs(["➕ Add Product", "📋 View Products", "✏️ Update/Delete"])
    
    # ADD PRODUCT TAB
    with tab1:
        st.subheader("Add New Product")
        with st.form("add_product_form"):
            name = st.text_input("Product Name")
            description = st.text_area("Description")
            price = st.number_input("Price ($)", min_value=0.0, step=0.01)
            quantity = st.number_input("Quantity", min_value=0, step=1)
            submitted = st.form_submit_button("Add Product", type="primary")
            
            if submitted:
                if name and price >= 0:
                    try:
                        create_product(name, description, price, quantity)
                        st.success(f"✅ Product '{name}' added successfully!")
                    except Exception as e:
                        st.error(f"❌ Error: {e}")
                else:
                    st.warning("⚠️ Please fill required fields (Name, Price)!")
    
    # VIEW PRODUCTS TAB
    with tab2:
        st.subheader("All Products")
        if st.button("🔄 Refresh", key="refresh_products"):
            st.rerun()
        
        try:
            products = get_all_products()
            if products:
                st.table({
                    "ID": [p[0] for p in products],
                    "Name": [p[1] for p in products],
                    "Description": [p[2] for p in products],
                    "Price ($)": [f"${p[3]:.2f}" for p in products],
                    "Quantity": [p[4] for p in products],
                    "Created At": [p[5] for p in products]
                })
            else:
                st.info("No products found in the database.")
        except Exception as e:
            st.error(f"❌ Database Error: {e}")
    
    # UPDATE/DELETE TAB
    with tab3:
        st.subheader("Update or Delete Product")
        
        try:
            products = get_all_products()
            if products:
                product_options = {f"{p[0]} - {p[1]}": p[0] for p in products}
                selected_product = st.selectbox("Select Product", list(product_options.keys()))
                product_id = product_options[selected_product]
                
                # Get current product data
                current_product = [p for p in products if p[0] == product_id][0]
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("#### ✏️ Update Product")
                    with st.form("update_product_form"):
                        new_name = st.text_input("Product Name", value=current_product[1])
                        new_description = st.text_area("Description", value=current_product[2] or "")
                        new_price = st.number_input("Price ($)", value=float(current_product[3]), min_value=0.0, step=0.01)
                        new_quantity = st.number_input("Quantity", value=int(current_product[4]), min_value=0, step=1)
                        update_btn = st.form_submit_button("Update Product", type="primary")
                        
                        if update_btn:
                            try:
                                update_product(product_id, new_name, new_description, new_price, new_quantity)
                                st.success("✅ Product updated successfully!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Error: {e}")
                
                with col2:
                    st.write("#### 🗑️ Delete Product")
                    st.warning("⚠️ This action cannot be undone!")
                    if st.button("Delete Product", type="secondary", key="delete_product"):
                        try:
                            delete_product(product_id)
                            st.success("✅ Product deleted successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Error: {e}")
            else:
                st.info("No products found to update or delete.")
        except Exception as e:
            st.error(f"❌ Database Error: {e}")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("📌 **Product Inventory**\nBuilt with Streamlit & MySQL")
