import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Affiliate Expert", layout="wide")

# Header Section
st.title("Affiliate Expert")
st.subheader("Your Guide to Successful Affiliate Marketing")

# Introduction Section
st.write("""Welcome to Affiliate Expert, your go-to resource for learning and excelling in affiliate marketing. Whether you're a beginner or an experienced marketer, we provide insights, tools, and recommendations to help you maximize your earnings.""")

# Niche Selection Section
st.header("1. Choose Your Niche")
st.write("""Start by selecting a niche that aligns with your interests and market demand. Below are some popular niches:""")
niches = ["Technology", "Fashion", "Fitness", "Travel", "Finance", "Home & Garden"]
selected_niche = st.selectbox("Select your niche:", niches)

if selected_niche:
    st.write(f"Sailaja You have selected **{selected_niche}**. Here's why it's a great choice:")

    # Add niche-specific content here
    if selected_niche == "Technology":
        st.write("Technology is an ever-growing field with constant innovations. You can promote gadgets, software, and more.")
    elif selected_niche == "Fashion":
        st.write("Fashion is always in demand. From clothing to accessories, the opportunities are endless.")

# Affiliate Programs Section
st.header("2. Join Affiliate Programs")
st.write("""After choosing your niche, the next step is to join relevant affiliate programs. Here are some popular options:""")
programs = ["Amazon Associates", "Flipkart Affiliate", "vCommission", "CJ Affiliate"]
for program in programs:
    st.markdown(f"- **{program}**: [Join here](#)")

# Content Creation Section
st.header("3. Create Quality Content")
st.write("""Creating valuable content is key to your success in affiliate marketing. Focus on writing reviews, tutorials, and guides that help your audience make informed decisions.""")

# Traffic Generation Section
st.header("4. Drive Traffic to Your Platform")
st.write("""Use SEO, social media, and email marketing to drive traffic to your website. The more targeted traffic you have, the higher your chances of earning commissions.""")

# Footer
st.write("---")
st.write("© 2024 Affiliate Expert | Your guide to affiliate marketing success.")

# Contact Information
st.header("Get in Touch")
st.write("If you have any questions, feel free to reach out to us:")
st.write("Email: info@affiliateexpert.com")
