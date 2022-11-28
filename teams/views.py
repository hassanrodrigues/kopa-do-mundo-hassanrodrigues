from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from .models import Team


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        return Response([model_to_dict(team) for team in teams])

    def post(self, request):

        team_dict = model_to_dict(Team.objects.create(**request.data))

        return Response(
            team_dict,
            status.HTTP_201_CREATED,
        )


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: str) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team = Team.objects.get(id=team_id)

        return Response(model_to_dict(team))

    def patch(self, request: Request, team_id: str) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team))

    def delete(self, request: Request, team_id: str) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
