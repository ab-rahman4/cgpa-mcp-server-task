from course_data import COURSES
from grade_marking import GRADE_MARKING

# 1. Convert marks into grade points

def marks_to_grade_points(marks: int) -> float | str:
    """
    Use this tool when you need to convert a student's marks
    into the corresponding grade points.
    """

    if not isinstance(marks, int):
        return "Error: marks must be an integer"

    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"

    for minimum_marks, grade_points in GRADE_MARKING:
        if marks >= minimum_marks:
            return grade_points

    return "Error: unable to determine grade points"


# 2. Calculate semester GPA

def calculate_semester_gpa( grade_points: list[float], credit_hours: list[float]) -> float | str:
    """
    Use this tool when you need to calculate a student's
    semester GPA from grade points and credit hours.
    """

    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours must have the same number of values"

    if len(grade_points) == 0:
        return "Error: at least one course is required"

    if any(gp < 0 or gp > 4.0 for gp in grade_points):
        return "Error: grade points must be between 0.0 and 4.0"

    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than 0"

    total_quality_points = sum(
        gp * ch for gp, ch in zip(grade_points, credit_hours)
    )

    total_credit_hours = sum(credit_hours)

    return total_quality_points / total_credit_hours


# 3. Calculate new CGPA

def calculate_new_cgpa(current_cgpa: float,completed_credit_hours: float,semester_gpa: float,semester_credit_hours: float) -> float | str:
    """
    Use this tool when you need to calculate a student's
    new CGPA after adding one completed semester.
    """

    if not 0.0 <= current_cgpa <= 4.0:
        return "Error: current CGPA must be between 0.0 and 4.0"

    if not 0.0 <= semester_gpa <= 4.0:
        return "Error: semester GPA must be between 0.0 and 4.0"

    if completed_credit_hours <= 0:
        return "Error: completed credit hours must be greater than 0"

    if semester_credit_hours <= 0:
        return "Error: semester credit hours must be greater than 0"

    return (
        (current_cgpa * completed_credit_hours)
        + (semester_gpa * semester_credit_hours)
    ) / (completed_credit_hours + semester_credit_hours)


# 4. Calculate required GPA for target CGPA

def required_gpa_for_target(
    target_cgpa: float,
    current_cgpa: float,
    completed_credit_hours: float,
    remaining_credit_hours: float
) -> float | str:
    """
    Use this tool when you need to determine the GPA required
    over remaining credit hours to reach a target CGPA.
    """

    if not 0.0 <= target_cgpa <= 4.0:
        return "Error: target CGPA must be between 0.0 and 4.0"

    if not 0.0 <= current_cgpa <= 4.0:
        return "Error: current CGPA must be between 0.0 and 4.0"

    if completed_credit_hours <= 0:
        return "Error: completed credit hours must be greater than 0"

    if remaining_credit_hours <= 0:
        return "Error: remaining credit hours must be greater than 0"

    required_gpa = (
        target_cgpa * (completed_credit_hours + remaining_credit_hours)
        - current_cgpa * completed_credit_hours
    ) / remaining_credit_hours

    return required_gpa


# 5. Get courses for a semester

def get_semester_courses(semester: int) -> str:
    """
    Use this tool when you need to find the courses and
    credit hours belonging to a specific semester.
    """

    if not isinstance(semester, int):
        return "Error: semester must be an integer"

    if semester < 1 or semester > 8:
        return "Error: semester must be between 1 and 8"

    courses = COURSES[semester]

    result = f"Semester {semester} courses:\n"

    for course_code, course_name, credit_hours in courses:
        result += (
            f"{course_code} - {course_name}: "
            f"{credit_hours} credit hours\n"
        )

    return result


# 6. Get remaining credit hours

def get_remaining_credit_hours(current_semester: int) -> float | str:
    """
    Use this tool when you need to determine how many graded
    credit hours remain after the student's current semester.
    """

    if not isinstance(current_semester, int):
        return "Error: current semester must be an integer"

    if current_semester < 1 or current_semester > 8:
        return "Error: current semester must be between 1 and 8"

    remaining_credit_hours = 0.0

    for semester in range(current_semester + 1, 9):
        for _, _, credit_hours in COURSES[semester]:
            remaining_credit_hours += credit_hours

    return remaining_credit_hours


# 7. Save report

def save_report(filename: str, content: str) -> str:
    """
    Use this tool when the user explicitly asks to save a useful
    GPA, CGPA, or target-planning result as a report.
    """

    if not isinstance(filename, str) or not filename.strip():
        return "Error: filename must be a non-empty string"

    if not isinstance(content, str) or not content.strip():
        return "Error: content must be a non-empty string"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Report saved successfully as {filename}"

    except OSError as error:
        return f"Error: could not save report: {error}"