import os

path =  os.path.join('..','materials')
print(path)

current_path = os.getcwd()
print('Current path is ' + current_path)
materials_path = 'C:\\source\\py_foundation\\Automate_the_Boring_Stuff\\materials'
os.chdir(materials_path)
current_path = os.getcwd()
print('New current path is ' + current_path)


new_path = 'C:\\source\\py_foundation\\Automate_the_Boring_Stuff\\materials\\tmp'
if os.path.exists(new_path):
    print(new_path + ' has existed')
else:
    os.makedirs(new_path,exist_ok = False)

total_size = 0
files_names = os.listdir(materials_path)
for name in files_names:
    total_size = total_size + os.path.getsize(os.path.join(materials_path,name))
print(total_size)
