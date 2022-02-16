#A Queue is a type of list where instead of accessing
#any item in the list at any time, you can only add
#items to the end of the list, and you can only access
#items from the start of a list (sort of like a line at
#a store: whoever gets in line first gets to the front
#of the line first).
#
#Adding a new item to the queue is called "enqueueing"
#the item into the queue. Removing an item from the
#queue is called "dequeueing" the item from the queue.
#When an item is "dequeued" from the queue, it is
#removed from the list altogether.
#
#Write a class called Queue. Queue should have the
#following methods:
#
# - An __init__ method that initializes the empty list
#   that is the queue's contents.
# - A enqueue() method that takes one parameter
#   (in addition to self): an item to add to the end of
#   the queue.
# - A dequeue() method that returns the first item
#   (that is, the one added first) from the queue and
#   removes it from the underlying list. If the list is
#   already empty, this returns None.
#
#For example, the following code would print the
#numbers 1, 2, and 3 (in that order). Items are printed
#in the same order in which they are added.
#
#new_queue = Queue()
#new_queue.enqueue(1)
#new_queue.enqueue(2)
#new_queue.enqueue(3)
#print(new_queue.dequeue())
#print(new_queue.dequeue())
#print(new_queue.dequeue())

#Add your class here!
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,enqueue):
#        self.enqueue = enqueue
        self.queue.append(enqueue)
        
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        
        enqueue =self.queue[0]
        del self.queue[0]
        return enqueue
        

#The following lines of code will test your class.
#If it works correctly, it will print 1, 2, and 3
#in that order, each on their own line.
new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())


#First, we define the class with its name:
class Queue:
    
    #The class needs to persist a list of items. Inside
    #the class, we'll use a regular list to hold these
    #items. When we create a new Queue, we need to initialize
    #that list to an empty list so we can use it later:
    def __init__(self):
        self.items = []
    
    #It doesn't matter whether we add to the end and remove
    #from the beginning or vice versa as long as we're
    #consistent. In this implementation, we'll add to the end
    #and remove from the beginning.
    def enqueue(self, item):
        self.items.append(item)
    
    #Then, we need to remove from the beginning:
    def dequeue(self):
        
        #First though, if there are no items, we return None
        #as instructed.
        if len(self.items) == 0:
            return None
        
        #Then, we need to do three things: first we need to
        #save the first item to return. Then we need to remove
        #it from the list. Then we need to actually return it.
        #Notice that these have to be done in this order: if we
        #delete it first, we don't know what it was and can't
        #return it. If we return before deleting, then the function
        #is over and the list is unchanged.
        item = self.items[0]
        del self.items[0]
        return item


new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())
