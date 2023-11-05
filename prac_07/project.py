import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initialize a new Project instance.

        :param name: str - The name of the project.
        :param start_date: str - The start date of the project in 'dd/mm/yyyy' format.
        :param priority: int - The priority of the project, lower numbers indicate higher priority.
        :param cost_estimate: float - The cost estimate for the project.
        :param completion_percentage: int - The current completion percentage of the project.
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """
        Return a string representation of the project.

        :return: str - The string representation of the project.
        """
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        """
        Check if the project is complete.

        :return: bool - True if the project is 100% complete, False otherwise.
        """
        return self.completion_percentage == 100

    # Add any comparison methods if needed (for example __lt__ for sorting by priority)
    def __lt__(self, other):
        """
        Less than operator for comparing projects based on their priority.
        """
        return self.priority < other.priority
