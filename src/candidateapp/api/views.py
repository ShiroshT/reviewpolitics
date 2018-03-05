from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from candidateapp.models import CandidatesWiki


from .pagination import StandardResultsPagination
from .serializers import CandidateModelSerializer





class CandidatesWikiListAPIView(generics.ListAPIView):
    serializer_class = CandidateModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(CandidatesWikiListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    # def get_queryset(self, *args, **kwargs):
    # 	return CandidatesWiki.objects.all()


    
    def get_queryset(self, *args, **kwargs):
        
        max_datetime = CandidatesWiki.objects.all().order_by('id')
        qs = CandidatesWiki.objects.all()

        query = self.request.GET.get("q", None)
        if query is not None:
            query = query.strip()
            qs = qs.filter( 
                Q(candiate_name__icontains=query) |
                Q(content_wiki__icontains=query) |
                Q(summary_wiki__icontains=query)
            )
        return qs 

    	
        # requested_user = self.kwargs.get("username")
        
        # if requested_user:
        #     qs = Tweet.objects.filter(user__username=requested_user).order_by("-timestamp")
        # else:
        #     im_following = self.request.user.profile.get_following() # none
        #     qs1 = Tweet.objects.filter(user__in=im_following)
        #     qs2 = Tweet.objects.filter(user=self.request.user)
        #     qs = (qs1 | qs2).distinct().order_by("-timestamp")
        
        # query = self.request.GET.get("q", None)
        # if query is not None:
        #     qs = qs.filter(
        #             Q(content__icontains=query) |
        #             Q(user__username__icontains=query)
        #             )
        # return qs

    # def get_queryset(self, *args, **kwargs):
        
    #     max_datetime = CandidatesWiki.objects.all().latest('fecha_ini_det')
    #     qs = CandidatesWiki.objects.all()

    #     query = self.request.GET.get("q", None)
    #     if query is not None:
    #         query = query.strip()
    #         qs = qs.filter( 
    #             Q(candiate_name__icontains=query) |
    #             Q(content_wiki__icontains=query) |
    #             Q(summary_wiki__icontains=query)
    #         )
    #     return qs 