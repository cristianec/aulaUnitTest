from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()


    def add_user(self,name,job):

        if type(name) != str or type(job) != str or name == None or job == None:
            return "Nome ou Job deve ser uma String e diferente de vazio"

        for user in self.store.bd:
            if user.name == name or user.job == job:
                return "Usuario ou Job já cadastrado"

        user = User(name, job)
        self.store.bd.append(user)
        return "Usuario adicionado"


    def remove_user(self, name, job):

        if type(name) != str or type(job) != str or name is None or job is None:
            return "Nome ou Job deve ser uma String e diferente de vazio"

        for user in self.store.bd:
            if user.name == name and user.job == job:
                self.store.bd.remove(user)
                return "Usuario removido"

        return "Usuario não encontrado"


    def update_user(self, name, new_job):
        if type(name) != str or type(new_job) != str or name is None or new_job is None:
            return "Nome ou Job deve ser uma String e diferente de vazio"

        for user in self.store.bd:
            if user.name == name:
                user.job = new_job
                return "Usuario atualizado"

        return "Usuario não encontrado"


    def get_user_by_name(self, name):

        if type(name) != str or name is None:
            return "Nome deve ser uma String e diferente de vazio"

        for user in self.store.bd:
            if user.name == name:
                return "Job:"+user.job

        return "Usuario não encontrado"