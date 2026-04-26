# 706. Design HashMap
# in python
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # update
                return

        bucket.append([key, value])  # insert

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)  # safe removal
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# in java
class MyHashMap {

    private int size;
    private List<int[]>[] buckets;

    public MyHashMap() {
        size = 1000;
        buckets = new ArrayList[size];

        for (int i = 0; i < size; i++) {
            buckets[i] = new ArrayList<>();
        }
    }

    private int hash(int key) {
        return key % size;
    }

    public void put(int key, int value) {
        int index = hash(key);
        List<int[]> bucket = buckets[index];

        for (int[] pair : bucket) {
            if (pair[0] == key) {
                pair[1] = value; // update
                return;
            }
        }

        bucket.add(new int[] { key, value }); # // insert
    }

    public int get(int key) {
        int index = hash(key);
        List<int[]> bucket = buckets[index];

        for (int[] pair : bucket) {
            if (pair[0] == key) {
                return pair[1];
            }
        }

        return -1;
    }

    public void remove(int key) {
        int index = hash(key);
        List<int[]> bucket = buckets[index];

        Iterator<int[]> it = bucket.iterator();
        while (it.hasNext()) {
            int[] pair = it.next();
            if (pair[0] == key) {
                it.remove();
                return;
            }
        }
    }
}
# /**
#  * Your MyHashMap object will be instantiated and called as such:
#  * MyHashMap obj = new MyHashMap();
#  * obj.put(key,value);
#  * int param_2 = obj.get(key);
#  * obj.remove(key);
#  */
