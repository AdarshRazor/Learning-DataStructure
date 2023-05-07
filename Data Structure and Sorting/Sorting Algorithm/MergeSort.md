# Merge Sort
 
Merge sort is an efficient general-purpose, and comparison-based sorting algoritm also know as divide and conquer.

It divides the input array into two halves, calls itself for the two halves repeatedly until it breaks down to smallest part. then merges the two sorted halves.

![image](https://user-images.githubusercontent.com/33658792/236674293-bcf28b2e-fdc1-48a6-bf55-9c348b2ab7f9.png)

## Implementation

1. It starts by dividing the array into two halves.
2. Repeat the procedure until it breakdown into smallest parts.
3. Then comapre the bottom halfs and sort the array putting smalles first.
4. While sorting, merge the two halves.
5. Repeat this process and you are done. :fire:

## Space and time complexity

* Worst complexity: n*log(n)
* Average complexity: n*log(n)
* Best complexity: n*log(n)
* Space complexity: n

## When to use

- Merge sort is more efficient and works faster in case of **larger array** size or dataset.

- It is also useful to sort **linked lists.**

Here is the [link](https://www.youtube.com/watch?v=JSceec-wEyw) of the video from GeeksforGeeks which might clear you idea.

## Implementation (Code)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]

    return result

arr = [27,13,57,43,98,3,7,11,45,21,100]

print(merge_sort(arr))
```
