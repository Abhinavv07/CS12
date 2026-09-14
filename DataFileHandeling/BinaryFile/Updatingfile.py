import pickle

def update(filename):
    flag = False
    try:
       
        stfile = open(filename, 'rb+')
        
        while True:
            pos = stfile.tell()
            student = pickle.load(stfile)
            
            if 30 <= student['Marks'] < 40:
                student['Marks'] = 40
                flag = True
                

                stfile.seek(pos)
                pickle.dump(student, stfile)
                
    except EOFError:
       
        stfile.close()
    except IOError:
        print("Error in file")
        
    if not flag:
        print("Student not found")
        
def read(file):
    stfile = open(file, 'rb+')
    while True:
        student = pickle.load(stfile)
        print(student)

