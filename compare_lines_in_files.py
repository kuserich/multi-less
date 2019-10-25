import sys


if len(sys.argv) == 1:
	print("Error: Please specify at least one file")
	print("e.g.   python "+sys.argv[0]+" path/to/file1.txt path/to/other/file.src anotherfile.txt etc.trg")


class MultiLess:

	def __init__(self, files, tabular=False, show_line_numbers=False, show_line_length=False):
		self.all_lines = []
		self.shortest_length = -1
		self.files = files
		self.tabular = tabular
		self.show_line_numbers = show_line_numbers
		self.show_line_length = show_line_length
		self.currentIndex = 0
		self.row_format = "{:<17}"

		for file_path in files:
			file_handler = open(file_path, 'r')
			lines = file_handler.readlines()
			self.all_lines.append(lines)
			if self.shortest_length == -1 or self.shortest_length > len(lines):
				self.shortest_length = len(lines)

	def print_line(self):
		if self.show_line_numbers:
			print("\n[" + str(self.currentIndex) + "]")

		for docs in self.all_lines:
			line_str = ""

			if self.show_line_length:
				line_str += "("
				line_str += str(len(docs[self.currentIndex].split()))
				line_str += ") "

			if self.tabular:
				tokens = docs[self.currentIndex].split()
				line_format = self.row_format * (len(tokens))
				line_str += line_format.format(*tokens)
			else:
				line_str += docs[self.currentIndex][:-1]

			print(line_str)

	def handle_input(self):
		key = input("")

		if key == "q":
			exit()

		if key == "t":
			self.tabular = not self.tabular
			self.print_line()
			print()
			self.handle_input()

		if key == "n":
			self.show_line_numbers = not self.show_line_numbers
			self.handle_input()

		if key == "l":
			self.show_line_length = not self.show_line_length
			self.handle_input()

	def run(self):
		for i in range(printer.shortest_length):
			self.currentIndex = i
			printer.print_line()
			printer.handle_input()


files = []
tabular = False
show_line_numbers = False
show_line_length = False

for arg in sys.argv[1:]:
	if arg == "-t" or arg == "--tabular":
		tabular = True
	elif arg == "-n" or arg == "--line-numbers":
		show_line_numbers = True
	elif arg == "-l" or arg == "--line-length":
		show_line_length = True
	else:
		files.append(arg)


print("Press ENTER to continue or q to quit.")
print("Press t to toggle tabular view.")
print("Press n to toggle line index.")
print("Press l to toggle line length.")
print()

printer = MultiLess(files, tabular=tabular, show_line_numbers=show_line_numbers, show_line_length=show_line_length)
printer.run()
