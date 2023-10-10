def display_emp(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("salary"))

display_emp(name="hari",dept="hr",n_place="ekm",location="ktm",salary=240000)

#create a function display_student and print student name and course
#display_student(name="hari",course="django",roll=1000,gender="male")

def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))
display_student(name="hari",course="django",roll=1000,gender="male")



