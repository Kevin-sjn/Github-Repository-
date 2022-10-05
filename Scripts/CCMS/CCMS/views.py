from django.http import HttpResponse

def main(request):
    return HttpResponse("Mission, Vision and Ojectives")

def mission(request):
    return HttpResponse("MISSION: The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.")

def vision(request):
    return HttpResponse("VISION: The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.")

def objectives(request):
    return HttpResponse("VISION: The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.")