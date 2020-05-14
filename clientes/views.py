from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404 #o método get_object_or_404 recupera o elemento do banco
from .models import Person #importação do model contendo o banco de dados pretendido
from .forms import FormularioPessoas


@login_required
def persons_list(request):
    persons = Person.objects.all() #variável persons recebera tod o conteudo do model Person.

    return render(request, 'person.html', {'pessoas': persons}) #retornando o template juntamente com a variável persons


@login_required
def persons_new(request):
    # a variável form receberá o formulário referenciado.
    # O parâmetro request.POST informa que este formulário usará uma request através do method POST
    # O parâmetro request.FILLES informa que a request deste form também solicita os arquivos passados pelo form.
    form = FormularioPessoas(request.POST or None, request.FILES or None)


    if form.is_valid():
        form.save()
        return redirect('listar')

    return render(request, 'formulario_de_pessoas.html', {'form': form})


@login_required
def persons_update(request, id):

    # pessoa está recebendo o objeto do banco através do método get_object_or_404
    # O primeiro parâmetro informa o model que sofrerá a busca
    # O argumento pk(primary key) passamos o id do elemento pretendido
    pessoa = get_object_or_404(Person, pk=id)
    # a variável form receberá o formulário referenciado.
    # O parâmetro request.POST informa que este formulário usará uma request através do method POST
    # O parâmetro request.FILLES informa que a request deste form também solicita os arquivos passados pelo form.
    # o parâmetro instance permite que ao abrir o formulário, ele já traga os dados da pessoa setada na view (pelo id).
    form = FormularioPessoas(request.POST or None, request.FILES or None, instance= pessoa)

    # este if verifica se o formulário é válido para então permitir que os dados sejam salvos
    if form.is_valid():
        form.save()
        return redirect('listar')

    return render(request, 'formulario_de_pessoas.html', {'form': form})


@login_required
def persons_delete(request, id):
    # pessoa está recebendo o objeto do banco através do método get_object_or_404
    # O primeiro parâmetro informa o model que sofrerá a busca
    # O argumento pk(primary key) passamos o id do elemento pretendido
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('listar')

    return render(request, 'person_delete.html', {'pessoas': person})

