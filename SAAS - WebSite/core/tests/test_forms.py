from django.test import TestCase

from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity'
        self.email = 'felicity@gmail.com'
        self.assunto = 'Assunto qualquer'
        self.mensagem = "Opaaa"

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        rest1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(rest1, res2)