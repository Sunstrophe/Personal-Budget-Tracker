"""
**Features to Implement:**
1. **User Registration and Login:** Allow users to register with a username and password. Existing users should be able to log in securely.

2. **Expense Tracking:** Users should be able to add, view, edit, and delete their expenses. Each expense should have a date, description, category (e.g., groceries, entertainment, rent), and amount.

3. **Income Tracking:** Similar to expenses, users should be able to track their income sources. Each income entry should have a date, description, category, and amount.

4. **Budget Categories:** Implement a system to categorize expenses and income. Users can create custom categories and assign transactions to them.

5. **Balance Calculation:** Calculate and display the user's current balance based on their income and expenses.

6. **Monthly Reports:** Generate monthly reports that show a summary of income, expenses, and balance for each month.

7. **Search and Filter:** Allow users to search for specific transactions and filter them based on categories, dates, or descriptions.

8. **Data Storage:** Store user data securely in files or a database.

9. **Graphical Representation:** Provide graphical representations of the user's financial data, such as bar charts or pie charts, to help visualize their spending habits.

10. **Security:** Implement proper password hashing and data encryption to ensure user data remains secure.
"""

import user_set


def main():
    print("Welcome to the personal budget tracking system!")
    current_key: str = ""
    # choose current actione
    while True:
        print("Type 1 to login")
        print("Type 2 to register a user")
        print("Type 3 to delete a user")
        print("Type q to quit")
        current_key = input("Enter a key: ")
        if current_key.lower() == "q":
            break
        if current_key.lower() == "1":
            user_set.login_user()
        if current_key.lower() == "2":
            user_set.register_user()
        if current_key.lower() == "3":
            user_set.remove_user()


main()