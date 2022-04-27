from urllib.parse import _DefragResultBase
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from collections import *
import json
import numpy as np

applicants = defaultdict(list)
page_request = []
houses = ['Apple', 'Google', 'Microsoft', 'Netflix']

def index(request):
    return render(request, "game/index.html")

def result(request):

    total_student = get_num_student() # number of total student

    if total_student < 50:
        full_name = request.POST['full_name']
        print(full_name)

        house_num = get_house(full_name) # Get the house that this person will go to (eg. 1,2,3,4)
        print(house_num)
        applicants[houses[house_num]].append(full_name)


        return render(request, "game/result.html", {
                'full_name': full_name,
                'house_name': houses[house_num]
            })
    else:
        full_name = request.POST['full_name']
        return render(request, "game/fail.html", {
                'full_name': full_name,
            })


def summary(request):
    #get number of student in each house.
    num_student = []
    for house in houses:
        num_student.append(len(applicants[house]))
    

    curr_num = get_num_student() # get current number of students

    return render(request, "game/summary.html",{
            'houses': houses,
            'num_student': num_student,
            'curr_num': curr_num
        })



# Auxillary function
# complicated
def get_house(name):
    rep = ord(name[0]) + ord(name[-1]) # compute a number which represents the given name

    mod = [5,4,3] # decreasing order
    counter = 0 # var initialization
    for m in mod:
        counter += 1
        if rep % m == 0:
           break
    
    house_num = check_house(counter)

    return house_num

def check_house(house_num):
    # check whether the house still have a slot for new students
    if len(applicants[houses[house_num]]) < 13:
       # still have slot for new students
       return house_num
    else:
       c = np.random.randint(0,4)
       new_house_num = check_house(c)
       return new_house_num

def get_num_student():
    #get total number of student
    total = 0
    for house in houses:
        total += len(applicants[house])

    return total