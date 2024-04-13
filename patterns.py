name = [
    r'name is(.*?)\n',
    r'name(.*?)\n',
    r'surname(.*?)\n',
    r'identity(.*?)\n',
    r'personal information(.*?)\n',
    r'personal info(.*?)\n',
    r'applicant information(.*?)\n',
    r'applicant info(.*?)\n'
]

Date_of_birth = [
    r'\d{2}[./]\d{2}[./]\d{2,4}',
    r'(0[1-9]|[12][0-9]|3[01])-./[-./]\d{2,4}',
    r'\d{4}[-/]\d{2}[-/]\d{2,4}',
    r'\b(\d{1,2})(?:st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November'
    r'|December)\b',
    r'date of birth(.*?)\n',
    r'dob(.*?)\n',
    r'born at(.*?)\n',
    r'birthdate(.*?)\n',
    r'birthday(.*?)\n',
    r'date born(.*?)\n',
    r'birth(.*?)\n',
    r'birth information(.*?)\n',
    r'birth info(.*?)\n',
    r'personal details(.*?)\n'
]

phone = [
    r'\d{11}',
    r'\+\d{11}',
    r'\+\d{1,2}\(\d{3}\)\d{7}',
    r'\+\d{1,2}\(\d{3}\)-\d{3}-\d{4}',
    r'\(\d{3}\) \d{3}-\d{4}',
    r'\d{3}[\s-]\d{3}[\s-]\d{4}',
    r'\+\d{1,2}\d{10}',
    r'\(?\d{3}\)?-?\d{3}-?\d{4}',
    r'(\+\d{1,2}\s?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}',
    r'phone number(.*?)\n',
    r'phone(.*?)\n',
    r'telephone(.*?)\n',
    r'contact information(.*?)\n',
    r'contact info(.*?)\n',
    r'contact(.*?)\n',
    r'mobile(.*?)\n',
    r'cell(.*?)\n',
    r'cellular(.*?)\n',
    r'reach me at(.*?)\n',
    r'call me at(.*?)\n'
]

email = [
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    r'email id(.*?)\n',
    r'e-mail(.*?)\n',
    r'email address(.*?)\n',
    r'email(.*?)\n',
    r'mail(.*?)\n'
]

address = [
    r'\b\d{1,4}\s\w+\sstreet\s\w+\b',
    r'\b\d{1,4}\s\w+\sstreet\b',
    r'\bstreet\s\w+\s\d{1,4}\b',
    r'\b\w+\s\d{1,4}\sstreet\b',
    r'\b\d{1,4}\s\w+\sstreet\b',
    r'address(.*?)\n',
    r'residence(.*?)\n',
    r'location(.*?)\n',
    r'home(.*?)\n',
    r'broadway(.*?)\n',
    r'street(.*?)\n',
    r'city(.*?)\n',
    r'town(.*?)\n',
    r'country(.*?)\n',
    r'village(.*?)\n',
    r'nation(.*?)\n'
]

university = [
    r'(.*?) university\n',
    r'university of(.*?)\n',
    r'(.*?) institution',
    r'university(.*?)\n',
    r'college(.*?)\n',
    r'institution(.*?)\n',
    r'alma mater(.*?)\n',
    r'school(.*?)\n',
    r'higher education(.*?)\n',
    r'education(.*?)\n'
]

faculty = [
    r'faculty of(.*?)\n',
    r'faculty(.*?)\n',
    r'bachelor(.*?)\n',
    r'doctorate(.*?)\n',
    r'academic unit(.*?)\n',
    r'degree in(.*?)\n',
    r'degree(.*?)\n',
    r'department of(.*?)\n',
    r'department(.*?)\n',
    r'division(.*?)\n',
    r'master(.*?)\n'
]

experience = [
    r'experience (.*?)\n',
    r'experience(.*?)\n',
    r'employment history(.*?)\n',
    r'career history(.*?)\n',
    r'job history(.*?)\n',
    r'career(.*?)\n',
    r'employment(.*?)\n',
    r'previous roles(.*?)\n',
    r'professional background(.*?)\n',
    r'career(.*?)\n',
    r'position held(.*?)\n',
]

languages = [
    r'programming languages(.*?)\n',
    r'programming language(.*?)\n',
    r'technical skills(.*?)\n',
    r'coding language(.*?)\n',
    r'coding languages(.*?)\n',
    r'software languages(.*?)\n',
    r'software language(.*?)\n',
    r'programming skills(.*?)\n',
    r'programming(.*?)\n',
    r'software development skills(.*?)\n',
    r'coding(.*?)\n',
    r'programing(.*?)\n',
    r'languages(.*?)\n',
    r'language(.*?)\n',
]

skills = [
    r'key skills(.*?)\n',
    r'(.*?) skills',
    r'skills(.*?)\n',
    r'skill highlights(.*?)\n',
    r'core competencies(.*?)\n',
    r'expertise(.*?)\n',
    r'strengths(.*?)\n',
    r'proficiencies(.*?)\n',
    r'proficiency(.*?)\n',
    r'strength(.*?)\n',
    r'capabilities(.*?)\n',
    r'capability(.*?)\n',
    r'competencies(.*?)\n',
    r'competency(.*?)\n',
    r'qualifications(.*?)\n',
    r'qualification(.*?)\n',
    r'abilities(.*?)\n',
]

salary = [
    r'salary expectations(.*?)\n',
    r'salary(.*?)\n',
    r'compensation requirements(.*?)\n',
    r'compensation requirement(.*?)\n',
    r'compensation expectation(.*?)\n',
    r'compensation expectations(.*?)\n',
    r'expected pay(.*?)\n',
    r'wage expectation(.*?)\n',
    r'wage(.*?)\n',
    r'compensation(.*?)\n'
]
