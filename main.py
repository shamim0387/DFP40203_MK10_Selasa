import os
import glob


def print_hi(name):
    print(f'Hi, {name}') 

def main():
    filelist = glob.glob("../DFP40203_MK10_Selasa/*.txt")
    for filename in filelist:
        print(filename)

        old_name = "text1.txt"
        new_name = "textrename.txt"

        os.rename(old_name, new_name)



if __name__ == '__main__':
    print_hi('PyCharm')
    main()

