#In Python we deal with data structures like lists,
#but we don't talk much about how lists are implemented
#by Python itself.
#
#One way in which lists can be implemented is with what
#is called a Linked List. In a Linked List, a list is
#made of a series of items. Each item contains two
#elements: its own value (node.value), and a pointer to
#where to find the next element in the list
#(node.next_node). So, you can't jump right in to
#"item 7"; you instead have to start with the first
#item and keep getting the next item until you reach the
#seventh item.
#
#Below is some code we've written to implement a
#Linked List. Specifically, this code represents a
#single node in a linked list: a full list is created
#just by chaining nodes like these together. The last
#node in the linked list will point to None as the
#next item; that indicates you've reached the end of
#the linked list.
#
#Write a function called linked_list_search. Your
#linked_list_search function should take two parameters:
#a single linked list node, and a search term. Your
#function should return True if the search term is the
#value of the linked list node or any node after it.
#It should return False if the value is not found in
#the linked list.

class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#Write your function here!
def linked_list_search(linked_list,search_term):
  curr_node = linked_list
  while curr_node:
    print(curr_node)
    if curr_node.value == search_term:
      return True
    curr_node = curr_node.next_node
  return False


#Below are lines of code that create a linked list,
#and then search for two values in that linked list:
#one that is there, one that isn't. If your function
#works, it should print True then False.
node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))

class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#There are two ways we can do this: recursively and
#non-recursively. I think the recursive approach is more
#elegant, so we'll start with that one.
#
#First we define the function. Note that it doesn't matter
#to the function whether the node is the first in the list
#or a later one; it just needs to search from the current
#node onwards:
def linked_list_search(node, search):
    
    #If this node's value is the one we're searching for,
    #we're done! Return True.
    if node.value == search:
        return True
    
    #Otherwise, we need to check if the next node is None.
    #If it is, we've reached the end of the list without
    #finding our search term, so we return False:
    elif node.next_node == None:
        return False
    
    #Then, if this node doesn't have the value we're looking
    #for, and if this node isn't the last node, then we call
    #linked_list_search on the next node:
    else:
        return linked_list_search(node.next_node, search)
    
    #This will continue until either the value is found or the
    #end of the list is reached.
    #
    #We can also do this non-recursively. See the other sample answer
    #for how!


node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))


class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#The non-recursive approach is similar, but instead of
#repeatedly calling linked_list_search, we'll instead use
#a while loop and update what node we're looking at on the
#current iteration. The function definition stays the same:
def linked_list_search(node, search):
    
    #We're going to want to loop while the current node is
    #not None. Once it's None, we know we have reached the
    #end of the list. If we find the search term before node
    #is None, then we'll return and the loop will be over
    #anyway!
    while not node == None:
        
        #Next, we check to see if this node's value is the
        #search term. If so, we're done! Return True.
        if node.value == search:
            return True
        
        #Otherwise, we keep searching from the next node.
        #If there is no next node, then this sets node equal
        #to None, and the while loop ends.
        else:
            node = node.next_node
    
    #The only way to reach the line below is if we looked through
    #the entire list and never returned True. So, that means we did
    #not find the search term. So, we return False.
    return False

node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))

