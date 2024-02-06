from django.contrib import admin

# add include to the path
from django.urls import path, include

# import views from todo

from bonethree import views

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers

# create a router object
router = routers.DefaultRouter()

# register the router
router.register(r'bonetwo',views.BonetwoView, 'bonetwo')
router.register(r'bonethree',views.BonethreeView, 'bonethree')
router.register(r'boneone',views.BoneoneView, 'boneone')
router.register(r'bonefour',views.BonefourView, 'bonefour')
router.register(r'bonefive',views.BonefiveView, 'bonefive')
router.register(r'bonesix',views.BonesixView, 'bonesix')
router.register(r'boneseven',views.BonesevenView, 'boneseven')
router.register(r'btwoone',views.BtwooneView, 'btwoone')
router.register(r'btwotwo',views.BtwotwoView, 'btwotwo')
router.register(r'btwothree',views.BtwothreeView, 'btwothree')
router.register(r'btwofour',views.BtwofourView, 'btwofour')
router.register(r'btwofive',views.BtwofiveView, 'btwofive')
router.register(r'btwosix',views.BtwosixView, 'btwosix')
router.register(r'btwoseven',views.BtwosevenView, 'btwoseven')
router.register(r'btwoeight',views.BtwoeightView, 'btwoeight')
router.register(r'btwonine',views.BtwonineView, 'btwonine')
router.register(r'btwoten',views.BtwotenView, 'btwoten')
router.register(r'btwoeleven',views.BtwoelevenView, 'btwoeleven')
router.register(r'btwotwelve',views.BtwotwelveView, 'btwotwelve')
router.register(r'btwothirteen',views.BtwothirteenView, 'btwothirteen')
router.register(r'btwofourteen',views.BtwofourteenView, 'btwofourteen')
router.register(r'btwofifteen',views.BtwofifteenView, 'btwofifteen')

router.register(r'bthreeone',views.BthreeoneView, 'bthreeone')
router.register(r'bthreetwo',views.BthreetwoView, 'bthreetwo')
router.register(r'bthreethree',views.BthreethreeView, 'bthreethree')
router.register(r'bthreefour',views.BthreefourView, 'bthreefour')
router.register(r'bthreefive',views.BthreefiveView, 'bthreefive')
router.register(r'bthreesix',views.BthreesixView, 'bthreesix')
router.register(r'bthreethreetwo',views.BthreethreetwoView, 'bthreethreetwo')
router.register(r'bthreeseven',views.BthreesevenView, 'bthreeseven')
router.register(r'bthreeeight',views.BthreeeightView, 'bthreeeight')
router.register(r'bthreenine',views.BthreenineView, 'bthreenine')
router.register(r'bthreeten',views.BthreetenView, 'bthreeten')
router.register(r'bthreeeleven',views.BthreeelevenView, 'bthreeeleven')
router.register(r'bthreetwelve',views.BthreetwelveView, 'bthreetwelve')
router.register(r'bthreethirteen',views.BthreethirteenView, 'bthreethirteen')
router.register(r'bthreefourteen',views.BthreefourteenView, 'bthreefourteen')
router.register(r'bthreefifteen',views.BthreefifteenView, 'bthreefifteen')


router.register(r'bfourone',views.BfouroneView, 'bfourone')
router.register(r'bfourtwo',views.BfourtwoView, 'bfourtwo')
router.register(r'bfourthree',views.BfourthreeView, 'bfourthree')
router.register(r'bfourfour',views.BfourfourView, 'bfourfour')
router.register(r'bfourfive',views.BfourfiveView, 'bfourfive')
router.register(r'bfoursix',views.BfoursixView, 'bfourosix')
router.register(r'bfourseven',views.BfoursevenView, 'bfourseven')


router.register(r'bfiveone',views.BfiveoneView, 'bfiveone')
router.register(r'bfivetwo',views.BfivetwoView, 'bfivetwo')
router.register(r'bfivethree',views.BfivethreeView, 'bfivethree')
router.register(r'bfivefour',views.BfivefourView, 'bfivefour')
router.register(r'bfivefive',views.BfivefiveView, 'bfivefive')
router.register(r'bfivesix',views.BfivesixView, 'bfiveosix')
router.register(r'bfiveseven',views.BfivesevenView, 'bfiveoseven')
router.register(r'bfiveeight',views.BfiveeightView, 'bfiveeight')
router.register(r'bfivenine',views.BfivenineView, 'bfivenine')
router.register(r'bfiveten',views.BfivetenView, 'bfiveten')
router.register(r'bfiveeleven',views.BfiveelevenView, 'bfiveeleven')

router.register(r'bsixone',views.BsixoneView, 'bsixone')
router.register(r'bsixtwo',views.BsixtwoView, 'bsixtwo')
router.register(r'bsixthree',views.BsixthreeView, 'bsixthree')
router.register(r'bsixfour',views.BsixfourView, 'bsixfour')
router.register(r'bsixfive',views.BsixfiveView, 'bsixfive')
router.register(r'bsixsix',views.BsixsixView, 'bsixsix')
router.register(r'bsixseven',views.BsixsevenView, 'bsixseven')
router.register(r'bsixeight',views.BsixeightView, 'bsixeight')
router.register(r'bsixnine',views.BsixnineView, 'bsixnine')
router.register(r'bsixten',views.BsixtenView, 'bsixten')
router.register(r'bsixeleven',views.BsixelevenView, 'bsixeleven')
router.register(r'bsixtwelve',views.BsixtwelveView, 'bsixtwelve')

router.register(r'bsevenone',views.BsevenoneView, 'bsevenone')
router.register(r'bseventwo',views.BseventwoView, 'bseventwo')
router.register(r'bseventhree',views.BseventhreeView, 'bseventhree')
router.register(r'bsevenfour',views.BsevenfourView, 'bsevenfour')
router.register(r'bsevenfive',views.BsevenfiveView, 'bsevenfive')
router.register(r'bsevensix',views.BsevensixView, 'bsevensix')
router.register(r'bsevenseven',views.BsevensevenView, 'bsevenseven')
router.register(r'bseveneight',views.BseveneightView, 'bseveneight')
router.register(r'bsevennine',views.BsevennineView, 'bsevennine')
router.register(r'bseventen',views.BseventenView, 'bseventen')
router.register(r'bseveneleven',views.BsevenelevenView, 'bseveneleven')
router.register(r'bseventwelve',views.BseventwelveView, 'bseventwelve')


router.register(r'aoneone',views.AoneoneView, 'aoneone')
router.register(r'aonetwo',views.AonetwoView, 'aonetwo')
router.register(r'aonethree',views.AonethreeView, 'aonethree')
router.register(r'aonefour',views.AonefourView, 'aonefour')
router.register(r'aonefive',views.AonefiveView, 'aonefive')
router.register(r'atwoone',views.AtwooneView, 'atwoone')
router.register(r'atwotwo',views.AtwotwoView, 'atwotwo')
router.register(r'atwothree',views.AtwothreeView, 'atwothree')
router.register(r'atwofour',views.AtwofourView, 'atwofour')
router.register(r'atwofive',views.AtwofiveView, 'atwofive')
router.register(r'atwosix',views.AtwosixView, 'atwosix')
router.register(r'atwoseven',views.AtwosevenView, 'atwoseven')
router.register(r'atwoeight',views.AtwoeightView, 'atwoeight')
router.register(r'atwonine',views.AtwonineView, 'atwonine')
router.register(r'atwoten',views.AtwotenView, 'atwoten')
router.register(r'atwoeleven',views.AtwoelevenView, 'atwoeleven')
router.register(r'atwotwelve',views.AtwotwelveView, 'atwotwelve')
router.register(r'atwothirteen',views.AtwothirteenView, 'atwothirteen')
router.register(r'atwofourteen',views.AtwofourteenView, 'atwofourteen')
router.register(r'atwofifteen',views.AtwofifteenView, 'atwofifteen')
router.register(r'atwosixteen',views.AtwosixteenView, 'atwosixteen')
router.register(r'atwoseventeen',views.AtwoseventeenView, 'atwoseventeen')
router.register(r'atwoeightteen',views.AtwoeightteenView, 'atwoeightteen')
router.register(r'atwonineteen',views.AtwonineteenView, 'atwonineteen')
router.register(r'atwotwenty',views.AtwotwentyView, 'atwotwenty')
router.register(r'atwotwentyone',views.AtwotwentyoneView, 'atwotwentyone')
router.register(r'atwotwentytwo',views.AtwotwentytwoView, 'atwotwentytwo')
router.register(r'atwotwentythree',views.AtwotwentythreeView, 'atwotwentythree')
router.register(r'atwotwentyfour',views.AtwotwentyfourView, 'atwotwentyfour')
router.register(r'atwotwentyfive',views.AtwotwentyfiveView, 'atwotwentyfive')
router.register(r'athreeone',views.AthreeoneView, 'athreeone')
router.register(r'athreetwo',views.AthreetwoView, 'athreetwo')
router.register(r'athreethree',views.AthreethreeView, 'athreethree')
router.register(r'athreefour',views.AthreefourView, 'athreefour')
router.register(r'athreefive',views.AthreefiveView, 'athreefive')

urlpatterns = [
	path('admin/', admin.site.urls),

	# add another path to the url patterns
	# when you visit the localhost:8000/api
	# you should be routed to the django Rest framework
	path('api/', include(router.urls))


]
