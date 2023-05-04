#include <bits/stdc++.h>
using namespace std;
int main()
{
    int Z0,Zl,N;
    cout<<"Enter Z0 value: ";
    cin>>Z0;
    cout<<"Enter Zl value: ";
    cin>>Zl;
    cout<<"Enter N value: ";
    cin>>N;
    int n=1;
    vector<double> p={sqrt(Z0*Zl)};
    while(n!=N)
    {
        n++;
        vector<double> q;
        double t=0;
        for(int i=0;i<p.size();i++)
        {
         if(i==0)
         t=sqrt(Z0*p[i]);
         else
         t=sqrt(p[i]*p[i-1]);
         q.push_back(t);
        }
        q.push_back(sqrt(p[p.size()-1]*Zl));
        p=q;
    }
    cout<<"The impedance values are: \n";
    for(int i=0;i<p.size();i++)
    {
        cout<<"Characteristic impedance "<<(i+1)<<": "<<p[i]<<"\n";
            }
            return 0;
}