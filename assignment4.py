
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def partOne():
    set2 = [25.81,37.65,30.69,33.64,27.43,34.07,33.95,35.33,33.38, 34.77,33.41,35.27,36.35,35.81,34.35,36.28,38.02,36.30,33.59,31.54,33.66,37.94,36.94,33.33,33.48]
    set1 = [65.5574,95.631,77.9526,85.4456,69.6722,86.5378,86.233,89.73819999999999,84.7852,88.31580000000001,84.86139999999999,89.5858,92.32900000000001,90.9574,87.24900000000001,92.1512,96.5708,92.202,85.3186,80.1116,85.4964,96.3676,93.82759999999999,84.6582,85.0392]
    n=25
    r = np.arange(n)
    width = 0.25

    plt.figure(figsize=(18,13)) 
    plt.bar(r, set2,color = 'g', width = width, label = 'Set 2')
    plt.bar(r + width, set1, color = 'b',  width = width, label = 'Set 1')

    plt.xlabel('Cities', fontsize = 15)
    plt.ylabel('Rainfall in inches', fontsize = 12)
    plt.xticks(r+width/2,['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade'])
    plt.yticks(size = 10)
    plt.title('Rainfall vs Rainfall 10 years after', fontsize = 20)
    plt.legend()
    plt.xticks(rotation=90)
    plt.savefig("PartOne.png")
    plt.show()

def partTwo():
    set2 = [25.81,37.65,30.69,33.64,27.43,34.07,33.95,35.33,33.38, 34.77,33.41,35.27,36.35,35.81,34.35,36.28,38.02,36.30,33.59,31.54,33.66,37.94,36.94,33.33,33.48]
    set1 = [65.5574,95.631,77.9526,85.4456,69.6722,86.5378,86.233,89.73819999999999,84.7852,88.31580000000001,84.86139999999999,89.5858,92.32900000000001,90.9574,87.24900000000001,92.1512,96.5708,92.202,85.3186,80.1116,85.4964,96.3676,93.82759999999999,84.6582,85.0392]
    
    cities = ['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade']
    n=25
    r = np.arange(n)
    width = 0.25

    fig, (plt1, plt2)=plt.subplots(2, figsize=(10,10))
    ax = plt.gca()
    ax.set_ylim([0, 100])

    colours = ['Yellow' if (x == max(set2)) else 'blue' if (x == min(set2)) else 'black' for x in set2 ]
    plt2.bar(r, set2, color = colours)
    plt1.bar(r, set1, color = colours)
    mini = mpatches.Patch(color='blue', label='min')
    maxi = mpatches.Patch(color='yellow', label='max')
    plt2.legend(handles = [mini, maxi])
    plt1.legend(handles = [mini, maxi])
    plt2.set_xlabel('Cities', fontsize = 10)
    plt1.set_xlabel('Cities', fontsize = 10)
    plt2.set_ylabel('Rainfall in inches', fontsize = 10)
    plt1.set_ylabel('Rainfall after 10 years in inches', fontsize = 10)
    plt2.set_xticks(r,['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade'], fontsize = 10,  rotation = 90)
    plt1.set_xticks(r,['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade'], fontsize = 10,  rotation = 90)
    fig.tight_layout()

    plt.savefig("PartTwo.png")
    plt.show()

def partThree():
    x = []
    y = []
    x1 = []
    y1 = []
    for line in open('rainfallSet1.txt', 'r'):
        lines = [i for i in line.split()]
        x.append(lines[0])
        y.append(float(lines[1]))

    for line in open('rainfallSet2.txt', 'r'):
        lines = [i for i in line.split()]
        x1.append(lines[0])
        y1.append(float(lines[1]))

    fig, (plt1, plt2)=plt.subplots(2, figsize=(10,10))
    ax = plt.gca()
    ax.set_ylim([0, 100])
    plt.title("Rainfall vs Rainfall after 10 years")
    plt1.set_xlabel('Cities')
    plt1.set_ylabel('Rainfall in inches')
    plt1.set_yticks([65,75,85,95])
    plt1.set_xticklabels(['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade'], rotation =90)
    plt1.plot(x, y, marker = 'o', c = 'b')
    plt2.set_xlabel('Cities')
    plt2.set_ylabel('Rainfall in inches')
    plt2.set_yticks([15,25,35,45])
    plt2.set_xticklabels(['Akron', 'Albia','Algona', 'Allison', 'Alton', 'AmesW', 'AmesSE', 'Anamosa','Ankeny', 'Atlantic', 'Audubon', 'Beaconsfield', 'Bedford', 'BellePlaine', 'Bellevue', 'Blockton', 'Bloomfield', 'Boone', 'Brighton', 'Britt', 'Buckeye', 'BurlingtonKBUR', 'Burlington','Carroll','Cascade'], rotation =90)
    plt2.plot(x1, y1, marker = 'o', c = 'g')
    fig.tight_layout()
    plt.savefig("PartThree.png")
    plt.show()

def main():
    partOne()
    partTwo()
    partThree()

main()