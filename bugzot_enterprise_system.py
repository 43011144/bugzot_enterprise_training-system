from abc import ABC, abstractmethod
from threading import Lock, Thread
import logging
import time
from tkinter import *
from tkinter import messagebox, ttk, scrolledtext
import unittest
import cProfile
import pstats
import sys


# 1.1.Domain Model Implementation(Organisation=Provides Professional training certifications)
class Learner:
    """Details that every student should contain"""

    def __init__(self, learner_name, learner_surname, learner_id, learner_email, phone_number):

        """Validating student details"""
        if learner_name == "":
            raise ValueError("Please enter a  name")

        if learner_surname == "":
            raise ValueError("Please enter a surname")

        if learner_id == "":
            raise ValueError("The ID is empty")

        if not learner_email.endswith("@gmail.com"):
            raise ValueError("Correct email must end with '@gmail.com'")

        if phone_number == "" or len(phone_number) != 10:
            raise ValueError("Phone number must not be empty and must contain 10 digits")

        if not phone_number.isdigit():
            raise ValueError("Phone number must be in digits")

        """Adding learner variables to self so they can work and be stored within the current working object"""
        self.learner_name = learner_name
        self.learner_surname = learner_surname
        self.learner_id = learner_id
        self.learner_email = learner_email
        self.phone_number = phone_number

    def learner_info(self):
        print(f"Learner's ID: {self.learner_id}\n"
              f"Name: {self.learner_name}\n"
              f"Surname: {self.learner_surname}\n"
              f"Email: {self.learner_email}\n"
              f"phoneNumber: {self.phone_number}\n")


print("----------Learner Data----------")
# Testing learner Object
learner = Learner(learner_name="Michael", learner_surname="Harrington", learner_id=1, learner_email="123456@gmail.com",
                  phone_number="1234567891")
learner.learner_info()


class Course:
    def __init__(self, course_name, course_id, course_duration, course_fee, course_instructor, course_capacity):

        """Validating course details"""
        if course_name == "":
            raise ValueError("Please enter a course name")
        if course_id == "":
            raise ValueError("Please enter a course ID")
        if course_duration == "":
            raise ValueError("Please enter a course duration")
        if course_duration <= 0:
            raise ValueError("Course duration must be greater than 0")
        if course_fee <= 0:
            raise ValueError("Course fee must be greater than 0")
        if course_instructor == "":
            raise ValueError("Please enter a course instructor")
        if course_capacity <= 0:
            raise ValueError("Course capacity must be greater than 0")

        self.course_name = course_name
        self.course_id = course_id
        self.course_duration = course_duration
        self.course_fee = course_fee
        self.course_instructor = course_instructor
        self.course_capacity = course_capacity

    def course_info(self):
        print(f"Course ID: {self.course_id}\n"
              f"Course Duration: {self.course_duration}\n"
              f"Course Fee: {self.course_fee}\n"
              f"Course Instructor: {self.course_instructor}\n"
              f"courseName: {self.course_name}\n"
              f"course Capacity: {self.course_capacity}\n")


print("----------Course Data----------")
# Testing course object
course = Course(course_name="Software Engineering", course_id=3, course_duration=3, course_fee=7000,
                course_instructor="Martin", course_capacity=1000)
course.course_info()

"""aggregation= was chosen because a student is part of the organization but can still exist without the organization"""


class Registration:
    def __init__(self, learner, course, registration_date, payment_status, registration_status):
        """
       Validating Registration details only because the learner and course objects are already validated in their respective classes
       """
        if registration_date == "":
            raise ValueError("Please enter a registration date")
        if payment_status == "":
            raise ValueError("Please enter a payment date")
        if not isinstance(learner, Learner):
            raise ValueError("Registration is supposed to receive learner info. through Learner object")
        if not isinstance(course, Course):
            raise ValueError("Registration is supposed to receive course info. through Course object")
        if payment_status == "Paid":
            print(f"{learner.learner_name} has successfully registered!")
        if registration_status == "Good":
            print(f"{learner.learner_name} has successfully registered!")

        self.learner = learner
        self.course = course
        self.registration_date = registration_date
        self.payment_status = payment_status
        self.registration_status = registration_status

    """Registration details will prove"""

    def registration_info(self):
        print(f"Learner Name:{self.learner.learner_name}\n"
              f"Course Name:{self.course.course_name}\n"
              f"Registration Date:{self.registration_date}\n"
              f"Payment Status:{self.payment_status}\n"
              f"Registration Status:{self.registration_status}\n")


print("----------Registration Data----------")
# Testing object: Passing learner and course object to the registration object:
registration = Registration(learner, course, "12 February 2015", "Paid", "Good")

"""aggregation(object injection)"""


class Assessment:
    def __init__(self, learner, course, registration, assessment_date, assessment_status):
        """Validating Assessment details"""
        if assessment_date == "":
            raise ValueError("Please enter a assessment date")
        if assessment_status == "":
            raise ValueError("Please enter a assessment status")
        if not isinstance(learner, Learner):
            raise ValueError("Assessment is supposed to receive learner info. through Learner object")
        if not isinstance(course, Course):
            raise ValueError("Assessment is supposed to receive course info. through Course object")
        if not isinstance(registration, Registration):
            raise ValueError("Assessment is supposed to receive registration info. through Registration object")
        if registration.payment_status != "Paid":
            raise ValueError("Learner cannot write assessment")
        if assessment_status != "good":
            raise ValueError("Learner cannot write assessment")
        else:
            print(f"{learner.learner_name} can write assessment!")

        self.learner = learner
        self.course = course
        self.registration = registration
        self.assessment_date = assessment_date
        self.assessment_status = assessment_status

    def assessment_info(self):
        print(f"Learner Name:{self.learner.learner_name}\n"
              f"Course Name:{self.course.course_name}\n"
              f"Assessment Date:{self.assessment_date}\n"
              f"Assessment Status:{self.assessment_status}\n")
        pass


print("----------Assessment Data----------")
assessment = Assessment(learner, course, registration, "12 November 2015", "good")

"""aggregation(object injection)"""


class SupportTicket:
    def __init__(self, learner, message_description, message_sent, message_date, message_status):
        """Validating SupportTicket details"""
        if not isinstance(learner, Learner):
            raise ValueError("SupportTicket is supposed to receive learner info")
        if message_description == "":
            raise ValueError("Please enter a message description")
        if message_date == "":
            raise ValueError("Please enter a message date")
        if message_status == "":
            raise ValueError("Please enter a message status")
        if message_sent == "sent":
            print(f"{learner.learner_name} has successfully sent a message!")
        elif message_sent != "sent":
            raise ValueError("Please send a message")

        self.learner = learner
        self.message_description = message_description
        self.message_date = message_date
        self.message_sent = message_sent
        self.message_status = message_status

    def message_info(self):
        print(f"Learner Name:{self.learner.learner_name}\n"
              f"Message Description:{self.message_description}\n"
              f"Message Date:{self.message_date}\n"
              f"Message Sent:{self.message_sent}\n")


print("----------Support Ticket Data----------")
support_ticket = SupportTicket(learner, message_description="Module content not loading", message_sent="sent",
                               message_date="29 November 2017", message_status="sent")


# 1.2 Design Pattern Implementation
# Singleton Design Pattern:
class Configuration(ABC):
    @abstractmethod
    def config_settings(self):
        pass


class SingletonConfiguration(Configuration):
    __instance = None

    @staticmethod
    def get_config_instance():
        if SingletonConfiguration.__instance is None:
            print("----------Configuration settings----------")
            SingletonConfiguration(0, "user settings", "login configurations", "course configurations",
                                   "registration configurations")
        return SingletonConfiguration.__instance

    def __init__(self, user_id, user_settings, login_config, course_config, registration_view):
        if SingletonConfiguration.__instance is not None:
            raise Exception("A configuration object is already created, and cannot be created again!")
        else:
            self.user_id = user_id
            self.user_settings = user_settings
            self.login_config = login_config
            self.course_config = course_config
            self.registration_view = registration_view
            # creating an object and it is going to be stored
            SingletonConfiguration.__instance = self

    @staticmethod
    def config_settings(**kwargs):
        print(f"User id: {SingletonConfiguration.__instance.user_id}\n"
              f"User settings: {SingletonConfiguration.__instance.user_settings}\n"
              f"Login details: {SingletonConfiguration.__instance.login_config}\n"
              f"Course details: {SingletonConfiguration.__instance.course_config}\n"
              f"Registration details: {SingletonConfiguration.__instance.registration_view}\n"
              f"Singleton Configuration Object Successful\n")


# Factory Design Pattern
class TechnicalSupportTicket(ABC):

    @abstractmethod
    def support_ticket(self):
        pass


class CourseSupportTicket(TechnicalSupportTicket):
    def __init__(self):
        self.support = "Course Support Ticket Created!"

    def support_ticket(self):
        print("Organisation has Course support ticket")


class AssessmentSupportTicket(TechnicalSupportTicket):
    def __init__(self):
        self.support = "Assessment Support Ticket Created!"

    def support_ticket(self):
        print("Organisation has Assessment support ticket")


class RegistrationSupportTicket(TechnicalSupportTicket):
    def __init__(self):
        self.support = "Registration Support Ticket Created!"

    def support_ticket(self):
        print("Organisation has Registration support ticket")


class SupportTicketFactory:
    @staticmethod
    def organisation_support_ticket(ticket_type):
        match ticket_type:
            case "Course":
                return CourseSupportTicket()
            case "Assessment":
                return AssessmentSupportTicket()
            case "Registration":
                return RegistrationSupportTicket()
            case _:
                raise ValueError("Invalid Support Ticket Type")


# Strategy pattern
class AssessmentResult(ABC):
    @abstractmethod
    def calculate_assessment_result(self):
        pass


class Average(AssessmentResult):
    def __init__(self, marks):
        self.marks = marks

    def calculate_assessment_result(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        return average_marks


class Percentage(AssessmentResult):
    def __init__(self, obtained_marks, total_marks):
        self.obtained_marks = obtained_marks
        self.total_marks = total_marks

    def calculate_assessment_result(self):
        percentage = (self.obtained_marks / self.total_marks) * 100
        return percentage


class Classification(AssessmentResult):
    def __init__(self, percentage_mark):
        self.percentage_mark = percentage_mark

    def calculate_assessment_result(self):
        if self.percentage_mark >= 80:
            print("Passed with Distinction. A+")
        elif self.percentage_mark >= 70:
            print("Passed very well. B+")
        elif self.percentage_mark >= 60:
            print("Pass well. C+")
        elif self.percentage_mark >= 50:
            print("You Passed D+")
        else:
            print("You failed. E+")


class Result:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate_assessment(self):
        return self.strategy.calculate_assessment_result()


# 3.1 Bugzot monitoring subsystem:
# Whenever logging is used, the information is recorded in bugzot_log.txt
logging.basicConfig(
    filename="bugzot_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# records normal events
def bugzot_log_event(message):
    logging.info(message)


# records warnings
def bugzot_log_warning(message):
    logging.warning(message)


# records errors
def bugzot_log_error(message):
    logging.error(message)


# Deliverable 2: Large-Scale processing and concurrent operations
# 2.1. Registration Processing Engine
class RegistrationProcessingEngine:
    def __init__(self):
        self.course = course

        # Stores successful and unsuccessful registrations
        self.registration_records = []
        self.failed_registrations = []

        # Lock protects shared registrations
        self.registrations_lock = Lock()

        # logging engine initialization
        bugzot_log_event("Registration Processing Engine initialized")

    def process_registration_records(self, learner, course):
        """Validation learner and course objects"""

        # performance monitoring
        start_time = time.time()

        if not isinstance(learner, Learner):
            message = "Invalid learner information"
            self.failed_registrations.append(("Unknown", message))
            bugzot_log_error(f"Validation failure: {message}")
            return False, message

        if not isinstance(course, Course):
            message = "Invalid course information"
            self.failed_registrations.append(("Unknown", message))
            bugzot_log_error(f"Validation failure: {message}")
            return False, message

        # Protecting shared resources
        with self.registrations_lock:

            # Checking for duplicate registration
            for registration in self.registration_records:

                if registration.learner.learner_id == learner.learner_id:
                    message = (f"Registration failed for: "
                               f"Duplicate registration: "
                               f"{learner.learner_name}")

                    self.failed_registrations.append(
                        (learner.learner_name, message)
                    )

                    bugzot_log_warning(
                        f"Duplicate registration attempt - "
                        f"Learner ID: {learner.learner_id}, "
                        f"Learner: {learner.learner_name}"
                    )

                    return False, message

            # Checking for course capacity
            if len(self.registration_records) >= course.course_capacity:
                message = (f"Registration failed for: "
                           f"Course capacity reached: "
                           f"{learner.learner_name}")

                self.failed_registrations.append(
                    (learner.learner_name, message)
                )

                bugzot_log_warning(
                    f"Course capacity violation - "
                    f"Learner ID: {learner.learner_id}, "
                    f"Course: {course.course_name}, "
                    f"Capacity: {course.course_capacity}"
                )

                return False, message

            # Creating a successful registration
            new_registration = Registration(
                learner,
                course,
                "15 August 2017",
                "Paid",
                "Good"
            )

            # Storing a successful registration
            self.registration_records.append(new_registration)

            bugzot_log_event(
                f"Registration Success | {learner.learner_name} "
                f"{learner.learner_surname} registered successfully."
            )

            duration = time.time() - start_time
            bugzot_log_event(f"Registration time: {duration:.3f} seconds")

            message = (f"Registration successful for: "
                       f"{learner.learner_name} "
                       f"{learner.learner_surname}")

            return True, message

    def process_concurrent_requests(self, learner, course):
        """Processes one registration request in a separate thread"""
        success, message = self.process_registration_records(learner, course)
        if success:
            print(f"[Success] Concurrent {learner.learner_name} registered ")
        else:
            print(f"[Rejected] Concurrent {learner.learner_name} rejected: {message} ")

    def registration_summary(self):
        print("-----------Registration Processing Summary:----------")

        print(
            f"Successful Registrations: "
            f"{len(self.registration_records)}"
        )

        print(
            f"Unsuccessful Registrations: "
            f"{len(self.failed_registrations)}"
        )

        print("-----------Successful Registrations:----------")

        for registration in self.registration_records:
            print(
                f"Learner: {registration.learner.learner_name} "
                f"Surname: {registration.learner.learner_surname} "
                f"ID: {registration.learner.learner_id} "
                f"Status: {registration.registration_status}"
            )

        print("-----------Unsuccessful Registrations:----------")

        for learner_name, message in self.failed_registrations:
            print(
                f"Learner: {learner_name} "
                f"Status: Failed "
                f"Reason: {message}"
            )


# 3.2 Application Performance Monitoring
def generate_performance_report(engine):
    """Generates a performance report from Bugzot monitoring data"""

    bugzot_log_event("=== PERFORMANCE REPORT GENERATED ===")

    total_success = len(engine.registration_records)
    total_failed = len(engine.failed_registrations)
    total_attempts = total_success + total_failed

    # Log summary statistics
    bugzot_log_event(f"Total Registrations: {total_success}")
    bugzot_log_event(f"Failed Registrations: {total_failed}")

    if total_attempts > 0:
        success_rate = (total_success / total_attempts) * 100
        bugzot_log_event(f"Success Rate: {success_rate:.1f}%")

    bugzot_log_event("=== END PERFORMANCE REPORT ===")

    return {
        'total_success': total_success,
        'total_failed': total_failed,
        'success_rate': (total_success / total_attempts * 100) if total_attempts > 0 else 0
    }


# Deliverable 4 :4.1
# Create main window
window = Tk()
window.title("Bugzot Training Organisation management System")
window.geometry("700x700")
window.configure(bg='#f0f0f0')

# Store registration engine for report viewing
engine = RegistrationProcessingEngine()

# Store current data
current_learner = None
current_course = None

# Create main container

main_container = Frame(window, bg='#f0f0f0')
main_container.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Create header
header_frame = Frame(main_container, bg='#f0f0f0')
header_frame.pack(fill=X, pady=(0, 10))

title_label = Label(
    header_frame,
    text="BUGZOT TRAINING ORGANISATION",
    font=('Arial', 18, 'bold'),
    bg='#f0f0f0'
)
title_label.pack()

subtitle_label = Label(
    header_frame,
    text="Professional Training Certification Management System",
    font=('Arial', 10),
    bg='#f0f0f0'
)
subtitle_label.pack()

# Create notebook for tabs
notebook = ttk.Notebook(main_container)
notebook.pack(fill=BOTH, expand=True, pady=10)

# LEARNER REGISTRATION TAB
learner_tab = Frame(notebook)
notebook.add(learner_tab, text="Learner Registration")

# Left side - Registration form
form_frame = LabelFrame(learner_tab, text="Learner Registration Form", padx=10, pady=10)
form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

# Form fields
fields = [
    ("learner_name", "Name:"),
    ("learner_surname", "Surname:"),
    ("learner_id", "ID:"),
    ("learner_email", "Email:"),
    ("phone_number", "Phone:")
]

reg_entries = {}

for i, (field, label) in enumerate(fields):
    Label(form_frame, text=label).grid(row=i, column=0, sticky=W, pady=5)
    entry = Entry(form_frame, width=30)
    entry.grid(row=i, column=1, sticky=W, pady=5, padx=(10, 0))
    reg_entries[field] = entry

# Course selection
Label(form_frame, text="Course:").grid(row=len(fields), column=0, sticky=W, pady=5)
course_var = StringVar()
course_combo = ttk.Combobox(form_frame, textvariable=course_var, width=27)
course_combo['values'] = ["Software Engineering", "Data Science", "Cloud Computing", "Cybersecurity"]
course_combo.grid(row=len(fields), column=1, sticky=W, pady=5, padx=(10, 0))


# Register button
def register_learner():
    """Handle learner registration"""
    try:
        # Get form data
        name = reg_entries['learner_name'].get()
        surname = reg_entries['learner_surname'].get()
        learner_id = reg_entries['learner_id'].get()
        email = reg_entries['learner_email'].get()
        phone = reg_entries['phone_number'].get()
        course_name = course_var.get()

        # Validate
        if not all([name, surname, learner_id, email, phone, course_name]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Create learner object
        learner_obj = Learner(name, surname, learner_id, email, phone)

        # Create course object (simplified for demo)
        course_obj = Course(course_name, 999, 3, 5000, "Instructor", 100)

        # Process registration
        success, message = engine.process_registration_records(learner_obj, course_obj)

        if success:
            # Add to treeview
            reg_tree.insert("", END, values=(
                learner_id, name, surname, email, course_name
            ))
            messagebox.showinfo("Success", f"Learner {name} registered successfully!")
            # Clear form
            for entry in reg_entries.values():
                entry.delete(0, END)
            course_var.set("")
            status_bar.config(text=f"Registered: {name}")
        else:
            messagebox.showerror("Registration Failed", message)
            status_bar.config(text=f"Registration failed: {message}")

    except ValueError as e:
        messagebox.showerror("Validation Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


reg_button = Button(form_frame, text="Register Learner", command=register_learner)
reg_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=20)

# Right side - Registration list
list_frame = LabelFrame(learner_tab, text="Registered Learners", padx=10, pady=10)
list_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Treeview for registrations
columns = ("ID", "Name", "Surname", "Email", "Course")
reg_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)

for col in columns:
    reg_tree.heading(col, text=col)
    reg_tree.column(col, width=100)

scrollbar = ttk.Scrollbar(list_frame, orient=VERTICAL, command=reg_tree.yview)
reg_tree.configure(yscrollcommand=scrollbar.set)

reg_tree.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# COURSE MANAGEMENT TAB
course_tab = Frame(notebook)
notebook.add(course_tab, text="Course Management")

# Left side - Course form
course_form_frame = LabelFrame(course_tab, text="Course Management Form", padx=10, pady=10)
course_form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

# Course fields
course_fields = [
    ("course_name", "Course Name:"),
    ("course_id", "Course ID:"),
    ("course_duration", "Duration (months):"),
    ("course_fee", "Fee (ZAR):"),
    ("course_instructor", "Instructor:"),
    ("course_capacity", "Capacity:")
]

course_entries = {}

for i, (field, label) in enumerate(course_fields):
    Label(course_form_frame, text=label).grid(row=i, column=0, sticky=W, pady=5)
    entry = Entry(course_form_frame, width=30)
    entry.grid(row=i, column=1, sticky=W, pady=5, padx=(10, 0))
    course_entries[field] = entry


def add_course():
    """Handle adding a new course"""
    try:
        # Get form data
        name = course_entries['course_name'].get()
        course_id = course_entries['course_id'].get()
        duration = course_entries['course_duration'].get()
        fee = course_entries['course_fee'].get()
        instructor = course_entries['course_instructor'].get()
        capacity = course_entries['course_capacity'].get()

        # Validate
        if not all([name, course_id, duration, fee, instructor, capacity]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Create course object
        course_obj = Course(name, course_id, int(duration), float(fee), instructor, int(capacity))

        # Add to treeview
        course_tree.insert("", END, values=(
            course_id, name, duration, fee, instructor, capacity
        ))

        messagebox.showinfo("Success", f"Course {name} added successfully!")
        # Clear form
        for entry in course_entries.values():
            entry.delete(0, END)
        status_bar.config(text=f"Added course: {name}")

    except ValueError as e:
        messagebox.showerror("Validation Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def clear_course_form():
    """Clear course form fields"""
    for entry in course_entries.values():
        entry.delete(0, END)


# Buttons
btn_frame = Frame(course_form_frame)
btn_frame.grid(row=len(course_fields), column=0, columnspan=2, pady=20)

add_course_btn = Button(btn_frame, text="Add Course", command=add_course)
add_course_btn.pack(side=LEFT, padx=5)

clear_course_btn = Button(btn_frame, text="Clear", command=clear_course_form)
clear_course_btn.pack(side=LEFT, padx=5)

# Right side - Course list
course_list_frame = LabelFrame(course_tab, text="Available Courses", padx=10, pady=10)
course_list_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Treeview for courses
course_columns = ("ID", "Name", "Duration", "Fee", "Instructor", "Capacity")
course_tree = ttk.Treeview(course_list_frame, columns=course_columns, show="headings", height=15)

for col in course_columns:
    course_tree.heading(col, text=col)
    course_tree.column(col, width=100)

course_scrollbar = ttk.Scrollbar(course_list_frame, orient=VERTICAL, command=course_tree.yview)
course_tree.configure(yscrollcommand=course_scrollbar.set)

course_tree.pack(side=LEFT, fill=BOTH, expand=True)
course_scrollbar.pack(side=RIGHT, fill=Y)

# SUPPORT TICKET TAB
ticket_tab = Frame(notebook)
notebook.add(ticket_tab, text="Support Tickets")

# Left side - Ticket form
ticket_form_frame = LabelFrame(ticket_tab, text="Create Support Ticket", padx=10, pady=10)
ticket_form_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

# Ticket fields
ticket_fields = [
    ("learner_id", "Learner ID:"),
    ("message_description", "Description:"),
    ("message_date", "Date:"),
    ("message_status", "Status:")
]

ticket_entries = {}

for i, (field, label) in enumerate(ticket_fields):
    Label(ticket_form_frame, text=label).grid(row=i, column=0, sticky=W, pady=5)

    if field == "message_description":
        entry = Text(ticket_form_frame, height=5, width=30)
        entry.grid(row=i, column=1, sticky=W, pady=5, padx=(10, 0))
        ticket_entries[field] = entry
    else:
        entry = Entry(ticket_form_frame, width=30)
        entry.grid(row=i, column=1, sticky=W, pady=5, padx=(10, 0))
        ticket_entries[field] = entry

# Ticket type
Label(ticket_form_frame, text="Ticket Type:").grid(row=len(ticket_fields), column=0, sticky=W, pady=5)
ticket_type_var = StringVar(value="Course")
ticket_type_combo = ttk.Combobox(ticket_form_frame, textvariable=ticket_type_var, width=27)
ticket_type_combo['values'] = ["Course", "Assessment", "Registration"]
ticket_type_combo.grid(row=len(ticket_fields), column=1, sticky=W, pady=5, padx=(10, 0))


def submit_ticket():
    """Handle support ticket submission"""
    try:
        # Get form data
        learner_id = ticket_entries['learner_id'].get()
        description = ticket_entries['message_description'].get("1.0", END).strip()
        date = ticket_entries['message_date'].get()
        status = ticket_entries['message_status'].get()
        ticket_type = ticket_type_var.get()

        # Validate
        if not all([learner_id, description, date, status]):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Create ticket
        ticket_id = f"TKT-{int(time.time())}"

        # Add to treeview
        ticket_tree.insert("", END, values=(
            ticket_id, learner_id, description[:30] + "...", date, status, ticket_type
        ))

        messagebox.showinfo("Success", f"Support ticket {ticket_id} created successfully!")
        # Clear form
        for field, entry in ticket_entries.items():
            if field == "message_description":
                entry.delete("1.0", END)
            else:
                entry.delete(0, END)
        ticket_type_var.set("Course")
        status_bar.config(text=f"Created ticket: {ticket_id}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


submit_btn = Button(ticket_form_frame, text="Submit Ticket", command=submit_ticket)
submit_btn.grid(row=len(ticket_fields) + 1, column=0, columnspan=2, pady=20)

# Right side - Ticket list
ticket_list_frame = LabelFrame(ticket_tab, text="Support Tickets", padx=10, pady=10)
ticket_list_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Treeview for tickets
ticket_columns = ("Ticket ID", "Learner ID", "Description", "Date", "Status", "Type")
ticket_tree = ttk.Treeview(ticket_list_frame, columns=ticket_columns, show="headings", height=15)

for col in ticket_columns:
    ticket_tree.heading(col, text=col)
    ticket_tree.column(col, width=100)

ticket_scrollbar = ttk.Scrollbar(ticket_list_frame, orient=VERTICAL, command=ticket_tree.yview)
ticket_tree.configure(yscrollcommand=ticket_scrollbar.set)

ticket_tree.pack(side=LEFT, fill=BOTH, expand=True)
ticket_scrollbar.pack(side=RIGHT, fill=Y)

# REPORT VIEWING TAB
report_tab = Frame(notebook)
notebook.add(report_tab, text="Reports")

# Report controls
control_frame = Frame(report_tab)
control_frame.pack(fill=X, pady=5)

Label(control_frame, text="Report Type:").pack(side=LEFT, padx=5)
report_type_var = StringVar(value="Registration Summary")
report_combo = ttk.Combobox(control_frame, textvariable=report_type_var, width=20)
report_combo['values'] = ["Registration Summary", "Performance Report", "System Log"]
report_combo.pack(side=LEFT, padx=5)


def generate_report():
    """Generate and display reports"""
    report_type = report_type_var.get()

    report_text.delete("1.0", END)

    if report_type == "Registration Summary":
        report_text.insert(END, "=== REGISTRATION SUMMARY ===\n\n")
        report_text.insert(END, f"Total Successful Registrations: {len(engine.registration_records)}\n")
        report_text.insert(END, f"Total Failed Registrations: {len(engine.failed_registrations)}\n\n")

        report_text.insert(END, "Successful Registrations:\n")
        report_text.insert(END, "-" * 40 + "\n")
        for reg in engine.registration_records:
            report_text.insert(END,
                               f"  {reg.learner.learner_name} {reg.learner.learner_surname} (ID: {reg.learner.learner_id})\n")

        report_text.insert(END, "\nFailed Registrations:\n")
        report_text.insert(END, "-" * 40 + "\n")
        for name, reason in engine.failed_registrations:
            report_text.insert(END, f"  {name}: {reason}\n")

    elif report_type == "Performance Report":
        report = generate_performance_report(engine)
        report_text.insert(END, "=== PERFORMANCE REPORT ===\n\n")
        report_text.insert(END, f"Total Successful: {report['total_success']}\n")
        report_text.insert(END, f"Total Failed: {report['total_failed']}\n")
        report_text.insert(END, f"Success Rate: {report['success_rate']:.1f}%\n")

    elif report_type == "System Log":
        report_text.insert(END, "=== SYSTEM LOG ===\n\n")
        try:
            with open("bugzot_log.txt", "r") as f:
                lines = f.readlines()
                for line in lines[-50:]:
                    report_text.insert(END, line)
        except FileNotFoundError:
            report_text.insert(END, "Log file not found.")


generate_btn = Button(control_frame, text="Generate Report", command=generate_report)
generate_btn.pack(side=LEFT, padx=10)

# Report display area
report_frame = LabelFrame(report_tab, text="Report Output", padx=10, pady=10)
report_frame.pack(fill=BOTH, expand=True, pady=10)

report_text = scrolledtext.ScrolledText(report_frame, height=20, width=80)
report_text.pack(fill=BOTH, expand=True)

# Status bar
status_bar = Label(window, text="Ready", relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)
window.mainloop()


# Deliverable 5.1: Automated Testing
class TestBugzotSystem(unittest.TestCase):
    """Automated tests for Bugzot Training Organisation System"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_learner = Learner(
            learner_name="Test",
            learner_surname="User",
            learner_id="T001",
            learner_email="testuser@gmail.com",
            phone_number="0821234567"
        )

        self.test_course = Course(
            course_name="Test Course",
            course_id="C001",
            course_duration=3,
            course_fee=5000,
            course_instructor="Test Instructor",
            course_capacity=5
        )

        self.engine = RegistrationProcessingEngine()

    def test_learner_validation_valid(self):
        """Test that valid learner data creates object successfully"""
        learner = Learner("John", "Doe", "L001", "john@gmail.com", "0821234567")
        self.assertEqual(learner.learner_name, "John")
        self.assertEqual(learner.learner_surname, "Doe")
        self.assertEqual(learner.learner_id, "L001")

    def test_learner_validation_invalid_email(self):
        """Test that invalid email raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Learner("John", "Doe", "L001", "john@yahoo.com", "0821234567")
        self.assertIn("Correct email must end with '@gmail.com'", str(context.exception))

    def test_learner_validation_invalid_phone(self):
        """Test that invalid phone number raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Learner("John", "Doe", "L001", "john@gmail.com", "082123")
        self.assertIn("Phone number must not be empty and must contain 10 digits", str(context.exception))

    def test_course_validation_valid(self):
        """Test that valid course data creates object successfully"""
        course = Course("Python", "C002", 6, 8000, "Dr. Smith", 20)
        self.assertEqual(course.course_name, "Python")
        self.assertEqual(course.course_fee, 8000)
        self.assertEqual(course.course_capacity, 20)

    def test_course_validation_invalid_fee(self):
        """Test that invalid course fee raises ValueError"""
        with self.assertRaises(ValueError) as context:
            Course("Python", "C002", 6, -100, "Dr. Smith", 20)
        self.assertIn("Course fee must be greater than 0", str(context.exception))

    def test_registration_successful(self):
        """Test successful registration processing"""
        success, message = self.engine.process_registration_records(self.test_learner, self.test_course)
        self.assertTrue(success)
        self.assertEqual(len(self.engine.registration_records), 1)

    def test_registration_duplicate(self):
        """Test that duplicate registration is rejected"""
        self.engine.process_registration_records(self.test_learner, self.test_course)
        success, message = self.engine.process_registration_records(self.test_learner, self.test_course)
        self.assertFalse(success)
        self.assertIn("Duplicate registration", message)
        self.assertEqual(len(self.engine.failed_registrations), 1)

    def test_registration_course_capacity(self):
        """Test that registration fails when course capacity is reached"""
        small_course = Course("Small", "C003", 3, 5000, "Instructor", 2)

        for i in range(3):
            learner = Learner(
                f"User{i}", "Test", f"L00{i}", f"user{i}@gmail.com", "0821234567"
            )
            self.engine.process_registration_records(learner, small_course)

        self.assertEqual(len(self.engine.registration_records), 2)
        self.assertEqual(len(self.engine.failed_registrations), 1)

    def test_average_calculation(self):
        """Test average calculation strategy"""
        average = Average([80, 90, 85, 75])
        result = average.calculate_assessment_result()
        self.assertEqual(result, 82.5)

    def test_percentage_calculation(self):
        """Test percentage calculation strategy"""
        percentage = Percentage(75, 100)
        result = percentage.calculate_assessment_result()
        self.assertEqual(result, 75)

    def test_classification_distinction(self):
        """Test classification for distinction"""
        classification = Classification(85)
        result = classification.calculate_assessment_result()
        self.assertIsNone(result)

    def test_support_ticket_creation(self):
        """Test support ticket creation"""
        ticket = SupportTicket(
            self.test_learner,
            "Test message",
            "sent",
            "2024-01-01",
            "Open"
        )
        self.assertEqual(ticket.message_description, "Test message")

    def test_support_ticket_invalid_learner(self):
        """Test that invalid learner raises ValueError"""
        with self.assertRaises(ValueError):
            SupportTicket("Not a learner", "Message", "sent", "2024-01-01", "Open")


# Deliverable 5.2: Application Profiling
def run_profiling():
    """Run profiling on the registration processing engine"""
    print("----------5.2 Application Profiling----------")

    profiler = cProfile.Profile()
    profiler.enable()

    engine = RegistrationProcessingEngine()
    test_course = Course("Profiling Course", "P001", 3, 5000, "Prof", 100)

    for i in range(20):
        learner = Learner(
            f"ProfUser{i}",
            "Test"             
             f"profuser{i}@gmail.com",
            "0821234567"
        )
        engine.process_registration_records(learner, test_course)

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats('cumtime')

    print("----------Profiling Results----------")
    stats.print_stats(10)

    stats.sort_stats('callcount')
    print("\n----------Top 10 Functions by Call Count----------")
    stats.print_stats(10)

    with open("profiling_results.txt", "w") as f:
        sys.stdout = f
        stats.sort_stats('cumtime')
        stats.print_stats()
        sys.stdout = sys.__stdout__

    print("Profiling results saved to profiling_results.txt")


if __name__ == "__main__":
    print("--------Learner-------")
    learner.learner_info()

    print("--------Course-------")
    course.course_info()

    print("--------Registration-------")
    registration.registration_info()

    print("--------Assessment-------")
    assessment.assessment_info()

    print("--------Support Ticket-------")
    support_ticket.message_info()

    print("--------Configuration Settings-------")
    configuration_settings = SingletonConfiguration.get_config_instance()
    configuration_settings.config_settings()

    print("--------Support Ticket--Type------")
    choice = input("What type of Support Ticket would you like?")
    ticket = SupportTicketFactory.organisation_support_ticket(choice)
    ticket.support_ticket()
    print(ticket.support)

    print("\n")

    print("--------Assessment Result-------")
    assessment.assessment_info()

    average_result = Result(Average([80, 90, 78]))
    average = average_result.calculate_assessment()
    print("Average:", average)

    percentage_result = Result(Percentage(70, 80))
    percentage = percentage_result.calculate_assessment()
    print(f"Percentage: {percentage}%")

    classification_result = Result(Classification(percentage))
    classification = classification_result.calculate_assessment()
    print(f"Classification: {classification}%\n")

    # Deliverable 2: Registration Processing Engine
    print("---------Registration Processing Engine---------")

    # Creating Registration Processing Engine object
    engine = RegistrationProcessingEngine()

    # Creating a smaller course capacity to test capacity management
    processing_course = Course(
        course_name="Enterprise",
        course_id=10,
        course_duration=3,
        course_fee=70000,
        course_instructor="Martin",
        course_capacity=5
    )

    # Creating 10 simulated registration requests
    registration_requests = []

    for i in range(1, 11):
        simulated_learner = Learner(
            learner_name=f"Learner{i}",
            learner_surname="Student",
            learner_id=i,
            learner_email=f"learner{i}@gmail.com",
            phone_number=f"08200000{i:02d}"
        )

        registration_requests.append(
            (simulated_learner, processing_course)
        )

    # 2.3.Concurrent Request Processing
    # Processing the 10 registration requests
    print("---------Processing 10 Registration Requests:---------")
    for learner_request, course_request in registration_requests:
        success, message = engine.process_registration_records(learner_request, course_request)
        print(message)

    # Testing duplicate registration
    print("\n---------Testing Duplicate Registration---------")
    success, message = engine.process_registration_records(registration_requests[0][0], processing_course)
    print(message)

    # Displaying registration summary
    engine.registration_summary()

    print("---------- Concurrent Registrations Processing:----------")
    threads = []
    for learner_request, course_request in registration_requests:
        thread = Thread(target=engine.process_concurrent_requests, args=(learner_request, course_request))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n---------Concurrent Registrations Processing---------")
    engine.registration_summary()

    # Deliverable 3: Bugzot Monitoring
    print("---------Deliverable 3: Bugzot Monitoring Subsystem-------")

    # 3.2 Performance Report
    print("---------3.2 Performance Report---------")
    report = generate_performance_report(engine)
    print(f"Total Successful: {report['total_success']}")
    print(f"Total Failed: {report['total_failed']}")
    print(f"Success Rate: {report['success_rate']:.1f}%")

    # Display Bugzot log file contents
    print("---------Bugzot Log File Contents---------")
    try:
        with open("bugzot_log.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Bugzot log file not found. Make sure you ran the registration processing.")

    # Deliverable 4: GUI
    window.mainloop()

    # Deliverable 5.1: Run Tests
    print("\n---------Deliverable 5.1: Running Automated Tests---------")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBugzotSystem)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)

    print("\n---------Test Summary---------")
    print(f"Tests Run: {test_result.testsRun}")
    print(f"Failures: {len(test_result.failures)}")
    print(f"Errors: {len(test_result.errors)}")
    print(f"Success: {test_result.wasSuccessful()}")

    # Deliverable 5.2: Run Profiling
    print("\n---------Deliverable 5.2: Running Profiling---------")
    run_profiling()