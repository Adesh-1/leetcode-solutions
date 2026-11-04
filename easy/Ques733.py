# 733. Flood Fill
# in python
class Solution:

    def helper(self, img, sr, sc, color, vis, org_col):
        if (sr < 0 or sc < 0 or sr >= len(img) or sc >= len(img[0]) \
            or vis[sr][sc] or img[sr][sc] != org_col
        ):
            return

        vis[sr][sc] = True
        img[sr][sc] = color

        self.helper(img, sr, sc - 1, color, vis, org_col)  # left
        self.helper(img, sr, sc + 1, color, vis, org_col)  # right
        self.helper(img, sr - 1, sc, color, vis, org_col)  # up
        self.helper(img, sr + 1, sc, color, vis, org_col)  # down

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        vis = [[False] * len(image[0]) for _ in range(len(image))]
        self.helper(image, sr, sc, color, vis, image[sr][sc])

        return image

# in java
class Solution {
    public void helper(int[][] img, int sr, int sc, int color, boolean[][] vis, int orgCol) {
        if (sr < 0 || sc < 0 || sr >= img.length || sc >= img[0].length
                || vis[sr][sc] || img[sr][sc] != orgCol)
            return;

        vis[sr][sc] = true;
        img[sr][sc] = color;

        helper(img, sr, sc - 1, color, vis, orgCol);
        helper(img, sr, sc + 1, color, vis, orgCol);
        helper(img, sr - 1, sc, color, vis, orgCol);
        helper(img, sr + 1, sc, color, vis, orgCol);
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        boolean[][] vis = new boolean[image.length][image[0].length];
        helper(image, sr, sc, color, vis, image[sr][sc]);

        return image;
    }
}
