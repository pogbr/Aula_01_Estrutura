class Aluno:
    def __init__(self, nome, datanascimento, cpf, endereco):
        self.nome = nome
        self.datanascimento = datanascimento
        self.cpf = cpf
        self.endereco = endereco
    
    def getNome(self):
        return self.nome

