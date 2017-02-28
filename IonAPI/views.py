from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist
import json

class APIViewException(Exception):
    pass

class IonAPIViewSet(viewsets.ViewSet):
    """
    Base ViewSet class for IonAPI
    """

    # You must declare a serializer and queryset
    queryset = None
    serializer = None
    current_version = 1.0

    def get_version(self, request):

        return request.get('version', self.current_version)

    def get_queryset(self, request, *args, **kwargs):
        """
        Property method that return declared queryset

        :param request:
        :param args:
        :param kwargs:
        :return: queryset
        """
        try:
            assert(self.queryset != None)
        except AssertionError:
            raise APIViewException('No QuerySet declared')

        return self.queryset

    def get_serializer(self, request, *args, **kwargs):
        """
        Property method that return declared serializer

        :param request:
        :param args:
        :param kwargs:
        :return: serializer
        """
        try:
            assert(self.serializer != None)
        except AssertionError:
            raise APIViewException('No Serializer declared')

        return self.serializer


    def get_detail(self, request, *args, **kwargs):

        id = kwargs.pop('id')

        fields = request.GET.getlist('field')
        explicitly_included_fields = request.GET.getlist('add')
        show_all = bool(request.GET.get('show_all', False))

        try:
            queryset = self.get_queryset(request).get(pk=id)
        except ObjectDoesNotExist:
            rep = {id: 'Sample not found'}
            return Response(rep, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(request)(queryset, fields=fields if fields else None,
                                                  explicitly_included_fields=explicitly_included_fields, show_all=show_all, *args, **kwargs)

        return Response(serializer.data)

    def get_list(self, request):

        fields = request.GET.getlist('field')
        explicitly_included_fields = request.GET.getlist('add')

        queryset = self.get_queryset(request)
        prefetch_fields = []
        select_fields = []

        queryset = queryset.select_related(*select_fields).prefetch_related(*prefetch_fields)

        serializer = self.get_serializer(request)(queryset, fields=fields if fields else None,
                                                  explicitly_included_fields=explicitly_included_fields, many=True)

        return Response(serializer.data)

    def get_sub_list(self, request):
        #     This should be a POST
        fields = request.POST.getlist('field')
        explictly_included_fields = request.POST.getlist('add')
        ids = json.loads(request.POST.get('ids', '[]'))
        queryset = self.get_queryset(request)
        prefetch_fields = []
        select_fields = []

        if ids:
            queryset = queryset.filter(id__in = ids)

        queryset = queryset.select_related(*select_fields).prefetch_related(*prefetch_fields)

        serializer = self.get_serializer(request)(queryset, fields=fields if fields else None,
                                                  explicitly_included_fields=explictly_included_fields, many=True)

        return Response(serializer.data)

    def create(self, request):
        # not yet implemented
        pass

    def update(self, request):
        # not yet implemented
        pass