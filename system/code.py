from parser import parse_input
from dispatcher import dispatch

def main():
	print("Orion awake type exit to terminate")

	while True:
		user_input= input(">>:").strip()

		if user_input.lower() == "exit":
			print("Orion terminated")
			break

		
		command, action, args=parse_input(user_input)
		dispatch(command, action, args)

if __name__ == "__main__":
  main()
