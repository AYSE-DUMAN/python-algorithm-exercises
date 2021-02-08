def make_rug(m, n, s='#'):
	res = []
	for _ in range(0,m):
		row = [s for i in range(0,n)]
		res.append("".join(row))
	return res

def make_rug2(m, n, s="?"):
    return [s * n] * m

def make_rug3(m, n, s="*"):
    	return [s * n for _ in range(m)]

if __name__ == "__main__":
    print(make_rug3(3,5))
    print(make_rug2(3,5,"?"))
    print(make_rug(3,5,"&"))
	
