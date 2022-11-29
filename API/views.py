from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie,Rating
from .serializers import MovieSerializer,RatingSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class  UserViewSet(viewsets.ModelViewSet):
    
    queryset                = User.objects.all()
    serializer_class        = UserSerializer
    



class  MovieViewSet(viewsets.ModelViewSet):
    
    
    queryset                = Movie.objects.all()
    serializer_class        = MovieSerializer
    authentication_classes  = (TokenAuthentication,)
    permission_classes      = (IsAuthenticated,)
    
    
    @action(detail=True, methods=['POST'])
    def rate_movie(self,request,pk):
    
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('user',user)
            
            try:
                rating = Rating.objects.get(user = user.id, movie = movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': "Rating updated",'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            
            except:
                rating = Rating.objects.create(user = user,movie = movie, stars = stars) 
                serializer = RatingSerializer(rating, many = False)
                response = {'message': 'Rating is created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        
        else:
            response = {'message': 'doesnt work without stars'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    

class RatingViewSet(viewsets.ModelViewSet):
    
    queryset                = Rating.objects.all()
    serializer_class        = RatingSerializer
    authentication_classes  = (TokenAuthentication,)
    permission_classes  = (IsAuthenticated,)
    
    def update(self, request, *args, **kwrags):
        response = {'message':"You can't updated rating...Sorry!! "}
        return Response(response,status=status.HTTP_403_FORBIDDEN)
    
    def create(self, request, *args, **kwrags):
        response = {'message':"You can't create again...Sorry!! "}
        return Response(response,status=status.HTTP_403_FORBIDDEN)