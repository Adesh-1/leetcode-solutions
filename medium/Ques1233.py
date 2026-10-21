# 1233. Remove Sub-Folders from the Filesystem
# in python
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()

        ans = []

        for f in folder:
            if not ans or not f.startswith(ans[-1] + "/"):
                ans.append(f)

        return ans

# in java
class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);

        List<String> list = new ArrayList<>();

        for (String f : folder) {
            if (list.isEmpty() || !f.startsWith(list.get(list.size() - 1) + "/"))
                list.add(f);
        }

        return list;
    }
}
