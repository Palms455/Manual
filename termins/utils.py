from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination



class PaginateMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    def paginate_run(self, obj):
    	page = self.paginate_queryset(obj)
    	if page is not None:
    		serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
    	else:
    		serializer = self.serializer_class(obj, many=True)
    	return Response(serializer.data, status=status.HTTP_200_OK)

    	 # the many param informs the serializer that it will be serializing
		 # more than a single schedule.

class ValidateData(object):

	schedule = None
	version = None

	def validate_element(self):
		if not in_code:
			content = {"code": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		if not in_value:
			content = {"value": ["This field may not be blank."]}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)
		try:
			element = Element.objects.get(code=in_code, schedule=item)
		except Element.DoesNotExist:
			content={f'{in_code} does not exist'}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		if element.value != in_value:
			content={f'{in_value} does not equal {element.value}'}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response({"all checked!!!"})