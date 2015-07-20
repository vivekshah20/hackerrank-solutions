#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


void quickSort(vector<int> &arr, int min, int max) 
{
    if (min >= max) return;
    int pivot = arr[max];
    int index = min;

    for (int i = min; i < max; ++i)
        if (arr[i] < pivot) 
        {
            swap(arr[i], arr[index]);
            ++index;
        }
    swap(arr[index], arr[max]);
    for (auto x : arr)
        cout << x << " ";
    cout << endl;
    quickSort(arr, min, index - 1);
    quickSort(arr, index + 1, max);
}

int main() 
{

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    quickSort(arr, 0, n - 1);

}
