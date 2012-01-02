from django.conf.urls.defaults import *
from views import *
from report import *

urlpatterns = patterns('',
    (r'^get_student/(?P<id>\d+)/$', student_page_redirect),
    (r'^reports/$', school_report_builder_view),
    (r'^reports/transcript_nonofficial/(?P<id>\d+)/$', transcript_nonofficial),
    (r'^flashcard/$', photo_flash_card),
    (r'^flashcard/(?P<year>\d+)/$', photo_flash_card),
    (r'^grade_report/$', grade_report),
    (r'^teacher_attendance/$', teacher_attendance),
    (r'^teacher_attendance/(?P<type>[a-z]+)/$', teacher_attendance),
    (r'^teacher_attendance/(?P<type>[a-z]+)/(?P<course>\d+)/$', teacher_attendance),
    (r'^import/$', import_everything),
    (r'^teacher_submissions/$', teacher_submissions),
    (r'^asp_submissions/$', asp_submissions),
    (r'^studentattendance/report/$', attendance_report),
    (r'^studentattendance/student/(?P<id>\d+)/$', attendance_student),
    (r'^preferences/$', user_preferences),
    (r'^view_student/$', view_student),
    (r'^view_student/(?P<id>\d+)/$', view_student),
    (r'^student/naviance/$', import_naviance),
)
