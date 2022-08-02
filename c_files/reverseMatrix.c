include <stdio.h>
include <stdlib.h>

void reverse(int arr[], int n)
{
    for (int low = 0, high = n - 1; low < high; low++, high--)
    {
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;
    }
}


void rotate(int** matrix, int matrixSize, int* matrixColSize)
{
    for(int i = 0; i < matrixSize; i++)
    {
        for(int j = i + 1; j < *matrixColSize; j++)
        {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
            
        }
    }
    
    for(int i = 0; i < matrixSize; i++)
    {
        reverse(matrix[i], matrixSize);
    }
}

