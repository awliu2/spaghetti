include <stdio.h>
include <stdlib.h>

int compare_ints(const void* a, const void* b)
{
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int longestConsecutive(int* nums, int numsSize)
{
    if (numsSize == 0)
    {
        return 0;
    }

    qsort(nums, numsSize, sizeof(int), compare_ints);
    int rv = 0;
    int current;
    for (int i = 0; i < numsSize; i++)
    {
        if (i == 0)
        {
            current = 1;
        }
        else if (nums[i] == (nums[i - 1]))
        {
            continue;
        }
        else if (nums[i] == (nums[i - 1] + 1))
        {
            current++;
        }
        else
        {
            current = 1;
        }
        if (current > rv)
        {
            rv = current;
        }
    }
    return rv;
}
