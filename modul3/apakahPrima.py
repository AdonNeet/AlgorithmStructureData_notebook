from math import sqrt as sq
 
def apakahPrima(n):
	n = int(n) ; # Kalau pecahan, dibuang pecahannya.
	assert n>=0; # Hanya menerima bilangan non-negatif.
	primaKecil = [2,3,5,7,11]; 
	bukanPrKecil = [0,1,4,6,8,9,10]; 
	if n in primaKecil:		# cek jika merupakan prima kecil
		# print("\nMerupakan bilangan prima");
		return True;
	elif n in bukanPrKecil:	# cek jika bukan merupakan prima kecil
		# print("\nBukan merupakan bilangan prima");
		return False;
	else:
		for i in range(2,int(sq(n))+1): # mod hingga nilai akar n
			if(n%i == 0 and n != 1):
				# print("\nBukan merupakan bilangan prima");
				return False;
		# ketika lolos dari looping di atas
		# print("\nMerupakan bilangan prima");
		return True;
 
 
