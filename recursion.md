# Recursion Code Example 01
```python
# Function to calculate the Fibonacci sequence using recursion
def fibonacci_recursive(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Recursive case: calculate Fibonacci for (n-1) and (n-2) and add them
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Main function to demonstrate the usage
if __name__ == "__main__":
    # Input: the term in the Fibonacci sequence to be calculated
    term = 10
    
    # Output: calculate and print the Fibonacci value for the given term
    result = fibonacci_recursive(term)
    print(f"The {term}th term in the Fibonacci sequence is: {result}")
```

Explanation in comments:

1. `def fibonacci_recursive(n):`: This line defines a function named `fibonacci_recursive` that takes an argument `n`, representing the term in the Fibonacci sequence to be calculated.

2. `if n <= 1:`: This line checks the base case. If `n` is 0 or 1, it means we have reached the end of the recursion, and the function returns `n`.

3. `return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)`: This line represents the recursive case. If `n` is greater than 1, the function calculates the Fibonacci values for `(n-1)` and `(n-2)` by calling itself recursively and adds them to get the result.

4. `if __name__ == "__main__":`: This line checks if the script is being run as the main program.

5. `term = 10`: This line sets the value of `term` to 10, representing the term in the Fibonacci sequence to be calculated.

6. `result = fibonacci_recursive(term)`: This line calls the `fibonacci_recursive` function with the specified term and stores the result in the variable `result`.

7. `print(f"The {term}th term in the Fibonacci sequence is: {result}")`: This line prints the result, indicating the term for which the Fibonacci value is calculated.

# Recursion Code Example 02
Certainly! Here's an example Python file that implements flattening a nested dictionary using recursion, along with detailed comments explaining each part of the solution:

```python
# Function to flatten a nested dictionary using recursion
def flatten_dictionary(d, parent_key='', sep='_'):
    # Initialize an empty dictionary to store the flattened result
    flattened_dict = {}
    
    # Iterate through the items in the input dictionary
    for k, v in d.items():
        # Form the current key by combining the parent key and the current key
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        # If the current value is a nested dictionary, call the function recursively
        if isinstance(v, dict):
            flattened_dict.update(flatten_dictionary(v, new_key, sep=sep))
        else:
            # If the value is not a dictionary, add it to the flattened dictionary
            flattened_dict[new_key] = v
    
    return flattened_dict

# Main function to demonstrate the usage
if __name__ == "__main__":
    # Input: a nested dictionary
    nested_dict = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
                'f': {
                    'g': 4
                }
            }
        },
        'h': 5
    }
    
    # Output: flatten the nested dictionary and print the result
    flattened_result = flatten_dictionary(nested_dict)
    print("Flattened Dictionary:")
    print(flattened_result)
```

Explanation in comments:

1. `def flatten_dictionary(d, parent_key='', sep='_'):`: This line defines a function named `flatten_dictionary` that takes a nested dictionary (`d`), an optional `parent_key` to keep track of the current key, and a separator `sep` to be used between keys in the flattened dictionary.

2. `flattened_dict = {}`: This line initializes an empty dictionary to store the flattened result.

3. `for k, v in d.items():`: This line iterates through the items in the input dictionary (`d`).

4. `new_key = f"{parent_key}{sep}{k}" if parent_key else k`: This line forms the current key by combining the parent key and the current key, using the specified separator. If there is no parent key, it uses just the current key.

5. `if isinstance(v, dict):`: This line checks if the current value is a nested dictionary.

6. `flattened_dict.update(flatten_dictionary(v, new_key, sep=sep))`: If the value is a nested dictionary, the function is called recursively with the nested dictionary, the new key, and the specified separator. The result is then updated into the `flattened_dict`.

7. `else:`: If the current value is not a dictionary, this block is executed.

8. `flattened_dict[new_key] = v`: The key-value pair is added to the `flattened_dict`.

9. `return flattened_dict`: The flattened dictionary is returned.

10. `if __name__ == "__main__":`: This line checks if the script is being run as the main program.

11. `nested_dict = { ... }`: This line sets an example nested dictionary.

12. `flattened_result = flatten_dictionary(nested_dict)`: This line calls the `flatten_dictionary` function with the specified nested dictionary and stores the flattened result in `flattened_result`.

13. `print("Flattened Dictionary:")`: This line prints a header indicating the output.

14. `print(flattened_result)`: This line prints the flattened dictionary result.

# Recursion Code Example 03

Certainly! Below is an example Python file that implements tree traversal using object-oriented programming (OOP) with a basic `TreeNode` class and methods for pre-order, in-order, and post-order traversals:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')

if __name__ == "__main__":
    # Creating a simple binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Perform different tree traversals
    print("Pre-order Traversal:")
    preorder_traversal(root)

    print("\nIn-order Traversal:")
    inorder_traversal(root)

    print("\nPost-order Traversal:")
    postorder_traversal(root)
```

Explanation:

1. `class TreeNode:`: This class represents a node in a binary tree. Each node has a `value`, a `left` child, and a `right` child.

2. `def __init__(self, value):`: The constructor initializes a `TreeNode` with a given value, and its left and right children are initially set to `None`.

3. `def preorder_traversal(node):`: This function performs pre-order traversal starting from the given node. In pre-order traversal, we visit the current node before its left and right children.

4. `def inorder_traversal(node):`: This function performs in-order traversal starting from the given node. In in-order traversal, we visit the left child, then the current node, and finally the right child.

5. `def postorder_traversal(node):`: This function performs post-order traversal starting from the given node. In post-order traversal, we visit the left and right children before the current node.

6. `if __name__ == "__main__":`: This line checks if the script is being run as the main program.

7. Creating a simple binary tree: This section creates a simple binary tree with values 1 to 7.

8. Perform different tree traversals: This section demonstrates the different tree traversal methods by calling the respective functions on the root of the binary tree and printing the results.