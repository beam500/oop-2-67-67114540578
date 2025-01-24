class Student(object):
  student_count = 0

  def __new__(self):
    print('student._new_')

  def __init__(self):
    print('student._init_')
    self.gpa = 4.0
  
  def student_hard(self):
    print('Sir, yes sir.')
