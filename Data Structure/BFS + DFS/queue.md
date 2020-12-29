
## FIFO
import queue
q1 = queue.Queue()

## FILO
import queue
q1 = queue.LifoQueue()

## Methods available inside Queue and LifoQueue class
Following are the important methods available inside Queue and LifoQueue class:

```
put(item): This will put the item inside the queue.
get(): This will return you an item from the queue.
empty(): It will return true if the queue is empty and false if items are present.
qsize(): returns the size of the queue.
full(): returns true if the queue is full, otherwise false.
```