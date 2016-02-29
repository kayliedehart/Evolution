# Echo program to count and echo JSON input from stdin
import sys
import json

class EchoStream:
	buf = None

	def __init__(self):
		self.buf = None
		self.main()

	def nonatomic(self, frag):
		return frag

	def validate(self, frag):
		"""
		Validate input as correct JSON. 
		If there are multiple JSON entities separated by a space, evaluate them separately.
		If there is an incomplete JSON array or object, buffer the fragment and wait to see
		if the object or array completes.
		Return a list of the valid JSON fragments passed in, or False.
		"""
		valid_input = []
		try:
			fragment = json.JSONDecoder().decode(frag)
			valid_input.append(fragment)
			return valid_input
		except ValueError:
			# In case of arrays and objects, check if they're incomplete, and if so, buffer
			# corner case: 4{} should be 4 {}
			if ("{" or "[") in frag:
				self.nonatomic(frag)
			else:
				return False

	def main(self):
		"""
		Get input from stdin, validate, and then echo. When done, return the number of 
		messages received.
		"""
		msg_count = {"count": 0}
		while True:
			try:
				line = sys.stdin.readline()
				echo_frag = self.validate(line)  
				if echo_frag:
					for echo in echo_frag:
						print echo	
						msg_count["count"] += 1
			except KeyboardInterrupt or EOFError:
				print msg_count
				sys.exit()
		


if __name__ == "__main__":
	EchoStream()
	 