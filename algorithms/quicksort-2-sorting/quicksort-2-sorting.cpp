#include <bits/stdc++.h>
using namespace std;

void quickSort(vector<int> &array, int l, int r){
    if(l >= r) return;
    int pivot = array[l];
    vector<int> large;
    vector<int> small;
    for(int i = l; i <= r; i++){
        if(array[i] < pivot){
            small.push_back(array[i]);
        }else{
            large.push_back(array[i]);
        }
    }
    
    int m = small.size() + l;
    small.insert(small.end(), large.begin(), large.end());
    for(int i = l; i <= r; i++){
        array[i] = small[i - l];
    }
    quickSort(array, l, m-1);
    quickSort(array, m+1, r);
    for(int i = l; i <= r; i++){
        cout << array[i];
        if(i+1 <= r) cout << " ";
        else cout << endl;
    }
}
void quickSort(vector <int>  &ar, int n) {
    quickSort(ar, 0, n-1);
}

int main()
{
    int n;
    cin >> n;

    vector <int> arr(n);
    for(int i = 0; i < (int)n; ++i) {
        cin >> arr[i];
    }

    quickSort(arr,n);

    return 0;
}
