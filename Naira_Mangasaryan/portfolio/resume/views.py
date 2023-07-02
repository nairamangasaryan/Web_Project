from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def portfolio(request):
    content = {"name": "Naira",
                        "surename": "Mangasaryan",
                        "expariance": [
                            {"job_title": "Scientist,manager of department",
                                "company": "Russian-Armenian University",
                                "period": "2007-present"},
                            {"job_title": "Research assistant",
                                "company": "Institute of Applied Problems of Physics of NAS RA",
                                "period": "2005-2007"}],
                        "education": [
                            {"university": "Yerevan State University, Faculty of Radiophysics",
                                "period": "2003-2003",
                                "degree": "Master’s degree"},
                            {"university": "Yerevan State University, Faculty of Radiophysics",
                                "period": "1999-2003",
                                "degree": "Bachelor’s degree"}],
                        "languages": ["Armenian (native)", "Russian (good)", "English (intermediate)"],
                        "contacts": ["email: mangasaryannaira@gmail.com", "phone: +374 93 49 55 44"],
                        "skills": ["Git/Github", "Linux OS", "MS Visual Studio", "Slack", 
                                    "Excellent problem-solving ability, punctuality, detail-oriented,responsibility",
                                    "Team player: interact well with coworkers and management" ]

                        }
    return render(request, "portfolio.html", context=content)


