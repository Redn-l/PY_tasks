class ProjectDTO:
    def __init__(self, id, name, description, start_date, end_date):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

class TaskDTO:
    def __init__(self, id, project_id, title, description, status, due_date):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
