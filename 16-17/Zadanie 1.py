import random
class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class LinkList:
    def __init__(self):
        self.top = Node()

    def add_element(self, value):
        new = Node(value)
        new.next = self.top.next
        self.top.next = new

    def add_random_elements(self, number):
        for i in range(0, number):
            self.add_element(random.randint(0,100))

    def print_list(self):
        tmp=self.top.next
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next
        print()

    def bubble_sort(self):
        if not self.top.next:
            return
        changes = True
        while changes:
            changes = False
            tmp = self.top.next
            prev = self.top
            while tmp.next is not None:
                if tmp.value > tmp.next.value:
                    changes = True
                    prev.next = tmp.next
                    tmp.next = prev.next.next
                    prev.next.next = tmp
                prev = prev.next
                tmp = prev.next

    def normal_distribution(self, end=0, elements=0):
        for i in range(elements):
            self.add_element(random.random()*end)

    def bucket_sort (self, end):
        buckets = [LinkList() for i in range(0, end)] #O(n)
        tmp = self.top.next
        while tmp is not None: #O(n)
            bufor = tmp.next
            tmp.next = buckets[int(tmp.value)].top.next
            buckets[int(tmp.value)].top.next = tmp
            tmp = bufor
        for i in buckets:
            i.bubble_sort() #narazie jest ~1/10 N^2 ale da sie 1/10n * log(1/10n) ,ale ponieważ rozkłąd jest jednostajny zakłądamy że w jednm
                            #Kubełku jest mało elementó więc brak wpływu na łżożoność (można inserta walnąć najlpeiej)
        result = LinkList()
        end = result.top
        for i in buckets: #O(n)
            end.next = i.top.next
            if end.next:
                prev = None
                tmp = end.next
                while tmp is not None:
                    prev = tmp
                    tmp = tmp.next
                end = prev
        self.top = result.top

link = LinkList()
link.normal_distribution(10,15)
link.print_list()
link.bucket_sort(10)
print()
link.print_list()



