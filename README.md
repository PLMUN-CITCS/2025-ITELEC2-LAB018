# 2025-ITELEC2-LAB018
Week 05 - Working with Functions

Laboratory # 18 - Guided Coding Exercise: Nested Functions and Reusing User-Defined Functions

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

**Laboratory # 18 - Guided Coding Exercise: Nested Functions and Reusing User-Defined Functions**

   **Objective:**
   - Learn to break down a complex task into smaller, more manageable functions.
   - Understand the concept of nested function calls (calling a function within another function).
   - Practice writing functions that work together to achieve a larger goal.
   - Reinforce the benefits of function reuse for code modularity and efficiency.

   **Desired Output:**
   ```bash
   The sum of squares is: 29
   ```
   (Since 2² + 3² + 4² = 4 + 9 + 16 = 29)
   
   **Notable Observations (to be discussed after completing the exercise):**
   - Nested Function Calls: The sum_of_squares() function calls the square() function within its loop. This is an example of a nested function call.
   - Function Reuse: The square() function is reused multiple times within the sum_of_squares() function, demonstrating the modularity and efficiency of using functions.
   - Breaking Down Complexity: The problem of calculating the sum of squares is broken down into smaller, more manageable functions (square and sum_of_squares), making the code easier to understand, test, and maintain.

   **Python Best Practices**
   - Single Responsibility Principle: Keep functions focused on a single, well-defined task. This makes your code more modular and easier to reason about.
   - Docstrings: Write clear and concise docstrings to describe the purpose and parameters of each function.
   - Meaningful Names: Use descriptive variable names and maintain consistency in your naming conventions.
   - Indentation: Proper indentation is crucial for readability and to define the structure of your code, especially when using nested functions.
   - Test Thoroughly: Test your functions individually and together to ensure they work correctly in all scenarios.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `nested_functions.py`
      
   2. Define a function to calculate the square of a number (square):
      - Use the def keyword followed by the function name (square).
      - Add parentheses () and include a parameter name (e.g., num) inside the parentheses. This defines the input that the function will accept.
      - End the line with a colon :.
      - Inside the function definition (indented), calculate the square of the num (using num * num or num ** 2).
      - Use the return statement to return the calculated square.
```python
def square(num):
    """Returns the square of the given number."""
    return num * num  # Or num ** 2
```
      
   3. Define a function to calculate the sum of squares (sum_of_squares):
      - Use the def keyword followed by the function name (sum_of_squares).
      - Add parentheses () and include a parameter name (e.g., numbers) inside the parentheses. This will be a list of numbers.
      - End the line with a colon :.
      - Inside the function definition (indented):
         - Initialize a variable named total to 0. This will store the sum of squares.
         - Use a for loop to iterate through each number (n) in the numbers list.
         - Inside the loop, call the square() function that you defined earlier, passing n as an argument. This calculates the square of the current number.
         - Add the returned square to the total.
      - After the loop, use the return statement to return the calculated total.
```python
def sum_of_squares(numbers):
    """Returns the sum of the squares of the numbers in the list."""
    total = 0
    for n in numbers:
        total += square(n)  # Call the square function and add to total
    return total
```

   4. Define a list of numbers and call the function:
      - After the function definitions (not indented), create a list of numbers (e.g., ``) and store it in a variable named numbers_list.
      - Call the sum_of_squares() function, passing numbers_list as an argument. Store the returned result in a variable named result.
```python
numbers_list = [2, 3, 4]
result = sum_of_squares(numbers_list)
```

   5. Print the final result:
      - Use the print() function with an f-string to display the final result with a descriptive message.
```python
print(f"The sum of squares is: {result}")
```

   6. Complete Code: Combine the steps above to form the complete program.
   7. Run the code: Execute your Python code.
   8. Observe the output: Verify that the output matches the "Desired Output" shown above.

   **Conclusion**
   This exercise demonstrated the power of using nested functions and reusing user-defined functions to solve more complex problems.  You learned how to break down a task into smaller, more manageable functions and how to call functions within other functions.  By reusing functions, you can write more efficient and modular code that is easier to understand and maintain.  This approach is essential for building larger and more complex Python programs.

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
git commit -m "Submitting Python Week 04 - Laboratory # 18"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
