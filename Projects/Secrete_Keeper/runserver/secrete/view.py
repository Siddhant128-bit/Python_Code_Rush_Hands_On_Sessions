from django.shortcuts import render

def secrete(request):
    result=""
    if request.method=='POST':
        a=str(request.POST.get('a'))
        b=int(request.POST.get('b'))
        
        for char in a:
            if char.isupper():
                result += chr((ord(char) + b - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + b - 97) % 26 + 97)
            else:
                result += char  
        return render(request,'results.html',{'result':result})
    else:
        return render(request,'input.html')
    

        
    