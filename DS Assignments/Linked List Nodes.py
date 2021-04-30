class Node:
    def __init__(self, info=None):
        self.info = info
        self.link = None

class SLinkedList:
    def __init__(self):
        self.head = Node()

    def displayOperation(self):
        elems = []
        current = self.head
        if current is None:
            print('Nonce')        
        while current.link != None:
            current = current.link
            elems.append(current.info)
        print(elems,type(elems))

    def searchingOperation(self):
        print('searchingOperation')

    def deletionOperation(self):
        current = self.head
        if current.info == None:
            print('Linked list is empty yet!')
        else:
            item = input('Enter value to delete: ')
            current = self.head
            while current.link != None:
                if current.info == item:
                    break
                p = current
                current = current.link
            p.link = current.link


    def insertionOperation(self):
        current = self.head
        i = int(input('Enter number of nodes to insert: '))
        j = 1
        while i != 0:
            msg = 'Enter value to insert at node number ' + str(j) + ': '
            item = input(msg)
            new_node = Node(item)
            current = self.head
            while current.link != None:
                current = current.link
            current.link = new_node
            i -= 1
            j += 1


class RunProgramme():
    def start(self):
        while True:
            print('There are following basic linked list operation:\n'
                  '------------------------------------------------\n'
                  '1 - Insertion Operation\n'
                  '2 - Deletion Operation\n'
                  '3 - Searching Operation\n'
                  '4 - Display Operation\n'
                  '5 - Exit')
            opType = int(input('Choice respective number: '))
            if opType > 0 and opType < 6:
                print('------------------------------------------------')
            else:
                print('Invalid Choice - Please try again [1-5]')
                continue
            if opType is 1:
                b.insertionOperation()
            elif opType is 2:
                b.deletionOperation()
            elif opType is 3:
                b.searchingOperation()
            elif opType is 4:
                b.displayOperation()
            elif opType is 5:
                exit(0)


a = RunProgramme()
b = SLinkedList()
a.start()
