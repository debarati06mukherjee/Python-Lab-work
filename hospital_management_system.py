### HOSPITAL MANAGEMENT SYSTEM
# 1. PATIENT REGISTRATION - DICTIONARY
patients = {}
def register_patient():
    print("PATIENT REGISTRATION")
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")

    patients[patient_id] = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Phone": phone
    }
    print("Patient registered successfully!")

# 2. APPOINTMENT SCHEDULING - LIST
appointments = []
def schedule_appointment():
    print("\nAPPOINTMENT SCHEDULING")
    patient_id = input("Enter Patient ID: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date: ")
    time = input("Enter Appointment Time: ")
    appointment = [patient_id, doctor, date, time]
    appointments.append(appointment)
    print("Appointment scheduled successfully!")
def display_appointments():
    print("\n--- Appointments ---")
    if len(appointments) == 0:
        print("No appointments found.")
    else:
        for i, appointment in enumerate(appointments, start=1):
            print("\nAppointment", i)
            print("Patient ID:", appointment[0])
            print("Doctor:", appointment[1])
            print("Date:", appointment[2])
            print("Time:", appointment[3])

# 3. MEDICAL RECORDS - FILE HANDLING
def save_medical_record():
    print("MEDICAL RECORD")
    patient_id = input("Enter Patient ID: ")
    disease = input("Enter Disease/Diagnosis: ")
    medicine = input("Enter Medicine: ")
    notes = input("Enter Doctor's Notes: ")
    with open("medical_records.txt", "a") as file:
        file.write("Patient ID: " + patient_id + "\n")
        file.write("Disease: " + disease + "\n")
        file.write("Medicine: " + medicine + "\n")
        file.write("Notes: " + notes + "\n")
        file.write("-------------------------\n")
    print("Medical record saved successfully!")

def view_medical_records():
    print("MEDICAL RECORD")
    try:
        with open("medical_records.txt", "r") as file:
            records = file.read()
            if records:
                print(records)
            else:
                print("No medical records found.")
    except FileNotFoundError:
        print("No medical records found.")
# 4. DOCTOR INFORMATION - TUPLE
doctors = (
    ("D001", "Dr. Sharma", "Cardiologist"),
    ("D002", "Dr. Verma", "Neurologist"),
    ("D003", "Dr. Singh", "Orthopedic"),
    ("D004", "Dr. Gupta", "General Physician")
)

def display_doctors():
    print("DOCTOR INFORMATION")
    for doctor in doctors:
        print("Doctor ID:", doctor[0])
        print("Name:", doctor[1])
        print("Specialization:", doctor[2])
        
# 5. BILLING SYSTEM - CLASS AND OBJECT
class Billing:
    def __init__(self, patient_name, consultation, medicine, room):
        self.patient_name = patient_name
        self.consultation = consultation
        self.medicine = medicine
        self.room = room

    def calculate_bill(self):
        return self.consultation + self.medicine + self.room

    def display_bill(self):
        total = self.calculate_bill()

        print("HOSPITAL BILL")
        print("Patient Name:", self.patient_name)
        print("Consultation Fee: ₹", self.consultation)
        print("Medicine Charges: ₹", self.medicine)
        print("Room Charges: ₹", self.room)
        print("Total Bill: ₹", total)


def generate_bill():
    print("BILLING SYSTEM")
    name = input("Enter Patient Name: ")
    consultation = float(input("Enter Consultation Fee: ₹"))
    medicine = float(input("Enter Medicine Charges: ₹"))
    room = float(input("Enter Room Charges: ₹"))

    bill = Billing(name, consultation, medicine, room)

    bill.display_bill()

# 6. REPORT GENERATION - PYTHON LIBRARIES
import datetime
def generate_report():

    print("HOSPITAL REPORT")
    current_date = datetime.datetime.now()

    print("Report Date:", current_date.strftime("%d-%m-%Y"))
    print("Report Time:", current_date.strftime("%H:%M:%S"))

    print("\nTotal Registered Patients:", len(patients))
    print("Total Appointments:", len(appointments))

    try:
        with open("medical_records.txt", "r") as file:
            records = file.read()

        if records:
            medical_records = records.count("Patient ID:")
        else:
            medical_records = 0

    except FileNotFoundError:
        medical_records = 0

    print("Total Medical Records:", medical_records)
    print("Total Doctors:", len(doctors))

    print("\nReport generated successfully!")
    
# MAIN MENU
while True:

    print("\n \n HOSPITAL MANAGEMENT SYSTEM")
    print("1. Patient Registration")
    print("2. Schedule Appointment")
    print("3. View Appointments")
    print("4. Add Medical Record")
    print("5. View Medical Records")
    print("6. Doctor Information")
    print("7. Generate Bill")
    print("8. Generate Hospital Report")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        display_appointments()

    elif choice == "4":
        save_medical_record()

    elif choice == "5":
        view_medical_records()

    elif choice == "6":
        display_doctors()

    elif choice == "7":
        generate_bill()

    elif choice == "8":
        generate_report()

    elif choice == "9":
        print("Thank you for using Hospital Management System.")
        break

    else:
        print("Invalid choice! Please try again.")