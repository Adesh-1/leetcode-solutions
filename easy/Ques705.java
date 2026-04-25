// 705. Design HashSet
// in java
class MyHashSet {

    private int size;
    private List<Integer>[] buckets;

    public MyHashSet() {
        size = 1000;
        buckets = new ArrayList[size];

        for (int i = 0; i < size; i++)
            buckets[i] = new ArrayList<>();
    }

    private int hash(int key){
        return key % size;
    }

    public void add(int key) {
        int index = hash(key);
        if (!buckets[index].contains(key))
            buckets[index].add(key);
    }

    public void remove(int key) {
        int index = hash(key);
        buckets[index].remove(Integer.valueOf(key)); // important
    }

    public boolean contains(int key) {
        int index = hash(key);
        return buckets[index].contains(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */


// in python
class MyHashSet:

    def __init__(self):
        self.size = 1000  # number of buckets
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.buckets[index]
