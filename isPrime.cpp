#include <iostream>

//declare the array we'll dump the primes in
//note that we can just resize the array if it's an issue
int primeArray[100];
int counter = 0;

int isPrime(int);

int main() {
    int x, y;
    bool flag;

    std::cout << "Enter two positive integers: ";
    std::cin >> x >> y;

    std::cout << "The primes between " << x << " and " << y << " are: " << std::endl;

    for (int i = x+1; i < y; ++i)
    {
        //flag number if it is prime
        flag = isPrime(i);
        if (flag == true)
        {
            std::cout << i << std::endl;
        }
    }
    return 0;
}

int isPrime(int n) {

    bool flag = true;

    //edge case, 1 is not prime
    if(n == 1)
        {
            flag = false;
            return flag;
        }

    //the trick here is that the largest value we actually need to check is n/2, otherwise we're repeating the process
    for (int j = 2; j <=n/2; ++j)
    {
        if(n%j == 0 & n != 1)
        {
            flag = false;
            break;
        }
    }
    if (flag == true) {
        primeArray[counter] = n;
        counter++;
    }
    return flag;
}
