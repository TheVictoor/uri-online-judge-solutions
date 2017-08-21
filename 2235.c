#include <stdio.h>
 
int main() {
 
	int a = 0; 
	int b = 0; 
	int c = 0;
	char ch = 'N';
	
	scanf("%d %d %d", &a , &b, &c);
	
	
	if(a == b || b == c || a == c){
		ch = 'S';
	}else if(a + b == c){
		ch = 'S';
	}else if(b + c == a){
		ch = 'S';
	}else if(a + c == b){
		ch = 'S';
	}else {
		ch = 'N';
	}
		
	printf("%c\n", ch);
    return 0;
}