#include <stdio.h>

typedef enum bool {false, true} bool;

bool IsPal(char *start, char *end){
    if (start > end)
        return true;
    else{
        char first = (char) *start;
        char last = (char) *end;
        return first == last && IsPal(++start, --end);
    }
}

bool IsPalindrome(char *word, size_t length){
    return IsPal(word, word + length - 1);
}
    
int main(){
    char *car = "racecar";
    char *a = "a";
    char *ab = "ab";
    printf("Pal('racecar'): %d\n", IsPalindrome(car, sizeof(car)-1));
    printf("Pal('a'): %d\n", IsPalindrome(a, 1));
    printf("Pal('ab'): %d\n", IsPalindrome(ab,2));
    return 0;
}

