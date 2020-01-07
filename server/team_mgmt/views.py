
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from team_mgmt.serializers import TeamMemberSerializer
from .models import TeamMember

from rest_framework import generics

# Create your views here.

class TeamList(generics.ListCreateAPIView):
    """
    List all team members, or create a new team member.
    """

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Creates, updates and delets a team member.
    """

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer