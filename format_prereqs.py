def janky_format_prereq(prereq_str: str) -> str:
	janky_str = prereq_str
	useless_phrases = ["Undergraduate Semester level", "Minimum Grade of C", "Minimum Grade of D"]
	for phrase in useless_phrases:
		janky_str = janky_str.replace(phrase,"")
	return " ".join(janky_str.split()) # trims external and *internal* whitespace (pretty inefficient lol)

prereq_str = input("Enter prerequisite text to be formatted:\n")
print("\n" + janky_format_prereq(prereq_str))