from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models ,db_methods
import json
# Create your views here.

def to_db_edit(request):
    return render(request, "oradb/db_edit_page.html",{'messages':""})

def to_db_home(request,id):
    tables = models.topTable.objects.filter(db_id = id)
    return render(request, "oradb/db_home.html", {'tables': tables})

def getJSONData(request):
    messages = models.dbMessage.objects.all()
    dictStr = []
    for mess in messages:
        obj = {"id":mess.id,
               "ip_address":mess.ip_address,
               "port":mess.port,
               "db_name":mess.db_name,
               "username":mess.username,
               "password":mess.password}
        dictStr.append(obj)
    jsonArray = json.dumps(dictStr)
    return HttpResponse(jsonArray)
def getAllDbData(request):
    messages = models.dbMessage.objects.all()
    return render(request, "oradb/home.html", {'messages': messages})

def db_page(request,id):
    if str(id) == '0':
        return render(request,'oradb/db_edit_page.html')
    message = models.dbMessage.objects.get(pk = id)
    return render(request,'oradb/db_edit_page.html',{'message':message})

def edit_dbPage(request):
    id = request.POST.get("id")
    if str(id) == '0':
        ip_address = request.POST.get("ip_address")
        port = request.POST.get("port")
        db_name = request.POST.get("db_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        models.dbMessage.objects.create(ip_address = ip_address,port=port,db_name=db_name,username=username,password=password)
    else:
        message = models.dbMessage.objects.get(pk = id)
        message.ip_address = request.POST.get("ip_address")
        message.port = request.POST.get("port")
        message.db_name = request.POST.get("db_name")
        message.username = request.POST.get("username")
        message.password = request.POST.get("password")
        message.save()
    messages = models.dbMessage.objects.all()
    return render(request, "oradb/home.html", {"messages": messages})

def test_oracle1_conn(request,id):
    if str(id) != '0':
        message = models.dbMessage.objects.get(pk = id)
        host = message.ip_address
        port = message.port
        db_name = message.db_name
        username = message.username
        password = message.password
        conn = db_methods.oracle_connection(host,port,db_name,username,password)
        print(conn)
        if conn :
            cursor = conn.cursor()
            sql = 'select table_name from user_tables WHERE ROWNUM<17'
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print(row[0])
                de_sql = 'select * from "'+row[0]+'"'
                print(de_sql)
                cursor.execute(de_sql)
                allcolum = cursor.fetchall()
                for line in allcolum:
                    print(line)
            cursor.close()
            conn.close()
    messages = models.dbMessage.objects.all()
    return render(request, "oradb/home.html", {"messages": messages})

def get_tables(request,db_id):
    pass

def create_table(request):
    name = request.POST.get("name")
    table_name = request.POST.get("table_name")
    search_value = request.POST.get("search_value")
    search_type = request.POST.get("search_type")
    search_type_name = request.POST.get("search_type_name")
    relation = request.POST.get("relation")
    isUse = request.POST.get("isUse")
    models.topTable.objects.create(name = name,
                                   table_name = table_name,
                                   search_value = search_value,
                                   search_type = search_type,
                                   search_type_name = search_type_name,
                                   relation = relation,
                                   isUse = isUse)

