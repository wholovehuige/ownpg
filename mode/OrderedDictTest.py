from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language["Bob"] = "java"
favorite_language["Alise"] = "js"
favorite_language["Roy"] = "python"
favorite_language["Rose"] = "C++"

for name,language in favorite_language.items():
    print(name +"'s favorite language is :" + language)