# Import MySQL connector library to connect Python with MySQL database
import mysql.connector


# Create a connection between Python application and MySQL database
connection = mysql.connector.connect(

    # This is the IP address of the MySQL container. It allows the Python application running in one container to connect to the MySQL database running in another container.
    host="172.17.0.2",

    # MySQL username used for authentication
    user="shaikh",

    # Password of MySQL user
    password="shaikh123",

    # Database name where we want to store and fetch data
    database="userinfo"
)


# Check whether the connection with MySQL was successful or not
if connection.is_connected():

    # Print message if database connection is successful
    print("Connected to MySQL Database")


# Create cursor object
# Cursor is used to execute SQL queries from Python
cursor = connection.cursor()


# Infinite loop to continuously show the menu until user chooses Exit
while True:


    # Display available operations for the user
    print("\n===== Student Database Menu =====")

    # Option to create student table
    print("1. Create Table")

    # Option to insert student record
    print("2. Insert Student Data")

    # Option to display student records
    print("3. View Student Data")

    # Option to close program
    print("4. Exit")


    # Take user input to select an operation
    choice = input("Enter your choice: ")



    # If user selects option 1, create table
    if choice == "1":


        # SQL query to create students table
        # IF NOT EXISTS prevents error if table is already present
        create_table_query = """

        CREATE TABLE IF NOT EXISTS students(

            # Automatically generates unique ID for each student
            id INT AUTO_INCREMENT PRIMARY KEY,

            # Stores student name
            name VARCHAR(50),

            # Stores student age
            age INT
        )

        """


        # Execute SQL query using cursor
        cursor.execute(create_table_query)


        # Display success message
        print("Table created successfully (or already exists)")



    # If user selects option 2, insert student data
    elif choice == "2":


        # Take student name from user
        name = input("Enter student name: ")


        # Take student age and convert input string into integer
        age = int(input("Enter student age: "))



        # SQL query for inserting data into students table
        # %s are placeholders used to safely insert values
        insert_query = """

        INSERT INTO students(name, age)

        VALUES(%s, %s)

        """



        # Execute insert query and pass user entered values
        cursor.execute(insert_query, (name, age))


        # Save changes permanently in database
        # Without commit(), inserted data will not be stored
        connection.commit()


        # Display success message
        print("Data inserted successfully")



    # If user selects option 3, display student data
    elif choice == "3":


        # SQL query to fetch all records from students table
        cursor.execute("SELECT * FROM students")


        # Fetch all rows returned by SELECT query
        records = cursor.fetchall()



        # Display heading
        print("\nStudent Records")

        print("----------------")



        # Check if database contains no records
        if len(records) == 0:


            # Print message when table is empty
            print("No data found")



        else:


            # Loop through every student record
            for row in records:


                # Display ID, name and age of each student
                print(

                    "ID:", row[0],

                    "Name:", row[1],

                    "Age:", row[2]

                )



    # If user selects option 4, close application
    elif choice == "4":


        # Display closing message
        print("Closing database connection...")


        # Stop the while loop
        break



    # If user enters any invalid option
    else:


        # Show error message
        print("Invalid choice! Please select 1-4")



# Close cursor after completing database operations
cursor.close()


# Close MySQL database connection
connection.close()


# Final message after closing connection
print("Connection Closed")