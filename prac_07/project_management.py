from datetime import datetime

from project import Project


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('\t')
                # Check if line is a header or if it doesn't have the correct number of parts
                if parts[0] == 'Name' or len(parts) != 5:
                    continue  # Skip header or invalid lines
                name, start_date, priority, cost_estimate, completion_percentage = parts
                # Now we have the parts, try to parse the start date and create the Project
                try:
                    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                    projects.append(project)
                except ValueError as e:
                    print(f"Error parsing line: {line}. Error: {e}")
                    # Handle or log the error as appropriate
        return projects
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        for project in projects:
            file.write(
                f"{project.name}\t"
                f"{project.start_date.strftime('%d/%m/%Y')}\t"
                f"{project.priority}\t"
                f"{project.cost_estimate}\t"
                f"{project.completion_percentage}\n")


def display_projects(projects):
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects, after_date):
    filtered_projects = [p for p in projects if p.start_date > after_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"  {project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    selected_project = projects[project_choice]
    print(f"{selected_project}")

    new_percentage = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    if new_percentage:
        projects[project_choice].completion_percentage = int(new_percentage)
    if new_priority:
        projects[project_choice].priority = int(new_priority)


def main():
    projects = []

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = "projects.txt"
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_input = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, datetime.strptime(date_input, "%d/%m/%Y").date())
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
