# Declaration
full_name = "Leonardo Rodrigues"
full_name_quotes = """Leonardo
Rodrigues"""
full_name_break = "Leonardo \
Rodrigues"

name = "Leonardo"
last_name = "Rodrigues"

# Formatting
print("Full name:", full_name)
print("Full name (+): " + full_name)
print("Full name (%%): %s" % full_name)
print("Full name (multiple %%): %s %s" % (name, last_name))
print(f"Full name (f and brackets): {name} {last_name}")
print("Full name (.format and brackets): {} {}".format(name, last_name))