// https://onlinejudge.org/external/113/11321.pdf

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int N, M;

bool compare(int a, int b){
    int moda = a % M;
    int modb = b % M;

    if (moda != modb){
        return moda < modb;
    }

    bool isodda = a % 2 != 0;
    bool isoddb = b % 2 != 0;

    if (isodda != isoddb){
        if (isodda){return true;}
        else {return false;}
    }

    return isodda ? a > b : a < b;
}

int main(){
    while(true){
        cin >> N >> M;
        std::vector<int> nums(N);
        if (N == 0 && M==0){
            cout<< "0 0" << endl;
            break;
        }
        for (int i = 0; i < N; i++){
            cin >> nums[i];
        }
        sort(nums.begin(), nums.end(), compare);
		
		cout<<  N << " " << M << endl;
        for (int i = 0; i < N; i++){
            cout << nums[i] << endl;
        }
    }
}