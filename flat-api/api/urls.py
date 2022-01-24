from django.urls import include, path

from api.views import branch as branch_views
from api.views import commit as commit_views
from api.views import pr as pr_views

branches_urls = [
    path('',
         branch_views.BranchView.as_view(),
         name='branches_list'),
    path('<str:branch>/commits/',
         commit_views.CommitListView.as_view(),
         name='branch_commits_list'),
]

commits_urls = [
    path('<str:commit_hex>/',
         commit_views.CommitDetailView.as_view(),
         name='commit_detail'),
]

pull_requests_urls = [
    path('',
         pr_views.PullRequestView.as_view(),
         name='pull_request_list_and_create'),
]

urlpatterns = [
    path('branches/', include(branches_urls)),
    path('commits/', include(commits_urls)),
    path('pull_requests/', include(pull_requests_urls)),
]
