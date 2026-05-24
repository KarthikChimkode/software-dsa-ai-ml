'''Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

'''

def second_largest(arr):

    unique_arr = list(set(arr)) #remove duplicates we use list() to convert the set to a list
    unique_arr.sort(reverse=True) #sort the list in descending order
    if len(unique_arr) < 2: #if the list has less than 2 elements, return -1
        return -1
    return unique_arr[1]