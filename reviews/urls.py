from django.urls import path
from .import views


urlpatterns = [
    path("", views.ReviewView.as_view()), # as_view is ncessary to find django the get and post method. its a built-in method.
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view())
]
