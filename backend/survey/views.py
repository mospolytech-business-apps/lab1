from survey.models import Survey
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import defaultdict


class SurveyView(APIView):
    def get(self, request):
        surveys = Survey.objects.all()

        questions = [
            "Please rate our aircraft flown on AMONIC Airlines:",
            "How would you rate out flight attendants:",
            "How would you rate out inflight entertainments:",
            "Please rate the ticket price for the trip you are taking:",
        ]

        metics = [
            "Outstanding",
            "Very Good",
            "Good",
            "Adequate",
            "Needs Improvement",
            "Poor",
            "Don't know",
        ]

        data = defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: [x for x in range(14)]))
        )

        for survey in surveys:
            month = survey.month.strftime("%B %Y")

            for i, question in enumerate(["q1", "q2", "q3", "q4"]):
                q_text = questions[i]
                key = survey.__getattribute__(question)
                if key != 0 and key != " ":
                    key = int(key) - 1
                else:
                    break

                key = metics[key]

                metric_list = data[month][q_text][key]

                if survey.gender == "M":
                    metric_list[0] += 1
                if survey.gender == "F":
                    metric_list[1] += 1

                age = int(survey.age) if isinstance(survey.age, int) else -1
                if age != -1:
                    if 18 <= age <= 24:
                        metric_list[2] += 1
                    if 25 <= age <= 39:
                        metric_list[3] += 1
                    if 40 <= age <= 59:
                        metric_list[4] += 1
                    if age >= 60:
                        metric_list[5] += 1

                if survey.cabintype == "Economy":
                    metric_list[6] += 1
                if survey.cabintype == "Business":
                    metric_list[7] += 1
                if survey.cabintype == "First":
                    metric_list[8] += 1

                if survey.arrival == "AUH":
                    metric_list[9] += 1
                if survey.arrival == "BAH":
                    metric_list[10] += 1
                if survey.arrival == "DOH":
                    metric_list[11] += 1
                if survey.arrival == "RYU":
                    metric_list[12] += 1
                if survey.arrival == "CAI":
                    metric_list[13] += 1

        response = Response(data)
        response["X-Object-Count"] = Survey.objects.all().count()

        return response
