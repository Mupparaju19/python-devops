#Q1: What is a list in Python, and how is it used in DevOps?
# ans)In Python, a list is a mutable data structure that can store multiple values in an ordered sequence. 
#It allows adding, removing, and modifying elements.
#In DevOps scenarios, lists are useful for gathering and organizing information, 
#such as EC2 instance IDs, S3 bucket names, or server configurations. This makes it easier to store, 
#process, and print resource details for automation tasks.
#How do you create a list in Python, and can you provide an example related to DevOps?
Ec2_instances_list = ["ansible", "murali", "python", "project1"]
Length_list = len(Ec2_instances_list)
Ec2_instances_list.append("king")
print(Length_list)
Ec2_instances_list.remove("murali")
print (Ec2_instances_list)

#What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?

# In Python, the main difference between a list and a tuple is:

# List:

# Mutable (can be changed after creation).
# Allows adding, removing, and modifying elements.
# Defined using square brackets [ ].
# Use case in DevOps: Useful for storing dynamic data like EC2 instances, S3 buckets, or server names, where updates may be needed during automation tasks.
# Tuple:
# command k c for all 
# Immutable (cannot be changed after creation).
# Does not allow adding, removing, or modifying elements.
# Defined using parentheses ( ).
# Use case in DevOps: Suitable for storing fixed data, such as configuration settings or default values that should not change during automation.
