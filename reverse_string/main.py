
def reverse(s):
	result = ""
	for i in range(len(s)-1,-1,-1):
		result = result + s[i]
	return result

def main():
	s = str(raw_input())
	print reverse(s)
	
if __name__ == "__main__":
    main()