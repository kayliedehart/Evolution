# Echo program to count and echo JSON input from stdin
import sys
import json

class EchoStream:
	def __init__(self):
		self.main()

	def validate(self):
		"""
		Validate input as correct JSON. Return True if it follows JSON specs, False if not.
		"""
		pass

	def main(self):
		"""
		Get input from stdin, validate, and then echo. When done, return the number of 
		messages received.
		"""
		valid_json = True
		msg_count = {"count": 0}
		while valid_json:   
			fragment = raw_input()  
			if self.validate(fragment):
				print fragment  
			else:
				json.dumps[msg_count, sys.stdout]
		sys.exit()
		

if __name__ == "__main__":
	EchoStream()
	 