>>> Veterinario.objects.all()
<QuerySet [<Veterinario: xavier maya>]>

>>> Veterinario.objects.count()
1

>>> Veterinario.objects.get(pk=1)
<Veterinario: xavier maya>

>>> Project.objects.filter(name="xavier maya")
<QuerySet [<Project: xavier maya>]>

>>> Veterinario.objects.filter(name__contains="xavier")
<QuerySet [<Project: xavier maya>]>

>>> Veterinario.objects.filter(description__icontains="proyecto")
<QuerySet [<Project: xavier maya>]>
