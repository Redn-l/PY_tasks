class ProjectDTO:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class TaskDTO:
    def __init__(self, id, title, description, status, project_id):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.project_id = project_id
