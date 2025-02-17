# 2025-ITELEC2-LAB016
Week 05 - Working with Functions

Laboratory # 16 - Guided Coding Exercise: Basic Function Definition and Calling

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 16 - Guided Coding Exercise: Basic Function Definition and Calling**

   **Objective:**
   - Understand the use of a while loop for repetitive tasks.
   - Learn how to terminate a loop using a sentinel value.
   - Recognize the advantages of looping for dynamic, user-driven processes.
   - Practice input validation and error handling.

   **Desired Output (Example 1):**
   ```bash
   Enter a number (or 'stop' to finish): 5
   Enter a number (or 'stop' to finish): 10
   Enter a number (or 'stop' to finish): 3
   Enter a number (or 'stop' to finish): stop
   The total sum is: 18
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - Python does not have a built-in switch statement like some other languages. Dictionaries provide a clean and efficient way to achieve similar functionality.
   - The .get() method of a dictionary allows you to retrieve a value associated with a key. Crucially, it also lets you specify a default value that will be returned if the key is not found in the dictionary. This is very useful for handling cases where the user might enter invalid input.
   - The ternary operator (value_if_true if condition else value_if_false) provides a concise way to write conditional expressions in a single line. It's useful for simple conditions where you want to assign one of two values.
   - String methods like .strip() and .lower() are essential for normalizing user input, making your code more robust.

   **Python Best Practices**
   - Input Normalization: Always normalize user input (e.g., convert to lowercase using .lower() and remove leading/trailing whitespace using .strip()) to handle variations in user input and prevent unexpected behavior.
   - Dictionary .get() with Default: Use the .get() method with a default value when retrieving values from a dictionary. This is a best practice, especially when dealing with user input, as it provides a clean way to handle cases where the key might not exist.
   - Readability: Even with concise constructs like the ternary operator, prioritize code readability. If a ternary expression becomes too complex, consider using a regular if...else statement for clarity.
   - Descriptive Variable Names: Use meaningful variable names (e.g., day_messages, day, message, day_type).
   - Comments: Add comments to explain your logic, especially when simulating control flow structures like a switch statement.
   - Test Thoroughly: Test your code with various inputs, including valid days of the week (with different capitalization and spacing) and invalid days, to ensure it handles all cases correctly.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `while_loop_sentinel.py`
      
   2. Initialize the sum variable:
      - Create a variable named total_sum and initialize it to 0. This variable will store the sum of the numbers entered by the user.
```python
total_sum = 0
```
      
   3.  Start a while loop that continues indefinitely:
      - Use a while True loop. This creates a loop that will run continuously until explicitly stopped using the break statement.
```python
while True:
```

   4. Prompt the user for input:
      - Inside the while loop, use the input() function to prompt the user to enter a number or "stop" to finish. Store the input in a variable named user_input.
```python
    user_input = input("Enter a number (or 'stop' to finish): ")
```

   5. Check if the sentinel value 'stop' is entered:
      - Convert the user_input to lowercase using .lower() and remove any leading/trailing whitespace using .strip(). - This handles variations in user input (e.g., "Stop", " STOP ", "stop").
      - Use an if statement to check if the normalized user_input is equal to "stop".
      - If it is, use the break statement to exit the while loop.
```python
    if user_input.strip().lower() == "stop":
        break  # Exit the loop
```

   6. Convert input to a number and add to total_sum (with error handling):
      - After the if statement that checks for "stop", use a try-except block to handle potential ValueError exceptions that might occur if the user enters something that is not a number.
      - Inside the try block:
         - Convert the user_input to a float (to allow for decimal numbers).
         - Add the converted number to total_sum using the += operator.
      - Inside the except ValueError block:
         - Print an error message to the user indicating that the input was invalid.
```python
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")
```

   7. Print the final total sum:
      - After the while loop has finished (outside the loop), use the print() function to display the final value of total_sum.
```python
print("The total sum is:", total_sum)
```
   8. Complete Code: Combine the steps above to form the complete program.
   9. Run the code: Execute your Python code.
   10. Observe the output: Test the program by entering various numbers and then entering "stop" (in different cases and with extra spaces).  Also, test it by entering non-numeric input to see how the error handling works.

   **Conclusion**
   This exercise demonstrated the use of a while loop for handling user input with a sentinel value.  You learned how to create a loop that continues until a specific condition is met (in this case, the user entering "stop").  You also practiced input validation and error handling using try-except blocks.  The while loop and sentinel values are very useful for creating interactive programs where the number of iterations depends on user input.  Robust error handling is crucial for creating reliable and user-friendly programs.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 16"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
