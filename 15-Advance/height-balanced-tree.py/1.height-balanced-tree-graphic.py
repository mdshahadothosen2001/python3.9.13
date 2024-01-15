# This is Binary Search Tree here imbalanced node
#        20
#       /  \
#      10   30
#     /    /  \
#    5   25   40

# Balance Factor for 20:
#     BF(20) = Height(5) - Height(30) 
#         = 1 - 2 
#         = -1 
# No imbalance at 20.


# Balance Factor for 10:
#  BF(10) = Height(5) - Height(None) 
#         = 1 - 0 
#         = 1 
# No imbalance at 10.


# Balance Factor for 30:
#     BF(5) = Height(25) - Height(40) 
#         =1 - 1
#         = 0 
# No imbalance at 30.

# Balance Factor for 25:
#  BF(25) = Height(None) - Height(None) 
#         = 0 - 0
#         = 0
# No imbalance at 25.


# Balance Factor for 40:
#  BF(40) = Height(None) - Height(None) 
#         = 0 - 0 
#         = 0 
# No imbalance at 40.




# Another Binary Tree
# Let's calculate the balance factors for each node in the provided AVL tree:

# ```
#        20
#       /  \
#      5   30
#         /  \
#       10   40
#            /
#          25
# ```

# Balance Factor for 20:
#     BF(20) = Height(5) - Height(30) 
#         = 1 - 2 
#         = -1 
# No imbalance at 20.

# Balance Factor for 5:
#     BF(5) = Height(None) - Height(None) 
#         =0 - 0
#         = 0 
# No imbalance at 5.

# Balance Factor for 30:
#     BF(30) = Height(10) - Height(40) 
#         = 0 - 1 
#         = -1 
# No imbalance at 30.

# Balance Factor for 10:
#  BF(10) = Height(None) - Height(25) 
#         = 0 - 0 
#         = 0 
# No imbalance at 10.

# Balance Factor for 40:
#  BF(40) = Height(25) - Height(None) 
#         = 1 - 0 
#         = 1 
# No imbalance at 40.

# Balance Factor for 25:
#  BF(25) = Height(None) - Height(None) 
#         = 0 - 0
#         = 0
# No imbalance at 25.

# In this AVL tree, all balance factors are within the acceptable range of \(-1, 0, 1\)
# indicating that the tree is balanced according to the AVL property. No rotations are needed to maintain balance.