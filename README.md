Product Management Application

This is a web-based Product Management Application that allows customer users to register, sign in, and manage their product listings. The application provides a user-friendly interface for customers to add, edit, and view their products along with product details and images.

Features

User Registration and Sign In

Users can register with the application by providing their First Name, Last Name, Email ID (unique), and Password.
Registered users can sign in using their Email ID and Password.

Dashboard

Upon successful sign-in, customers are redirected to the dashboard page.
The dashboard is login protected, ensuring only authenticated users can access it.
Navigation elements are available to provide easy access to different sections of the application.


Change Password

Authenticated users can change their passwords for added security.
Users need to provide their Current Password, New Password, and Confirm Password to change their password.
Product List

Customers can view a list of products they have added.
Each product entry displays the Product Name, Price, SKU, and Description.

Add New Product
Customers can easily add a new product by clicking the "Add Product" button.
They can enter the Product Name, Price, SKU, and Description for the new product.
Product Images

Users can upload product images while adding a new product.
A maximum of 5 images can be uploaded for each product.
Each image must not exceed 5MB in size.

Edit Product

Authenticated users can edit the product details for products they have added.
They can modify the Product Name, Price, SKU, and Description for the existing product.
Images for the product can also be updated, following the same limitations as during product addition.

View Product Details

Customers can view detailed information about each product they have added.
The product details include the Product Name, Price, SKU, Description, and associated images.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Django
Database: MYSQL


Getting Started
Clone the repository.
Set up the backend and database as per the configuration provided in the project.
Deploy the application on a web server (e.g., Apache, Nginx) and make sure the backend is up and running.
Access the application in your web browser using the server URL.


How to Use
Register: Sign up with the application using your First Name, Last Name, Email ID, and Password.
Sign In: Log in using your registered Email ID and Password to access the dashboard.
Dashboard: Navigate through the dashboard to manage your products, change your password, or add new products.
Change Password: From the dashboard, access the "Change Password" section to update your password.
Product List: View a list of products you have added by clicking on the "Product List" section.
Add New Product: Click on the "Add Product" button from the dashboard to add a new product with details and images.
Edit Product: Go to the "Product List," find the product you wish to edit, and click on the "Edit" button to modify the details and images.
View Product Details: To see the detailed information of a particular product, select it from the "Product List."


Notes
This application does not support simultaneous usage by multiple users. It is intended for individual use.
Please ensure that the images you upload do not exceed the size limit mentioned (5MB).
For any issues or feedback, please feel free to create an issue in the GitHub repository.
