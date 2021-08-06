#include <stdio.h>

int main(){
	int h1, m1, h2, m2, h , m;

	h1 = m1 = h2 = m2 = h = m = 0;

	scanf("%d %d %d %d", &h1, &m1, &h2, &m2);

	
	if(h1 == h2 && m1 == m2){
		printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)\n");
		return 0;
	}else if(h1 == h2){
		if(m1 > m2){
			m1 = 60 - m1;
			m = m1 + m2;
			h = 23;
		}else if(m1 < m2){
			m = m2 - m1;
			h = 0;
		}
		printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
		return 0;
	}else if(h1 > h2){
		h1 = 24 - h1;
		h = h1 + h2;

		if(m1 > m2){
			m1 = 60 - m1;
			m = m1 + m2;
			h--;
		}else if(m1 < m2){
			m = m2 - m1;
		}else{
			m = 0;
		}

		printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
		return 0;
	}else{
		h = h2 - h1;

		if(m1 > m2){
			m1 = 60 - m1;
			m = m1 + m2;
			h--;
		}else if(m1 < m2){
			m = m2 - m1;
		}else{
			m = 0;
		}
		
		printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
		return 0;
	}
	return 0;
}