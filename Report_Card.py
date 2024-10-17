import csv
import sys
from pathlib import Path

#Chris Pirnack 
#05/23/2024
#This program print out the trainer score for steps 7

#You need have Python installed
#You also need a directory where all the school data is saved to

def calculate_percentage(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        total_students = 0
        hour_total = 0
        students_30_up = 0
        trainer_score = 0
        step_5_trainer_score = 0

        

        if 'Seat Time - Hours' not in header:
                str(trainer_score)
                return trainer_score, total_students, step_5_trainer_score

        seat_time_index = header.index('Seat Time - Hours')
        
        for row in reader:
            if 'Archived' in row:
                continue
                
            else:
                total_students += 1 #Increases the count if row doesn't have archive in it

                try:
                    value = float(row[seat_time_index])
                    if value >= 30:
                        students_30_up += 1
                except ValueError:
                    continue
                hour_total += value
            
        percentage = (students_30_up / total_students) * 100
        average_hours = (hour_total / total_students)
        trainer_score = (((average_hours * 100) / 30) + (5 * students_30_up))
        if total_students > 0:
            step_5_trainer_score = 50
    str(trainer_score)
    return trainer_score, total_students, step_5_trainer_score

def teacher_cert(filename):
    #Opens the CSV file
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)

        #Variables

        sign_in_teacher = 0
        total_teachers = 0
        cert_lvl_total = 0
        complete_tutorial_teacher = 0

        average_teach_sign_in = 0
        average_teach_cert_lvl = 0
        average_complete_tutorial_teacher = 0

        #if Time Spent is blank It will let the 
        if 'Time Spent' not in header:
            str(average_teach_sign_in)
            str(average_teach_cert_lvl)
            return average_teach_sign_in, average_teach_cert_lvl, average_complete_tutorial_teacher

        cert_lvl_index = header.index('Certification Level')
        time_spent_index = header.index('Time Spent')

        for row in reader:
            cert_lvl = row[cert_lvl_index]
            time_spent = row[time_spent_index]

            total_teachers += 1

            try:
                if float(time_spent) > 0:
                    sign_in_teacher += 1
            except ValueError:
                continue

            if cert_lvl != 'None':
                cert_lvl_total += 1
                complete_tutorial_teacher += 1

        average_teach_sign_in = (sign_in_teacher/total_teachers) * 100
        if sign_in_teacher == total_teachers:
            average_teach_sign_in += 10
        average_teach_cert_lvl = (cert_lvl_total/total_teachers) * 100
        average_complete_tutorial_teacher = (complete_tutorial_teacher/total_teachers) * 100
        if complete_tutorial_teacher == total_teachers:
            average_complete_tutorial_teacher += 10
    str(average_teach_sign_in)
    str(average_teach_cert_lvl)
    str(average_complete_tutorial_teacher)
    return average_teach_sign_in, average_teach_cert_lvl, average_complete_tutorial_teacher


def calculate_steps(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        total_step = 0
        students_1step = 0
        step_trainer_score = 0
        if 'Seat Time - Hours' not in header:
                str(step_trainer_score)
                return step_trainer_score
        
        step_index = header.index('Steps Completed')

        for row in reader:
            if 'Archived' in row:
                continue

            else:
                total_step += 1

                try:
                    step = float(row[step_index])
                    if step >= 30:
                        students_1step += 1
                except ValueError:
                    continue

        step_percentage = (students_1step / total_step) * 100
        if total_step == students_1step:
            step_trainer_score = step_percentage + 20
        else:
            step_trainer_score = step_percentage
    str(step_trainer_score)
    return step_trainer_score





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Get the files  <Name of School>")
        sys.exit(1)
    
    # Initialize the data dictionary
    data = {
        'Enrolled Students': None,
        'Step 1': 'NOUPDATE',  # Administrator Set-up and Orientation
        'Step 2': None,        # Teacher Set-Up (calculated below)
        'Step 3': None,        # Teacher Start-up Tutorials (calculated below)
        'Step 4': 'NOUPDATE',  # Teacher Quick-Start Webinar
        'Step 5': None,        # Student Enrollment (calculated below)
        'Step 6': None,        # Go Live 🚀 (calculated below)
        'Step 7': None,        # Student Hours Logged (calculated below)
        'Step 8': None,        # Professional Development
        'Step 9': 'NOUPDATE',  # Advanced Teacher Tutorials
        'Step 10': 'NOUPDATE'  # Embedded Training Webinar
    }

    school_name = sys.argv[1]
    filepath = Path(school_name + "/")

    filename_seat_time_all = "StudentSeatTime_ALL.csv"
    filename_seat_time_month = "StudentSeatTime_MONTH.csv"
    filename_teacher_cert = "TeacherCertification_ALL.csv"

    full_path_seat_time_all = f"{filepath}/{filename_seat_time_all}"
    full_path_seat_time_month = f"{filepath}/{filename_seat_time_month}"
    full_path_teacher_cert = f"{filepath}/{filename_teacher_cert}"

    trainer_score_all, total_students_all, step_5_trainer_score_all = calculate_percentage(full_path_seat_time_all)
    average_teach_sign_in, average_teach_cert_lvl, average_complete_tutorial_teacher = teacher_cert(full_path_teacher_cert)
    step_trainer_score = calculate_steps(full_path_seat_time_all)
    trainer_score_month, total_students_month, step_5_trainer_score_month = calculate_percentage(full_path_seat_time_month)

    data['Enrolled Students'] = f"{total_students_all:.2f}"
    data['Step 2'] = f"{average_teach_sign_in:.2f}"
    data['Step 3'] = f"{average_complete_tutorial_teacher:.2f}"
    data['Step 5'] = f"{step_5_trainer_score_all}"
    data['Step 6'] = f"{step_trainer_score:.2f}"
    data['Step 7'] = f"{trainer_score_month:.2f}"
    data['Step 8'] = f"{average_teacher_cert_lvl:.2f}"

   '''print("----------------Enrolled Students---------------")
    print("The number of students:", total_students_all)
    print("---------------------Step 2---------------------")
    print(f"Percent of teachers who signed in (Trainer Score): {average_teach_sign_in:.2f}")
    print("---------------------Step 3---------------------")
    print(f"Percent of teachers who have completed all the tutorials (Trainer Score): {average_complete_tutorial_teacher:.2f}")
    print("---------------------Step 5---------------------")
    print("If a student has been created (Trainer Score):", step_5_trainer_score_all)
    print("---------------------Step 6---------------------")
    print(f"Percent of students who have completed at least one step (Trainer Score): {step_trainer_score:.2f}")
    print("---------------------Step 7---------------------")
    print(f"Average number of hours that the students have worked in the past month (Trainer Score): {trainer_score_month:.2f}")
    print("---------------------Step 8---------------------")
    print(f"Percent of teachers that completed at least one CEU (Trainers Score): {average_teach_cert_lvl:.2f}")
    '''
    output = ' '.join([str(v) for v in data.values()])
    print(output)