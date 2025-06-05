# E-Commerce-Data-Analysis-using-Python
 
## Objective

To perform an end-to-end exploratory data analysis (EDA) on an e-commerce dataset to understand customer behavior, sales trends, returns, payment modes, and product performance using Python.

## Goal

1.Clean and preprocess raw e-commerce data

2.Uncover patterns using univariate and bivariate analysis

3.Visualize key trends and customer behavior

4.Identify high-performing products and top customers

5.Analyze return and discount trends

## Dataset

The dataset contains e-commerce order data with the following columns:
Order_ID, Customer_Name, Email, Order_Date, Delivery_Date, Product_Category, Product_Name, Price, Quantity, Total_Amount, Discount (%), Final_Amount, Payment_Mode, Shipping_Address, Order_Status, Review_Rating, Return_Status

## Tools Used

1.Python

2.Pandas

3.Matplotlib

4.Seaborn

5.Jupyter Notebook

6.Excel (for initial raw data)

## Process
1. Data Import & Cleaning

Imported data using pandas.read_excel()

Removed null values and cleaned Email column by extracting names

Standardized inconsistent Payment_Mode entries

Dropped unnecessary columns like Email and Shipping_Address

## Analysis

🔹 Univariate Analysis

Order Status Distribution:

Delivered: 3,319

Cancelled: 3,245

Pending: 3,244

##Product Category Distribution:

Highest:Electronics: 1,125

Followed by:Toys: 1,120

Least:Clothing: 1,035

🔹 Bivariate Analysis

Product Category vs Final Amount:

Highest: Furniture

Followed by: Electronics and Toys

Lowest: Fitness

Payment Mode Preference:

Most Used: Credit Card

Then: UPI Payment

Least Used: Net Banking

Discount (%) vs Final Amount:

5% Discounts → Highest final amount

Followed by 10% and 20%

Top 10 Customers by Final Amount:

Noah Wilson

Charlotte Green

Liam Martin

Olivia Anderson

Sophia Thomas

Emma Lee

James Brown

Ava Garcia

Lucas Martinez

William Johnson

Return Rate:

Returned: 56.84%

Not Returned: 43.15%

🔹 Correlation Analysis

A heatmap was created to analyze correlations between numeric features.

Key Observations:

Strong correlation between Total_Amount and Final_Amount

Moderate correlation between Price and Final_Amount

Other features show minimal correlation

## Conclusion

1.Electronics and Toys are the most frequently purchased categories

2.Most orders were paid using Credit Cards and UPI

3.Discount strategies at 5% and 10% are driving more revenue

4.High return rate (~57%) could affect profit margins

5.Price and quantity significantly impact sales value

## Recommendations

Reduce return rates by analyzing reasons and improving quality

Boost Furniture category through promotions — it's high-value

Offer loyalty perks to top customers to improve retention

Focus marketing on popular payment methods like Credit Card and UPI

Test pricing and discount strategies to maximize Final Amount

