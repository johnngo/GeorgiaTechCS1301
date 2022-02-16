#A Stack is a type of list where instead of accessing
#any item in the list at any time, you can only add
#or remove items from the top of the Stack.
#
#Adding a new item to the stack is called "pushing"
#the item onto the stack. Removing the top item on
#the stack is called "popping" the item off the stack.
#When an item is "popped" off the stack, it is removed
#from the list altogether.
#
#Write a class called Stack. Stack should have the
#following methods:
#
# - An __init__ method that initializes the empty list
#   that is the stack's contents.
# - A stack_push() method that takes one parameter (in
#   addition to self): an item to push onto the top
#   of the stack.
# - A stack_pop() method that returns the current top
#   item on the stack and removes it from the underlying
#   list. If the list is already empty, this returns
#   None.
#
#For example, the following code would print the
#numbers 3, 2, and 1 (in that order). Note that this
#is the opposite order of how they are pushed: the
#pop method will always return the elements in the
#reverse order that they were added in.
#
#new_stack = Stack()
#new_stack.stack_push(1)
#new_stack.stack_push(2)
#new_stack.stack_push(3)
#print(new_stack.stack_pop())
#print(new_stack.stack_pop())
#print(new_stack.stack_pop())

#Add your class here!
class Stack:
    def __init__(self):
        self.stack =[]
        
    def stack_push(self, stack):
        self.stack.append(stack)
    
    def stack_pop(self):
        if len(self.stack) >= 1:
            data = self.stack[-1]
            del self.stack[-1]
            return data
        else:
            return None    


#The following lines of code will test your class.
#If it works correctly, it will print 3, 2, and 1
#in that order, each on their own line.
new_stack = Stack()
new_stack.stack_push(1)
new_stack.stack_push(2)
new_stack.stack_push(3)
print(new_stack.stack_pop())
print(new_stack.stack_pop())
print(new_stack.stack_pop())



#First, we define the class with its name:
class Stack:
    
    #The class needs to persist a list of items. Inside
    #the class, we'll use a regular list to hold these
    #items. When we create a new Stack, we need to initialize
    #that list to an empty list so we can use it later:
    def __init__(self):
        self.items = []
    
    #The key to pushing and popping is that it doesn't matter
    #whether we add new items to the beginning or end of the
    #list as long as we're consistent. In this implementation,
    #we'll always add them to the end. so, if we want to push
    #a new item, we append it to the list of items:
    def stack_push(self, item):
        self.items.append(item)
    
    #Then, if we want to pop an item, we have to get it from
    #the end as well:
    def stack_pop(self):
        
        #First though, if there are no items, we return None
        #as instructed.
        if len(self.items) == 0:
            return None
        
        #Then, we need to do three things: first we need to
        #save the last item to return. Then we need to remove
        #it from the list. Then we need to actually return it.
        #Notice that these have to be done in this order: if we
        #delete it first, we don't know what it was and can't
        #return it. If we return before deleting, then the function
        #is over and the list is unchanged.
        item = self.items[-1]
        del self.items[-1]
        return item


new_stack = Stack()
new_stack.stack_push(1)
new_stack.stack_push(2)
new_stack.stack_push(3)
print(new_stack.stack_pop())
print(new_stack.stack_pop())
print(new_stack.stack_pop())
