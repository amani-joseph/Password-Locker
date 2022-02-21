def write_to_file(file, data):
     with open(file, 'a') as file:
          print(data)
     file.write(str(data))

def read_from_file(file):
     with open(file, 'r') as file:
          lines = file.readlines()
          print("Usernames & password")
          for line in lines:
               print(f'{line}')
               return lines

def overwrite_file(file, data):
    with open(file, 'w') as file:
        file.write(str(data))