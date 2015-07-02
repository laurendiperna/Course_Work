#ex8.py
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it ddin't sing.",
	"So I said goodnight."
)

#python prints the last statement with single quotes except for the
#third statement which it leaves in double quotes, I don't know
#why this is the case, it seems like the answer may be that python
#prints the strings in the most efficient way it can, and does not
#replicate exactly what you wrote.