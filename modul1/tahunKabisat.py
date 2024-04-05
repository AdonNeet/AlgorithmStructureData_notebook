# L200220194
def apakahKabisat(year):
	if(year%4 == 0):
		if(year%400 == 0):
			return True;
		elif(year%100 == 0):
			return False;
		else:
			return True;
	else:
		return False;



print(apakahKabisat(1974));
print(apakahKabisat(1900));
print(apakahKabisat(2100));
print(apakahKabisat(2004));
print(apakahKabisat(112104));
print(apakahKabisat(2400));
