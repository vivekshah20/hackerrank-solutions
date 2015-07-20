#include <algorithm>
#include <cstring>
#include <iostream>

#define MAXN 1000

using namespace std;

int arr1[MAXN], arr2[MAXN];

void swap(int* arr, int i, int j, int& cnt) {
  int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
  cnt++;
}

void insertionSort(int* arr, int n, int& cnt) {
  for(int i = 1; i < n; i++) {
    for(int j = i - 1; j >= 0 && arr[j + 1] < arr[j]; j--)
      swap(arr, j, j + 1, cnt);
  }
}

void quickSort(int* arr, int st, int end, int& cnt) {
  if(end - st < 2) return;

  int pivot = arr[end - 1];
  int idx = st;
  for(int i = st; i < end - 1; i++) {
    if(arr[i] < pivot) swap(arr, idx++, i, cnt);
  }
  swap(arr, idx, end - 1, cnt);

  quickSort(arr, st, idx, cnt);
  quickSort(arr, idx + 1, end, cnt);
}

int main() {
  int n; cin >> n;
  for(int i = 0; i < n; i++) cin >> arr1[i];
  memcpy(arr2, arr1, n * sizeof(int));

  int insertionSwaps = 0, quickSwaps = 0;
  insertionSort(arr1, n, insertionSwaps);
  quickSort(arr2, 0, n, quickSwaps);

  cout << insertionSwaps - quickSwaps << endl;
  return 0;
}