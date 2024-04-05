# L200220194
def formatRupiah(num):
	num = str(num);
	ans = "";
	post = 0;
	for i in num[::-1]:
		if(post%3 == 0 and post != 0):
			ans = "." + ans;
		ans = i + ans;
		post += 1;
	ans = "Rp " + ans;
	print(ans);
