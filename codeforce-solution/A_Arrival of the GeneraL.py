def solve():
    n = int(input())
    heights = list(map(int, input().split()))

    # Find the indices of max and min heights
    max_val = max(heights)
    min_val = min(heights)
    
    # We take the FIRST occurrence of max and the LAST occurrence of min
    max_index = heights.index(max_val)
    # Finding the last occurrence by reversing the list and calculating the correct index
    min_index = n - 1 - heights[::-1].index(min_val)

    # Calculate base swaps
    swaps = max_index + (n - 1 - min_index)

    # Adjust for overlap
    if max_index > min_index:
        swaps -= 1

    print(swaps)

if __name__ == "__main__":
    solve()
