# --- Step 1: Define the Class (The Blueprint) ---
# We use the 'class' keyword to create our Dog blueprint.
class Dog:
    
    # --- Step 2: The Initializer / Constructor ---
    # This special method '__init__' runs automatically whenever we create a new dog.
    # It's used to set up the dog's initial properties (attributes).
    # 'self' refers to the specific dog object we are creating (e.g., fido, buddy).
    def __init__(self, name, age):
        print(f"A new dog named '{name}' has been created!")
        # We store the name and age as attributes of the object.
        self.name = name
        self.age = age

    # --- Step 3: Define Methods (The Object's Behaviors) ---
    # Methods are functions that belong to the class. They define what a dog can do.
    # Notice 'self' is the first parameter. This lets the method access the object's attributes.
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def get_info(self):
        # This method uses the object's attributes to return a description.
        return f"{self.name} is a {self.age}-year-old dog."

# --- Step 4: Create Objects (Instances) from the Class ---
# Now we use our Dog blueprint to create actual, individual dogs.
# This is called "creating an instance" or "creating an object".
# When we call Dog(), the __init__ method runs automatically.
fido = Dog("Fido", 3)
buddy = Dog("Buddy", 5)

# --- Step 5: Use the Objects ---
# We can now access the attributes and call the methods of our dog objects.

# Accessing attributes using dot notation (object.attribute)
print(f"Fido's age is: {fido.age}")         # Output: Fido's age is: 3
print(f"Buddy's name is: {buddy.name}")   # Output: Buddy's name is: Buddy

print("-" * 20) # A separator for clarity

# Calling methods using dot notation (object.method())
fido.bark()      # Output: Fido says: Woof! Woof!
buddy.bark()     # Output: Buddy says: Woof! Woof!

print("-" * 20) # A separator for clarity

# Using our custom info method
print(fido.get_info())   # Output: Fido is a 3-year-old dog.
print(buddy.get_info())  # Output: Buddy is a 5-year-old dog.