#include<bits/stdc++.h>
using namespace std;

int longestCommon(string &s1,string &s2)
{
    int m=s1.size();
    int n=s2.size();
    int maxlen=0;

    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            int len=0;

            while(i+len <m && j+len < n && s1[i+len]==s2[j+len])
            {
                len++;
            }       
            maxlen=max(maxlen,len);
        }
    }
    return maxlen;
}
int main()
{
    string s1="abcdxyz";
    string s2="xyzabcd";
    cout<<longestCommon(s1,s2);
}
