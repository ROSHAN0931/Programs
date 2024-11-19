#include<bits/stdc++.h>
using namespace std;

bool countPal(string &s,int low,int high)
{
    while(low < high)
    {
        if(s[low] != s[high])
        {
            return false;
        }
        low++;
        high--;
    }
    return true;
}

string longestpal(string &s)
{
    int n = s.size();
    int maxlen=0;
    int start=0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(countPal(s,i,j) && (j-i+1) > maxlen)
            {
                start=i;
                maxlen=j-i+1;
            }
        }
    }
    return s.substr(start,maxlen);
}
int main()
{
    string s="rodeeks";
    cout<<longestpal(s);
}
