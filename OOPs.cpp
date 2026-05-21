#include<iostream>
using namespace std;

class Customer{
    string name;
    int acc_no;
    int balance;

    public:
    // Default constructor
    // If we don't create a constructor, compiler creates empty one 
    Customer(){
        // def
    } 
    // Parameterized constructor
    Customer(string name, int acc_no, int balance){
        // this - it stores the address of object created
        this->name = name;
        this->acc_no = acc_no;
        this->balance = balance;
    }
    // Constructor overloading
    // Same name constructor but with different parameters
    Customer(string a, int b){
        name = a;
        acc_no = b;
    }
    // Inline Constructor
    inline Customer(string a): name(a){}
};

int main(){
    Customer C;
}