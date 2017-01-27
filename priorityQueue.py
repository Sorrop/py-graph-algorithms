import heapq
import itertools


class PriorityQueue:
    """
    Collection of items with priorities, such that items can be
    efficiently retrieved in order of their priority, and removed. The
    items must be hashable.

    """
    _REMOVED = object()         # placeholder for a removed entry

    def __init__(self, iterable=()):
        """Construct a priority queue from the iterable, whose elements are
        pairs (item, priority) where the items are hashable and the
        priorities are orderable.

        """
        self._entry_finder = {}  # mapping of items to entries

        # Iterable generating unique sequence numbers that are used to
        # break ties in case the items are not orderable.
        self._counter = itertools.count()

        self._data = []
        for item, priority in iterable:
            self.add(item, priority)

    def add(self, item, priority):
        """Add item to the queue with the given priority. If item is already
        present in the queue then its priority is updated.

        """
        if item in self._entry_finder:
            self.remove(item)
        entry = [priority, next(self._counter), item]
        self._entry_finder[item] = entry
        heapq.heappush(self._data, entry)

    def remove(self, item):
        """Remove item from the queue. Raise KeyError if not found."""
        entry = self._entry_finder.pop(item)
        entry[-1] = self._REMOVED

    def pop(self):
        """Remove the item with the lowest priority from the queue and return
        it. Raise KeyError if the queue is empty.

        """
        while self._data:
            _, _, item = heapq.heappop(self._data)
            if item is not self._REMOVED:
                del self._entry_finder[item]
                return item
        raise KeyError('pop from an empty priority queue')
