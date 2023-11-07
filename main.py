import os
import glob


def print_hi(name):
    print(f'Hi, {name}') 

def main():
    filelist = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for filename in filelist:
        print(filename)

        old_name = input("Enter the old name for the file: ")
        new_name = input("Enter the new name for the file: ")


        os.rename(old_name, new_name)



if __name__ == '__main__':
    print_hi('PyCharm')
    main()

