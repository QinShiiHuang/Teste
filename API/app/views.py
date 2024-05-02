from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cadastro
from .serializer import CadastroSerializer

@api_view(['GET', 'POST'])
def cadastrados(request):
    if request.method == 'GET':
        pessoa = Cadastro.objects.all()
        serializer = CadastroSerializer(pessoa, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def consulta_att_delete(request, id):
    try:
        cadastro = Cadastro.objects.get(id=id)
    except Cadastro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CadastroSerializer(cadastro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CadastroSerializer(cadastro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)