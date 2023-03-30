from django.shortcuts import render

# Create your views here.
# request 오면 response할 것
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['text']
    text_list = text.split()
    text_dict = {}
    for word in text_list:
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    for word in list(text_dict):
        if text_dict[word] < 5 :
            del text_dict[word]
            
    words = sorted(text_dict.items(), key = lambda x : x[1], reverse = True)
    return render(request, 'result.html', {'words': words})
