class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact


class Education:
    def __init__(self, degree, institution, graduation_year):
        self.degree = degree
        self.institution = institution
        self.graduation_year = graduation_year


class WorkExperience:
    def __init__(self, job_title, company, start_year, end_year):
        self.job_title = job_title
        self.company = company
        self.start_year = start_year
        self.end_year = end_year


class DetailedWorkExperience(WorkExperience):
    def __init__(self, job_title, company, start_year, end_year, responsibilities):
        super().__init__(job_title, company, start_year, end_year)
        self.responsibilities = responsibilities


class CV:
    def __init__(self, person, education, work_experience):
        self.person = person
        self.education = education
        self.work_experience = work_experience

    def generate_cv(self):
        # Method to generate CV in standard format
        cv_output = f"CV\n\nPersonal Information:\nName: {self.person.name}\nAge: {self.person.age}\nContact: {self.person.contact}\n\nEducation:\nDegree: {self.education.degree}\nInstitution: {self.education.institution}\nGraduation Year: {self.education.graduation_year}\n\nWork Experience:\n"

        if isinstance(self.work_experience, DetailedWorkExperience):
            cv_output += f"Job Title: {self.work_experience.job_title}\nCompany: {self.work_experience.company}\nStart Year: {self.work_experience.start_year}\nEnd Year: {self.work_experience.end_year}\nResponsibilities: {self.work_experience.responsibilities}\n"
        else:
            cv_output += f"Job Title: {self.work_experience.job_title}\nCompany: {self.work_experience.company}\nStart Year: {self.work_experience.start_year}\nEnd Year: {self.work_experience.end_year}\n"

        return cv_output


# User Interface
def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    contact = input("Enter your contact information: ")

    degree = input("Enter your highest degree: ")
    institution = input("Enter the institution where you studied: ")
    graduation_year = int(input("Enter your graduation year: "))

    job_title = input("Enter your current job title: ")
    company = input("Enter your current company: ")
    start_year = int(input("Enter the start year of your current job: "))
    end_year = int(input("Enter the end year of your current job: "))

    # Additional details for DetailedWorkExperience
    responsibilities = input("Enter your responsibilities (if any): ")

    person = Person(name, age, contact)
    education = Education(degree, institution, graduation_year)
    work_experience = DetailedWorkExperience(job_title, company, start_year, end_year, responsibilities)

    return person, education, work_experience


def main():
    # Gather user input
    person, education, work_experience = get_user_input()

    # Create CV object
    cv = CV(person, education, work_experience)

    # Generate and display CV
    cv_output = cv.generate_cv()
    print("\nGenerated CV:\n")
    print(cv_output)


if __name__ == "__main__":
    main()
