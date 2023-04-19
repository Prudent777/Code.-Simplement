Examinons la même fonction.

def function(a, b, *args, keyword=True, **kwargs):
    print(a, b)
    print(args)
    print(keyword)
    print(kwargs)

Notez que cet appel échouera.

function(a=1, b=2, 5, 3, 4, param=42)

Mais celui-ci ne le sera pas.

function(1, 2, 5, 3, 4, param=42)

