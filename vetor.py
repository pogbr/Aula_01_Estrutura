from aluno import Aluno
class Vetor:
    alunos = []
    alunos.append(Aluno("Johnata","03/09/1991",123,"Rua Alba"))
    alunos.append(Aluno("Marina","10/02/1990",345,"Rua Peixoto de Castro"))
    for i in alunos:
        print("O nome do aluno é: {}\n a data de nascimento: {}\n o cpf dele é: {}\n e o endereço dele é: {}".format(i.nome,i.datanascimento, i.cpf, i.endereco))