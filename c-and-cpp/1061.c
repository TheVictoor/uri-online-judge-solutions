#include <stdio.h>

int main(){
	int hi, mi, si;
	int hf, mf, sf;
	int di, df;

	int dd, hh, mm, ss;

	scanf("Dia %d", &di);
	scanf("%d : %d : %d\n", &hi, &mi, &si);

	scanf("Dia %d", &df);
	scanf("%d : %d : %d", &hf, &mf, &sf);

	
	ss = sf - si;
	mm = mf - mi;
	hh = hf - hi;
	dd = df - di;

	if(ss < 0){
		ss += 60;
		mm--;
	}

	if(mm < 0){
		mm += 60;
		hh--;
	}

	if(hh < 0){
		hh += 24;
		dd--;
	}

	printf("%d dia(s)\n", dd);
	printf("%d hora(s)\n", hh);
	printf("%d minuto(s)\n", mm);
	printf("%d segundo(s)\n", ss);

	return 0;

}