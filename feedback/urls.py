from django.urls import path



app_name = "feedback"
urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
]
