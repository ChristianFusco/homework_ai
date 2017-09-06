import os

root_dir = '.'

# Gets the name of all of the top level directories.
# Returns as a good ol' list
def get_directory_names():
	top_level_dirs = []
	# Hacky bullshit
	# Break after 1 pass for just top level
	for subdirs, dirs, files in os.walk(root_dir):
		top_level_dirs.extend(dirs)
		break
	top_level_dirs.remove('.git')
	return top_level_dirs

# Gives a prompt for picking a directory
# Returns the name of one dir
def get_search_dir(top_level_dirs):
	print('Pick a directory to look into for zipping.\n')
	for i in range(len(top_level_dirs)):
		print(str(i) + '. ' + top_level_dirs[i])
	resp = int(input('\nEnter your choice: '))
	if resp < 0 or resp >= len(top_level_dirs):
		raise ValueException('Input was out of range.')


os.walk(root_dir)

