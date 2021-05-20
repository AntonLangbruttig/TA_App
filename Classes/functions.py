from django.shortcuts import redirect

from project_app.models import *


def login(name, password):
    # precondition: user with provided username and password exists
    # postcondition: returns True if username and password match those in database, False if either entry is incorrect
    noSuchUser = False
    badPassword = False
    try:
        m = User.objects.get(username=name)
        badPassword = (m.password != password)
    except:
        noSuchUser = True
    if noSuchUser or badPassword:
        return False
    else:
        return True


def formatDays(daysList):
    # precondition: a list is provided containing strings for the days of the week, or an empty list
    # postcondition: a string for the formatted days is returned, or an empty string if an empty list was provided

    formattedDays = ""
    day_options = {"Monday": "M", "Tuesday": "T", "Wednesday": "W", "Thursday": "R", "Friday": "F", "Saturday": "S",
                   "Sunday": "U"}

    for day in daysList:
        formattedDays += day_options[day]

    return formattedDays


def allDays(Days):
    # precondition: a list is provided containing the letters corresponding to the days of the week
    # postcondition: a list of key value pairs is returned for the days of the week and whether the day was provided or not (True/ False)

    day_options = {"M": "Monday", "T": "Tuesday", "W": "Wednesday", "R": "Thursday", "F": "Friday", "S": "Saturday",
                   "U": "Sunday"}
    all_days = {"Monday": False, "Tuesday": False, "Wednesday": False, "Thursday": False, "Friday": False,
                "Saturday": False, "Sunday": False}
    for c in Days:
        all_days[day_options[c]] = True

    return all_days.items()


def createAccount(username="", name="", password="", email="", role="", phone="", address="", officenumber="",
                  officehoursStart=None,
                  officehoursEnd=None, officehoursDays=[], skills=""):
    # precondition: user with provided username does not currently exist with username, password, email, and role entered
    # postcondition: user account is created with a unique username, a password, an email, a role,
    # and a phone number, address and officehours if provided, returns a message if user already exists or required entries are not filled out

    # Need to handle the edge cases for the office hours...

    formattedDays = formatDays(officehoursDays)
    if username != '' and name != '' and password != '' and email != '' and role != '' and officehoursStart is not None and officehoursEnd is not None and formattedDays != '':
        if len(list(User.objects.filter(username=username))) == 0:
            User.objects.create(username=username, name=name, password=password, email=email, role=role, phone=phone,
                                address=address, officenumber=officenumber, officehoursStart=officehoursStart,
                                officehoursEnd=officehoursEnd, officehoursDays=formattedDays, skills=skills)
            if role == "TA":
                user1 = User.objects.get(username=username)
                TA.objects.create(user=user1)
            string = ""
        else:
            string = "User with that username already exists"
    else:
        string = "Please fill out all required entries"
    return string


def editAccount(username="", name="", password="", address="", phone="", officenumber="",
                officehoursStart=None, officehoursEnd=None, officehoursDays=[], skills=""):
    # precodition user must exist
    # post condition the users account information as been updated

    formattedDays = formatDays(officehoursDays)

    User.objects.filter(username=username).update(name=name, password=password, address=address, phone=phone,
                                                  officenumber=officenumber,
                                                  officehoursStart=officehoursStart, officehoursEnd=officehoursEnd,
                                                  officehoursDays=formattedDays, skills=skills)
    return ""


def createCourse(courseId="", name="", credits=""):
    # precondition: course with provided courseid does not currently exist with courseid, coursename, courseschedule, and coursecredits entered
    # postcondition: course is created with unique ID and name, message is returned if course with the id exists or required entries are blank
    if courseId != '' and name != '' and credits != '':
        if len(list(Course.objects.filter(courseid=courseId))) == 0:
            Course.objects.create(courseid=courseId, name=name, credits=credits)
            string = ""
        else:
            string = "Course with that ID already exists"
    else:
        string = "Please fill out all required entries"
    return string


def createSection(course="", sectionid="", types="", scheduleStart=None, scheduleEnd=None, scheduleDays=[]):
    # precondition: course is given and exists, section with provided sectionid does not currently exist with sectionid, type, and sectionschedule entered
    # postcondition: section is created with unique sectionId and course, type, sectionschedule, message is returned if lab with the id exists or required entries are blank

    # Handle the edge cases for the schedule...
    if not scheduleDays:
        string = "Please fill out all required entries"
        return string
    formattedDays = formatDays(scheduleDays)
    if not (not course) and not (not sectionid) and not (not types) and not (not scheduleStart) and not (
    not scheduleEnd) and not (not formattedDays):
        if len(list(Section.objects.filter(sectionid=sectionid))) == 0:
            Section.objects.create(course=course, sectionid=sectionid, type=types, scheduleStart=scheduleStart,
                                   scheduleEnd=scheduleEnd, scheduleDays=formattedDays)
            string = ""
        else:
            string = "Section with that ID already exists"
    else:
        string = "Please fill out all required entries"
    return string


def deleteAccount(username=""):
    # precondition: account with unique username exists
    # postcondition: account with unique username is removed from database and a message is returned if username is not entered,
    # if user with that username does not exist or if the user was successfully deleted
    if username == "":
        string = "Please enter a username"
    elif username not in list(i["username"] for i in User.objects.all().values("username")):
        string = "User with that username does not exist"
    else:
        User.objects.get(username=username).delete()
        string = "User with username " + username + " has been deleted"
    return string


def deleteCourse(courseid=""):
    # precondition: course with unique courseid exists
    # postcondition: course with unique courseid is removed from database and a message is returned if courseid is not entered,
    # if course with that courseid does not exist or if the course was successfully deleted
    if courseid == "":
        string = "Please enter a course ID"
    elif courseid not in list(i["courseid"] for i in Course.objects.all().values("courseid")):
        string = "Course with that ID does not exist"
    else:
        Course.objects.get(courseid=courseid).delete()
        string = "Course with ID " + courseid + " has been deleted"
    return string


def manage_registration(request):
    # precondition: request is provided
    # postcondition: redirect is handled along with the proper session
    dict = {"add_course": '/RegisterCourses/', "assign_instructor": '/AssignInstructor/',
            "register_section": '/RegisterSection/', "assign_TA_to_course": '/AssignTAToCourse/',
            "assign_TA_to_Section": '/AssignTAToSection/'}

    for key in dict:
        if request.POST.get(key) and key != "assign_TA_to_Section":
            request.session["course"] = request.POST[key]
            return redirect(dict[key])
        if key == "assign_TA_to_Section" and request.POST.get(key):
            request.session["sectionid"] = request.POST["assign_TA_to_Section"]
            return redirect(dict[key])


def manage_deletion(request):
    # precondition: request is provided
    # postcondition: confirmation for the deletion is returned
    dict2 = {"delete_course": deleteCourse,
             "rem_TA": unAssignTA, "del_section": deleteSection,
             "rem_TA_sec": unAssignTASection,
             "rem_Ins": unAssignInstructor}
    for key in dict2:
        if request.POST.get(key):
            message = dict2[key](request.POST.get(key))
    return message


def deleteSection(sectionid=""):
    # precondition: section with unique sectionid exists
    # postcondition: section with unique sectionid is removed from database and a message is returned if sectionid is not entered,
    # if section with that sectionid does not exist or if the section was successfully deleted
    if not sectionid:
        string = "Please enter a section ID"
    elif sectionid not in list(i["sectionid"] for i in Section.objects.all().values("sectionid")):
        string = "Section with that ID does not exist"
    else:
        section = Section.objects.get(sectionid=sectionid)
    if section.TA_assigned:
        section.TA_assigned.assignedlabs -= 1
    section.TA_assigned.save()
    section.delete()
    string = "Section with ID " + sectionid + " has been deleted"
    return string


def assignInstructor(courseObj="", instructorUsername=""):
    # precondition: coursid of a current course and a unique instructor
    # postcondition: instructor is assigned to the passed in course
    if not courseObj:
        string = "Please select a course"
    elif not instructorUsername:
        string = "Please select an instructor"
    else:
        string = ""
        courseObj.Instructor = User.objects.get(username=instructorUsername)
        courseObj.save()

    return string


def assignTAtoCourse(courseObj="", TAUsername="", numLabs="", graderstatus=False):
    # precondition: course object, ta username, number of labs, and grader status is provided
    # postcondition: confirmation message for the ta assignment is returned
    if not courseObj:
        message = "Please select a course"
    elif not TAUsername:
        message = "Please select a TA"
    elif not numLabs or int(numLabs) < 0:
        message = "Please enter the number of labs"
    else:
        message = ""
        TA.objects.filter(user__username=(User.objects.get(username=TAUsername)).username).update(course=courseObj,
                                                                                                  numlabs=numLabs,
                                                                                                  assignedlabs=0,
                                                                                                  graderstatus=graderstatus)
    return message


def assignTAtoSection(sectionid="", TAUsername=""):
    # precondition: section id, ta username is provided
    # postcondition: confirmation message after the ta assignment is returned
    if not sectionid:
        message = "Please select a section"
    elif not TAUsername:
        message = "Please select a TA"
    else:
        message = ""
        ta = TA.objects.get(user__username=TAUsername)
        ta.assignedlabs += 1
        ta.save()
        Section.objects.filter(sectionid=sectionid).update(TA_assigned=ta)
    return message


def getCourses():
    # precondition: None
    # postcondition: returns a dictionary with course keys and values are lists of section
    courses = list(Course.objects.all())
    dictionary = {}
    for c in courses:
        dictionary[c] = list(Section.objects.filter(course__courseid=c.courseid))
    return dictionary


def getTAsInCourse(sectionid):
    # precndition: sectionid
    # postcondition: returns a dictionary of TAs in a particular course
    s = Section.objects.get(sectionid=sectionid)
    total = list(TA.objects.filter(course__courseid=s.course.courseid))
    available = []
    for ta in total:
        if ta.assignedlabs < ta.numlabs:
            available.append(ta)
    return available


def unAssignTA(TAUsername):
    # precondition: ta username is provided
    # postcondition: confirmation message after removing the given ta from the course is returned
    user1 = User.objects.get(username=TAUsername)
    ta = TA.objects.get(user=user1)
    courseid = ta.course.courseid
    try:
        section = list(Section.objects.filter(TA_assigned=ta))
        for sect in section:
            unAssignTASection(sect.sectionid)
    except:
        pass
    ta.course = None
    ta.save()
    return ta.user.name + " has been unassigned from course with ID " + courseid


def unAssignTASection(sectionid):
    # precondition: section id is provided
    # postcondition: confirmation message of removing the ta from the section is returned
    section = Section.objects.get(sectionid=sectionid)
    ta = section.TA_assigned
    ta.assignedlabs -= 1
    ta.save()
    section.TA_assigned = None
    section.save()
    return ta.user.name + " has been unassigned from section with ID " + ta.course.courseid + "-" + sectionid


def unAssignInstructor(courseid):
    # precondition: course id is provided
    # postcondition: confirmation message of removing the instructor from the course is returned
    course = Course.objects.get(courseid=courseid)
    instructor = course.Instructor.name
    course.Instructor = None
    course.save()
    return instructor + " has been unassigned from course with ID " + courseid
