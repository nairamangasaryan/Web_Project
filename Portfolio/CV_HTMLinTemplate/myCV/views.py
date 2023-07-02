from django.shortcuts import render
from django.http import HttpResponse


def resume(request):
    return render(request, "resume.html",
                  context={"name": "Naira",
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
                           "aboutMe": """I am a beginner Python programmer.
                                            Now, I am participating in the
                                            'Python' course of the AGBU
                                            'Women Coders' program, which
                                            started on 02.2023. I managed to
                                            study: Types and Operations,
                                            Functions, Modules, Classes
                                            and OOP, Decorator, Iterator and
                                            Generator Anonymous
                                            Function, File Manipulation. """
                           })
