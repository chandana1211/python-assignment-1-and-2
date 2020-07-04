import os 
file = 'file1.txt'
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil
path = os.path.join(location, file)  
os.remove(path)  
