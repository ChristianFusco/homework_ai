import os
from zipfile import ZipFile

def main():
    root_dir = '.'
    # Figure out what files should be zipped
    search_dir = get_search_dir(get_directory_names(root_dir))
    if os.path.isfile(os.path.join(search_dir, '.ziprc')):
        files_to_zip = read_ziprc(search_dir)
    else:
        for subdir, dirs, files in os.walk(search_dir):
            files_to_zip = get_files_to_zip(subdir, files)
            break
    # Update headers since file finding is based on last modified
    # TODO: Make add_headers a module
    os.system('python add_headers.py')

    files_to_zip = [os.path.join(search_dir, file) for file in files_to_zip]
    with ZipFile(search_dir + '.zip','w') as zip:
        # writing each file one by one
        for file in files_to_zip:
            zip.write(file)

def get_directory_names(root_dir):
    """ Gets the name of all of the top level directories.
    Returns as a good ol' list
    """
    top_level_dirs = []
    # Hacky bullshit
    # Break after 1 pass for just top level
    for subdirs, dirs, files in os.walk(root_dir):
        top_level_dirs.extend(dirs)
        break
    top_level_dirs.remove('.git')
    return top_level_dirs



def get_earliest_timestamp(search_dir, files):
    earliest_timestamp = 0
    for file in files:
        timestamp = os.path.getmtime(os.path.join(search_dir, file))
        if timestamp < earliest_timestamp:
            earliest_timestamp = timestamp
    return earliest_timestamp

def get_search_dir(top_level_dirs):
    """
    Gives a prompt for picking a directory
    Returns the name of one dir
    """
    print('Pick a directory to look into for zipping.\n')
    for i in range(len(top_level_dirs)):
        print(str(i) + '. ' + top_level_dirs[i])
    try:
        resp = int(input('\nEnter your choice: '))
        if resp < 0 or resp >= len(top_level_dirs):
            raise ValueError('Input was out of range.')
    except ValueError:
        return get_search_dir(top_level_dirs)
    return top_level_dirs[resp]


def get_files_to_zip(search_dir, files):
    earliest_timestamp = get_earliest_timestamp(search_dir, files)
    files_to_zip = []
    for file in files:
    	file_name = os.path.join(search_dir, file)
        current_timestamp = os.path.getmtime(file_name)
        if earliest_timestamp != current_timestamp:
            files_to_zip.append(file)
    files_to_zip = check_zip_list(files_to_zip)
    if raw_input('\n\nSave list to .ziprc? (Y/n)').upper() != 'N':
        make_ziprc(search_dir, files_to_zip)
    return files_to_zip

def check_zip_list(files_to_zip):
    print('These files will be added to the zip, is that okay?\n')
    for i in range(len(files_to_zip)):
        print(str(i) + '. ' + files_to_zip[i])
    resp = raw_input('(Y/n): ')
    if 'N' == resp.upper():
        return modify_zip_list(files_to_zip)
    return files_to_zip


def make_ziprc(search_dir, files_to_zip):
    with open(os.path.join(search_dir, '.ziprc'), 'w') as out:
        for file in files_to_zip:
            out.write(file + '\n')


def modify_zip_list(files_to_zip):
    print('Enter index of file to remove it.\nEnter \'add\' to add a new file or nothing to exit.')
    resp = raw_input()
    if resp == 'add':
        resp = raw_input('Enter the name of the file relative to ' + search_dir)
        files_to_zip.append(resp)
    try:
        if int(resp) >= 0 and int(resp) < len(files_to_zip):
            del files_to_zip[int(resp)]
    except ValueError:
        print('\nThat\'s not a valid option.')
    return check_zip_list(files_to_zip)

def read_ziprc(search_dir):
    try:
        with open(os.path.join(search_dir, '.ziprc'), 'r') as file:
            files_to_zip = file.read().split('\n')
            # Gets rid of leftover \n line
            files_to_zip.pop()
            return files_to_zip
    except:
        print('No .ziprc file found.  Trying to make one.')
    return None


if __name__ == "__main__":
    main()