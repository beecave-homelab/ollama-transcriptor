def main():
	message(state, msg)

def message(state, msg):
	if state == "succes":
		print(colors.GREEN + msg + colors.END)
	elif state == "warning":
		print(colors.WARNING + msg + colors.END)
	elif state == "header":
		print(colors.HEADER + msg + colors.END)
	elif state == "underline":
		print(colors.UNDERLINE + msg + colors.END)
	elif state == "bold":
		print(colors.BOLD + msg + colors.END)
	elif state == "info":
		print(colors.RED + msg + colors.END)
	else:
		print(msg)

class colors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

if __name__ == "__main__":
	main()
	