from django.conf.urls import url

from .views import add_view, BookListView, BookSearchResultsView


urlpatterns = [
    url(r'^$', BookListView.as_view(), name='index'),
    url(r'^page/(?P<page>[0-9]+)$', BookListView.as_view(), name='paginator'),
    url(r'^search_results/$', BookSearchResultsView.as_view(), name='search_results'),
    url(r'^import-helper/$', add_view),
]