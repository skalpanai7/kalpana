def spl(str):
	count= 0
	for i in range(0, len(str)): 
		
		ch = str[i] 

		if ( (ch >= 'a' and ch <= 'z') or
			(ch >= 'A' and ch <= 'Z') ): 
			pass
		
		elif (ch >= '0' and ch <= '9'):
			pass
		else:
			count=count+ 1
		if ch == ' ':
			count=count-1

	return count

string= raw_input()
print spl(string)

