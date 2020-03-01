"""day19.py
"""
ELFCOUNT = 3017957
elves = [[i, 1] for i in range(1, ELFCOUNT+1)]
startlen = len(elves)
elflen = len(elves)

class Link:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Link(val={self.val}, next={self.next.val}, prev={self.prev.val})'


def create_list(num):
    prev = None
    for i in range(1, num+1):
        l = Link(i)
        if i == 1:
            head = l
        if prev:
            prev.next = l
        l.prev = prev
        prev = l
    l.next = head
    head.prev = l
    return head

head = create_list(ELFCOUNT)
pointer = head

while elflen > 1:
    pointer.next = pointer.next.next
    pointer.next.next.prev = pointer
    elflen -= 1
    if elflen != 1:
        pointer = pointer.next
print(f'Part 1: {pointer.val}')


head = create_list(ELFCOUNT)
elflen = ELFCOUNT
pointer1 = head
pointer2 = head
for _ in range(ELFCOUNT // 2):
    pointer2 = pointer2.next


is_even = elflen % 2 == 0
while elflen > 1:
    pointer2.next.prev = pointer2.prev
    pointer2.prev.next = pointer2.next
    pointer2 = pointer2.next
    elflen -= 1
    is_even = not is_even
    if elflen != 1:
        if is_even:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        else:
            pointer1 = pointer1.next
print(f'Part 2: {pointer1.val}')

