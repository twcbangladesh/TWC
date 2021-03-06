from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (TestView,
                    GuardianDetailsView,
                    GuardianHistoryView,
                    GuardianListView,
                    TeacherDetailsListView,
                    TeacherDetailsView,
                    TeacherHistoryView,
                    FollowUpView,
                    FollowUpGuardianTableView,
                    FollowUpTuitionTableView,
                    TemporaryTuitionForChildListView, ShortListCreateView, ShortListView,
                    PermanentCreateView, PermanentListView,
                    ChildUpdateView, GuardianUpdateView,
                    AddNoteToGuardian, AddNoteToChild, AutoRecommendationView,
                    AutoToTemporary, TemporaryToShortList, ShortListToAssigned,
                    AssignedToDemo, AssignedShortListView,
                    SendSMSView, SendSMSViewtest, ReminderListView,
                    ReminderListUpdateView, ReminderView,
                    FollowUpConfirm, FollowUpAssign, FollowUpPaid, FollowUpCanceled,
                    AddRating, SetPaid, DemoToPermanent, DemoShortListView)

urlpatterns = [
    path('api/temporary/', TemporaryTuitionForChildListView.as_view()),
    path('api/short/create/', ShortListCreateView.as_view()),
    path('api/short/', ShortListView.as_view()),
    path('api/permanent/create/', ShortListCreateView.as_view()),
    path('api/permanent/', PermanentListView.as_view()),
    path('api/assigned/', AssignedShortListView.as_view()),
    path('api/demo/', DemoShortListView.as_view()),
    path('api/auto/', AutoRecommendationView.as_view()),
    path('api/guardian/', GuardianListView.as_view()),
    path('api/guardian/<pk>', GuardianDetailsView.as_view()),
    path('api/guardian/<pk>/update/', GuardianUpdateView.as_view()),
    path('api/guardian/<pk>/note/', AddNoteToGuardian.as_view()),
    path('api/child/<pk>/note/', AddNoteToChild.as_view()),
    path('api/child/<pk>', ChildUpdateView.as_view()),
    path('api/guardian/history/<pk>', GuardianHistoryView.as_view()),
    path('api/reminder/', ReminderListView.as_view()),
    path('api/reminder/<pk>', ReminderListUpdateView.as_view()),
    path('api/addrating/', login_required(AddRating.as_view())),

    path('api/auto_temporary/', AutoToTemporary.as_view()),
    path('api/temporary_sort/', TemporaryToShortList.as_view()),
    path('api/sort_assign/', ShortListToAssigned.as_view()),
    path('api/assign_demo/', AssignedToDemo.as_view()),
    path('api/demo_permanent/', DemoToPermanent.as_view()),

    path('teacher/', TeacherDetailsListView.as_view()),
    path('teacher/<pk>', TeacherDetailsView.as_view()),
    path('teacher/history/<pk>', TeacherHistoryView.as_view()),
    path('', login_required(FollowUpView.as_view())),
    path('guardian/', FollowUpGuardianTableView.as_view()),
    path('portal/', login_required(FollowUpTuitionTableView.as_view())),
    path('reminders/', login_required(ReminderView.as_view())),
    path('confirms/', login_required(FollowUpConfirm.as_view())),
    path('assings/', login_required(FollowUpAssign.as_view())),
    path('paids/', login_required(FollowUpPaid.as_view())),
    path('canceleds/', login_required(FollowUpCanceled.as_view())),
    path('sms/', login_required(SendSMSView.as_view())),
    path('smstest/', SendSMSViewtest.as_view()),
    path('setpaid', SetPaid.as_view()),
]