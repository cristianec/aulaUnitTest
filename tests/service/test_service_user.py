from unittest import TestCase

from main import service
from src.models import user
from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_nameString(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario adicionado")
        resultado = service.add_user("matheus","dev")

        assert resultado == resultado_esperado


    def test_add_user_jobString(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario adicionado")
        resultado = service.add_user("matheus", "dev")

        assert resultado == resultado_esperado


    def test_add_user_nameExis(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario ou Job já cadastrado")
        otherUser  = service.add_user("matheus", "dev")
        resultado = service.add_user("matheus", "dev2")

        assert resultado == resultado_esperado


    def test_add_user_jobExist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario ou Job já cadastrado")
        otherUser = service.add_user("matheus", "dev")
        resultado = service.add_user("joao", "dev")

        assert resultado == resultado_esperado


    def test_add_user_different_nameString(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.add_user(1, "dev")

        assert resultado == resultado_esperado


    def test_add_user_different_jobString(self):
        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.add_user("matheus", 1)

        assert resultado == resultado_esperado


    def test_add_user_nameNone(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.add_user(None, "dev")

        assert resultado == resultado_esperado


    def test_add_user_jobNone(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.add_user("matheus", None)

        assert resultado == resultado_esperado



    def test_remove_user_nameExist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario removido")
        adicionar =  resultado = service.add_user("matheus", "QA")
        resultado = service.remove_user("matheus", "QA")

        assert resultado == resultado_esperado


    def test_remove_user_nameNoExist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario não encontrado")
        resultado = service.remove_user("matheus", "QA")

        assert resultado == resultado_esperado


    def test_remove_user_name_different_from_string(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.remove_user(1, "QA")

        assert resultado == resultado_esperado


    def test_remove_user_name_none(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        resultado = service.remove_user("matheus", 1)

        assert resultado == resultado_esperado


    def test_update_user_name_string_different_from_string(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        newUser = service.add_user("matheus","QA")
        resultado = service.update_user(1, "QASenior")

        assert resultado == resultado_esperado

    def test_update_user_name_none(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        newUser = service.add_user("matheus", "QA")
        resultado = service.update_user(None, "QASenior")

        assert resultado == resultado_esperado

    def test_update_user_new_job_different_from_string(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        newUser = service.add_user("matheus", "QA")
        resultado = service.update_user("matheus", 1)

        assert resultado == resultado_esperado

    def test_update_user_new_job_none(self):

        service = ServiceUser()

        resultado_esperado = ("Nome ou Job deve ser uma String e diferente de vazio")
        newUser = service.add_user("matheus", 1)
        resultado = service.update_user("matheus", None)

        assert resultado == resultado_esperado


    def test_update_user_name_exist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario atualizado")
        newUser = service.add_user("matheus", "QA")
        resultado = service.update_user("matheus", "QASenior")

        assert resultado == resultado_esperado

    def test_update_user_name_noExist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario não encontrado")
        resultado = service.update_user("matheusNaoExistente", "QASenior")

        assert resultado == resultado_esperado


    def test_get_user_by_name_different_from_string(self):

        service = ServiceUser()

        resultado_esperado = "Nome deve ser uma String e diferente de vazio"
        resultado = service.get_user_by_name(1)

        assert resultado == resultado_esperado

    def test_get_user_by_name_none(self):

        service = ServiceUser()

        resultado_esperado = ("Nome deve ser uma String e diferente de vazio")
        resultado = service.get_user_by_name(None)

        assert resultado == resultado_esperado

    def test_get_user_by_name_Exist(self):

        service = ServiceUser()

        resultado_esperado = ("Job:QA")
        newUser = service.add_user("matheus","QA")
        resultado = service.get_user_by_name("matheus")

        assert resultado == resultado_esperado

    def test_get_user_by_name_noExist(self):

        service = ServiceUser()

        resultado_esperado = ("Usuario não encontrado")
        resultado = service.get_user_by_name("matheusNaoExiste")

        assert resultado == resultado_esperado