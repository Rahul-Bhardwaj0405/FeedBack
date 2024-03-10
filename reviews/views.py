from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView # This is especially used in classes which are rendering templates only.like ThankYou class here.
from .models import Review
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


# Create your views here. You can create view using class and function both and same time also. let's see that.Note: write view using class if its very important.

# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#             })
    

#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             return HttpResponseRedirect("/thank-you")
            
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"



# def thank_you(request):
#     return render(request, "reviews/thank_you.html")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review   # django send the Review model into the "review_list.html" as "object_list".
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["reviews"] = selected_review
#         return context


class SingleReviewView(DetailView):
        template_name = "reviews/single_review.html"
        model = Review


        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            loaded_review = self.object
            request = self.request
            favorite_id = request.session.get("favorite_review")
            context["is_favorite"] = favorite_id == str(loaded_review.id)
            return context




# Session
        
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)