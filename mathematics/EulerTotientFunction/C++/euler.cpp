#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll gcd(ll f,ll s){
	if(f==0)return s;
	return(s%f,f);
}

ll euler(ll n) 
{ 
    // Initialize answer as n
    ll ans = n;  
    
    // Consider all prime factors of n and subtract their 
    // multiples from ans
    for (int p=2; p*p<=n;++p) { 
          
        // Check if p is a prime factor. 
        if (n%p== 0) { 
              
            // If yes, then update n and ans
            while (n%p== 0){
            	n/=p;
            }  
            ans-= ans/p; 
        } 
    } 
  
    // If n has a prime factor greater than sqrt(n) 
    // (There can be at-most one such prime factor) 
    if (n > 1) 
        ans-= ans/n; 
    return ans; 
} 

int main(){
	ll n;
	cin>>n;
	cout<<"The number of coprimes less than n are "<<euler(n)<<"\n";
  return 0; 
} 

/*  Sample Test Cases:

	Input: 8
	Output: The number of coprimes less than 8 are: 4
	
	Explaination:
	
	n = 8 
	Initialize: ans = 8

	2 is a prime factor, so n = n/i = 4, ans=4
	3 is not a prime factor.

	The for loop stops after 3 as 3*3 is not less than or equal
	to 8.

	After for loop, ans = 4, n = 1
	Since n <= 1, ans= 4
*/
