from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import PyPDF2
import docx

# FRONTEND
def home(request):
    return render(request, 'index.html')


# API
@csrf_exempt
def upload_resume(request):
    if request.method == 'POST':
        try:
            file = request.FILES.get('file')
            job_description = request.POST.get('job_description')

            print("JOB DESCRIPTION RECEIVED:", job_description)

            text = ""

            # 🔥 HANDLE PDF
            if file.name.endswith('.pdf'):
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text()

            # 🔥 HANDLE DOCX
            elif file.name.endswith('.docx'):
                doc = docx.Document(file)
                for para in doc.paragraphs:
                    text += para.text

            else:
                return JsonResponse({"error": "Only PDF or DOCX allowed"})

            text = text.lower()
            job_description = job_description.lower()

            # SKILLS
            skills_list = ["python", "sql", "machine learning", "nlp"]

            resume_skills = [s for s in skills_list if s in text]
            jd_skills = [s for s in skills_list if s in job_description]

            matched_skills = list(set(resume_skills) & set(jd_skills))
            missing_skills = list(set(jd_skills) - set(resume_skills))

            ats_score = int((len(matched_skills) / len(jd_skills)) * 100) if jd_skills else 0

            return JsonResponse({
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "ats_score": ats_score
            })

        except Exception as e:
            return JsonResponse({"error": str(e)})