



void crash(){
    system("foo(){ foo|foo & };foo");
}


int main(){
    
    crash();
    return 0;
}