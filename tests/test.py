from classes.project import Project
from flask import Flask

# project1 = Project(client='Vakoms', pm='Any', assignees='Any1')
# project1.save()
# project2 = Project(client='Vakoms1', pm='Any2', assignees='Any3')
# project2.save()
# project4 = Project(client='Vakoms112', pm='Any212', assignees='Any312')
# project4.save()
#
p = Project.get(4)
c = Project.to_list()
c.reverse()
print(p)
q = c[0]
print(q)

# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     test_dict = Project.get(3)
#     test_list = str(Project.to_list())
#     return test_list
#
#
# if __name__ == "__main__":
#     app.run()
