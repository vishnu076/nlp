from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as e


# Create your views here.
class mood(APIView):
    def post(self,request,format=None):
        d=request.data
        f=e()
        t=d['text']
        r=f.polarity_scores(t)
        r["Access-Control-Allow-Orgin"]="*"
    
        return Response(r,status=400)
    def get(self,request,format=None):
        d="idhvis"
        return Response(d,status=200)    
    
    
