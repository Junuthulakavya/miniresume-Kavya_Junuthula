from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer

# In-memory storage
RESUME_STORAGE = []


class HealthCheckView(APIView):
    def get(self, request):
        return Response(
            {"status": "healthy"},
            status=status.HTTP_200_OK
        )


class ResumeCreateView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            RESUME_STORAGE.append(serializer.validated_data)

            return Response(
                {
                    "message": "Resume submitted successfully",
                    "data": serializer.validated_data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResumeListView(APIView):
    def get(self, request):
        return Response(
            {
                "count": len(RESUME_STORAGE),
                "resumes": RESUME_STORAGE
            },
            status=status.HTTP_200_OK
        )
