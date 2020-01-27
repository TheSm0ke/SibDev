from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from SibDev.settings import MEDIA_ROOT
import codecs
from .models import SavedForm

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(request.FILES['document'])
        type = uploaded_file.name.split('.')
        if type[-1] == 'csv':
            fs = FileSystemStorage()
            #fs.save(uploaded_file.name, uploaded_file)
            server_file = codecs.open(MEDIA_ROOT+'/'+uploaded_file.name,'r','utf-8')
            #mass = [line.strip() for line in server_file]
            buff = 0;
            response = ''
            for text in server_file:
                #mass[buff] = text.split(',')
                mass = text.split(',')
                if mass[0] != 'customers' and mass[1] != 'item' and mass[2] != 'total' and mass[3] != 'quantity' and mass[4] != 'date':
                    buff = buff + 1;
                    SavedForm.objects.create(username=mass[0],spent_money=mass[2],gems=mass[1])
                    response = str(buff)+'Добавлено строк, последняя строка: '+'customers = '+str(mass[0])+' spent_money = '+str(mass[2])+' gem = '+ str(mass[1])+'\n'
                    #print(response)

            server_file.close()
            return render(request, 'forms.html',context={'response': response})
        else:
            return render(request, 'forms.html',context={'errors': 'Type\'s file incorrect'})
    else:
        return render(request, 'forms.html',context={'errors': 'Don\'t have a file'})

def objects_detail_url(request):
    users = SavedForm.objects.all()
    return render(request, 'allusers.html', context={'users': users})
