#Create a dictionary of students.
#Ask the user for a key and handle KeyError.

students = {'nithin':'python', 'nandini':'data science', 'shubham' : 'phd', 'anil':'AI', 'santhosh':'management'}

def student_course_finder(student):
    return students[student]

try:
    name = input('Enter student name to find assigned course: ')
    course = student_course_finder(name.lower())
    print(f'Student: {name.title()} is registered in {course} course')

except KeyError:
    print(f"No course information found for '{name}'.")