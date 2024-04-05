# L200220194
from math import sqrt;

def cetakPrima(n):
	n = int(n);
	ans = [];
	assert n >= 0;
	for i in range(1, n+1):
		cek = 0;
		for j in range(2, int(sqrt(i)+1)):
			if(i%j == 0):
				cek += 1;
				break;
		if(cek == 0 and i != 1):
			ans = ans + [i];
		else:
			continue;
	print(tuple(ans));
				

cetakPrima(1000);
