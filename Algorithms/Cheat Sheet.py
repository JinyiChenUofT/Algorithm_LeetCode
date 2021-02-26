# ⼆分法 Binary Search

# 时间复杂度：O(logn)
# 空间复杂度：O(1)

def search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# 双指针 Two Pointers

# 相向双指针(patition in quicksort)
def patition(self, A, start, end):
    if start >= end:
        return
    left, right = start, end
    # key point 1: pivot is the value, not the index
    pivot = A[(start+end)//2]
    # key point 2: every time you compare left &right, it should be left<=right not left< right
    while left <= right:
        while left <= right and A[left] < pivot:
            left += 1
        while left <= right and A[right]>pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
            

def merge(list1, list2):
    new_list = []
    i, j = 0, 0
    while i < len(list1) and j <len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1
    # 合并剩下的数到 new_list ⾥
    # 不要⽤ new_list.extend(list1[i:]) 之类的⽅法
    # 因为 list1[i:] 会产⽣额外空间耗费
    while i < len(list1):
        new_list.append([list1[i]])
        i += 1
    while j < len(list2):
        new_list.append([list2[j]])
        j += 1
    return new_list

# Sorting
# Quicksort:  time O(nlogn) space O(1)
# Merge sort: time O(nlogn) space O(n)
# Heap sort: 
# quick sort: time O(nlogn) space O(1)
class QuickSortSolution:
    def sortIntegers(self, A):
        self.quickSort(A, 0, len(A)-1)

    def quickSort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start+end)//2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]

                left += 1
                right -= 1
        self.quickSort(A, start, left)
        self.quickSort(A, left, end)
    
# merge sort
class MergeSortSolution:
    def sortIntegers(self, A):
        if not A:
            return A
        temp = [0]*len(A)
        self.merge_sort(A, 0, len(A)-1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        
        self.merge_sort(A, start, (start+end)//2, temp)
        self.merge_sort(A, (start+end)//2, end, temp)
        self.merge(A, start, end, temp)
    
    def merge(self, A, start, end, temp):
        mid = (start+end)//2
        left= start
        right= end
        index = start

        while left <= mid and right<=end:
            if A[left] < A[right]:
                temp[index] = A[left]
                index += 1
                left += 1
            else:
                temp[index] = A[right]
                index += 1
                right += 1
        while left <= mid:
            index += 1
            left += 1
        while right <= mid:
            index += 1
            right += 1
        for i in range(start, end+1):
            A[i] = temp[i]
# heap sort
def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != r:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# 二叉树分治 Binary Tree Divid & Conquer
# time O(n)
# space O(n)
def divide_conquer(root):
    if root is None:
        return ..
    left = divide_conquer(root.left)
    right = divide_conquer(root.right)

    result = merge (left, right)
    return result


# Tree
def traverse(root):
    #pre-order
    traverse(root.left)
    #in-order
    traverse(root.right)
    #post-order

# BST Iterator
# time O(n)
# space O(n)
def inorder(root):
    if root is None:
        return []
    
    dummy = TreeNode(0)
    dummy.right = root
    stack = [dummy]

    inorder = []
    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            inorder.append(stack[-1])
    return inorder

#BFS
# time O(n+m) ,n 是点数, m 是边数  # 
# Time Complexity of BFS = O(V+E) where V is vertices and E is edges.
# space O(n)
def bfs(start_node):
    queue = collections.deque([start_node])
    distance = {start_node:0}
    while queue:
        node = queue.popleft()
        if node 是终点:
            break or return something
        for neighbor in node.get_neighbors():
            if neighor in distance:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + 1

    return distance
    return distance.keys()
    return distance[end_node]

# https://leetcode.com/problems/walls-and-gates/
# Complexity analysis

# Time complexity : O(mn).

# If you are having difficulty to derive the time complexity, start simple.

# Let us start with the case with only one gate. The breadth-first search takes at most m \times nm×n steps to reach all rooms, therefore the time complexity is O(mn). But what if you are doing breadth-first search from kk gates?

# Once we set a room's distance, we are basically marking it as visited, which means each room is visited at most once. Therefore, the time complexity does not depend on the number of gates and is O(mn)

# Space complexity : O(mn). The space complexity depends on the queue's size. We insert at most m \times nm×n points into the queue.

# DFS

# 找满⾜某个条件的所有⽅案 (99%)
# ⼆叉树 Binary Tree 的问题 (90%)
# 组合问题(95%)
#    问题模型：求出所有满⾜条件的“组合”
#    判断条件：组合中的元素是顺序⽆关的
# 排列问题 (95%)
#    问题模型：求出所有满⾜条件的“排列”
#    判断条件：组合中的元素是顺序“相关”的。

# 不要⽤ DFS 的场景: ⼀切 BFS 可以解决的问题

# 时间复杂度：O(⽅案个数 * 构造每个⽅案的时间)
#   树的遍历 ： O(n)
#   排列问题 ： O(n! * n)
#   组合问题 ： O(2^n * n)
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择


def solveNQueens(self, n: int) -> List[List[str]]:
    results = []
    
    def draw(cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board
    
    def isValid(cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if abs(r-row) == abs(c-col):
                return False
        return True
        
    def search(n,cols):
        row = len(cols)
        if row == n:
            results.append(draw(cols))
            return
        for cur_col in range(n):
            if not isValid(cols, row, cur_col):
                continue
            cols.append(cur_col)
            search(n,cols)
            cols.pop()
    search(n, [])
    return results

def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    def isValid(board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[row//3*3 + i//3][col//3*3 + i%3] == val:
                return False
        return True
            
    def dfs(board, row, col):
        if col == 9:
            return dfs(board, row+1, 0)
        if row == 9:
            return True
        if board[row][col] != '.':
            return dfs(board, row, col+1)
            
        for val in range(1, 10):
            if not isValid(board, row, col, str(val)):
                continue
            board[row][col] = str(val)
            if dfs(board, row, col+1) is True:
                return True
            board[row][col] = '.'
        return False
    dfs(board,0,0)
    return board

# Dynamic Programming


# Tire
WORD_KEY = '$'
        
trie = {}
for word in words:
    node = trie
    for letter in word:
        # retrieve the next node; If not found, create a empty node.
        node = node.setdefault(letter, {})
    # mark the existence of a word in trie node
    node[WORD_KEY] = word
        
# union-find
def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    results = []
    island = set()
    self.size = 0
    self.father = {}
    for pos in positions:
        x, y = pos[0], pos[1]
        if (x, y) in island:
            results.append(self.size)
            continue
        
        island.add((x, y))
        self.father[(x, y)] = (x, y)
        self.size += 1
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            if (x_, y_) in island:
                self.union((x_, y_), (x, y))
            
        results.append(self.size)
        
    return results

def union(self, point_a, point_b):
    root_a = self.find(point_a)
    root_b = self.find(point_b)
    if root_a != root_b:
        self.father[root_a] = root_b
        self.size -= 1
    
def find(self, point):
    path = []
    while point != self.father[point]:
        path.append(point)
        point = self.father[point]
        
    for p in path:
        self.father[p] = point
        
    return point